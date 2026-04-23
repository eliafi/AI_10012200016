#!/usr/bin/env python3
"""Run custom retrieval pipeline: embeddings, FAISS index, baseline retrieval, and hybrid retrieval."""

from __future__ import annotations

import argparse
import json
import statistics
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class RetrievalConfig:
    embedding_model: str
    top_k: int
    hybrid_alpha: float


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_json_list(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def pick_chunk_file(code_root: Path, explicit_chunk_file: Path | None) -> Path:
    if explicit_chunk_file is not None:
        return explicit_chunk_file

    results_path = code_root / "eval" / "chunking_results.json"
    if results_path.exists():
        results = load_json(results_path)
        best = results.get("best_strategy")
        strategy_results = results.get("strategy_results", [])
        for item in strategy_results:
            if item.get("strategy") == best:
                chunk_file = Path(item.get("chunk_file", ""))
                if chunk_file.exists():
                    return chunk_file

    fallback = code_root / "data" / "processed" / "chunks_large.jsonl"
    if fallback.exists():
        return fallback

    raise FileNotFoundError("No chunk file found. Run data preparation first.")


def save_chunk_lookup(chunks: list[dict[str, Any]], metadata_dir: Path) -> Path:
    lookup = [
        {
            "position": idx,
            "chunk_id": chunk["chunk_id"],
            "source": chunk["source"],
            "doc_id": chunk["doc_id"],
        }
        for idx, chunk in enumerate(chunks)
    ]
    path = metadata_dir / "chunk_lookup.json"
    write_json(path, {"count": len(lookup), "items": lookup})
    return path


def build_embeddings(
    chunks: list[dict[str, Any]],
    model_name: str,
) -> tuple[np.ndarray, SentenceTransformer]:
    model = SentenceTransformer(model_name)
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    embeddings = embeddings.astype(np.float32)
    return embeddings, model


def build_faiss_index(embeddings: np.ndarray) -> faiss.Index:
    dimension = int(embeddings.shape[1])
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    return index


def normalize_array(values: np.ndarray) -> np.ndarray:
    if values.size == 0:
        return values
    min_v = float(values.min())
    max_v = float(values.max())
    if max_v - min_v < 1e-12:
        return np.zeros_like(values)
    return (values - min_v) / (max_v - min_v)


def is_relevant(chunk: dict[str, Any], query_spec: dict[str, Any]) -> bool:
    if chunk["source"] != query_spec["expected_source"]:
        return False

    text = chunk["text"].lower()
    must_all = [term.lower() for term in query_spec.get("must_contain_all", [])]
    must_any = [term.lower() for term in query_spec.get("must_contain_any", [])]

    if must_all and not all(term in text for term in must_all):
        return False
    if must_any and not any(term in text for term in must_any):
        return False
    return True


def retrieve_vector(
    query: str,
    model: SentenceTransformer,
    index: faiss.Index,
    chunks: list[dict[str, Any]],
    top_k: int,
) -> list[dict[str, Any]]:
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)
    scores, indices = index.search(query_embedding, top_k)

    retrieved: list[dict[str, Any]] = []
    for rank, (idx, score) in enumerate(zip(indices[0], scores[0]), start=1):
        if idx < 0:
            continue
        chunk = chunks[int(idx)]
        retrieved.append(
            {
                "rank": rank,
                "chunk_id": chunk["chunk_id"],
                "source": chunk["source"],
                "doc_id": chunk["doc_id"],
                "vector_score": float(score),
                "hybrid_score": float(score),
                "text_preview": chunk["text"][:220],
            }
        )
    return retrieved


def retrieve_hybrid(
    query: str,
    model: SentenceTransformer,
    embeddings: np.ndarray,
    vectorizer: TfidfVectorizer,
    tfidf_matrix: Any,
    chunks: list[dict[str, Any]],
    top_k: int,
    alpha: float,
) -> list[dict[str, Any]]:
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)[0]

    vector_scores = embeddings @ query_embedding
    keyword_scores = cosine_similarity(vectorizer.transform([query]), tfidf_matrix).ravel()

    vector_norm = normalize_array(vector_scores)
    keyword_norm = normalize_array(keyword_scores)
    hybrid_scores = alpha * vector_norm + (1.0 - alpha) * keyword_norm

    top_indices = np.argsort(hybrid_scores)[::-1][:top_k]

    retrieved: list[dict[str, Any]] = []
    for rank, idx in enumerate(top_indices, start=1):
        chunk = chunks[int(idx)]
        retrieved.append(
            {
                "rank": rank,
                "chunk_id": chunk["chunk_id"],
                "source": chunk["source"],
                "doc_id": chunk["doc_id"],
                "vector_score": float(vector_scores[int(idx)]),
                "keyword_score": float(keyword_scores[int(idx)]),
                "hybrid_score": float(hybrid_scores[int(idx)]),
                "text_preview": chunk["text"][:220],
            }
        )
    return retrieved


def evaluate_method(
    method_name: str,
    query_specs: list[dict[str, Any]],
    chunks: list[dict[str, Any]],
    retrieve_fn: Callable[[str], list[dict[str, Any]]],
    top_k: int,
) -> dict[str, Any]:
    precision_values: list[float] = []
    recall_values: list[float] = []
    mrr_values: list[float] = []
    top1_hits: list[int] = []
    per_query: list[dict[str, Any]] = []

    for query_spec in query_specs:
        retrieved = retrieve_fn(query_spec["query"])
        total_relevant = sum(1 for chunk in chunks if is_relevant(chunk, query_spec))

        hits = 0
        reciprocal_rank = 0.0
        retrieved_rows: list[dict[str, Any]] = []

        for item in retrieved:
            chunk = next(c for c in chunks if c["chunk_id"] == item["chunk_id"])
            relevant = is_relevant(chunk, query_spec)
            if relevant:
                hits += 1
                if reciprocal_rank == 0.0:
                    reciprocal_rank = 1.0 / float(item["rank"])

            row = dict(item)
            row["relevant"] = relevant
            retrieved_rows.append(row)

        precision = hits / float(top_k)
        recall = (hits / float(total_relevant)) if total_relevant > 0 else 0.0
        top1_relevant = 1 if (retrieved_rows and retrieved_rows[0]["relevant"]) else 0

        precision_values.append(precision)
        recall_values.append(recall)
        mrr_values.append(reciprocal_rank)
        top1_hits.append(top1_relevant)

        per_query.append(
            {
                "query_id": query_spec["id"],
                "query": query_spec["query"],
                "failure_case": bool(query_spec.get("failure_case", False)),
                "expected_source": query_spec["expected_source"],
                "total_relevant_chunks": int(total_relevant),
                "precision_at_k": precision,
                "recall_at_k": recall,
                "mrr_at_k": reciprocal_rank,
                "top1_relevant": bool(top1_relevant),
                "retrieved": retrieved_rows,
            }
        )

    summary = {
        "method": method_name,
        "top_k": top_k,
        "queries_evaluated": len(query_specs),
        "precision_at_k": float(statistics.mean(precision_values)) if precision_values else 0.0,
        "recall_at_k": float(statistics.mean(recall_values)) if recall_values else 0.0,
        "mrr_at_k": float(statistics.mean(mrr_values)) if mrr_values else 0.0,
        "top1_accuracy": float(statistics.mean(top1_hits)) if top1_hits else 0.0,
    }
    return {"summary": summary, "per_query": per_query}


def build_failure_analysis(
    baseline_eval: dict[str, Any],
    hybrid_eval: dict[str, Any],
) -> dict[str, Any]:
    baseline_by_id = {row["query_id"]: row for row in baseline_eval["per_query"]}
    hybrid_by_id = {row["query_id"]: row for row in hybrid_eval["per_query"]}

    details: list[dict[str, Any]] = []
    improved = 0

    for qid, base_row in baseline_by_id.items():
        if not base_row.get("failure_case", False):
            continue

        hyb_row = hybrid_by_id[qid]
        baseline_failed = (not base_row["top1_relevant"]) or (base_row["recall_at_k"] < 1.0)
        improved_case = (hyb_row["mrr_at_k"] > base_row["mrr_at_k"]) or (
            hyb_row["top1_relevant"] and not base_row["top1_relevant"]
        )

        if improved_case:
            improved += 1

        details.append(
            {
                "query_id": qid,
                "query": base_row["query"],
                "baseline_failed": baseline_failed,
                "baseline_top1_relevant": base_row["top1_relevant"],
                "hybrid_top1_relevant": hyb_row["top1_relevant"],
                "baseline_mrr_at_k": base_row["mrr_at_k"],
                "hybrid_mrr_at_k": hyb_row["mrr_at_k"],
                "improved_with_hybrid": improved_case,
                "baseline_top3": base_row["retrieved"][:3],
                "hybrid_top3": hyb_row["retrieved"][:3],
            }
        )

    baseline_failures = sum(1 for row in details if row["baseline_failed"])
    return {
        "failure_queries_evaluated": len(details),
        "baseline_failure_count": baseline_failures,
        "improved_count": improved,
        "details": details,
    }


def write_markdown_report(
    report_path: Path,
    config: RetrievalConfig,
    chunk_file: Path,
    chunk_count: int,
    baseline_eval: dict[str, Any],
    hybrid_eval: dict[str, Any],
    failure_analysis: dict[str, Any],
) -> None:
    b = baseline_eval["summary"]
    h = hybrid_eval["summary"]

    lines: list[str] = []
    lines.append("# Retrieval System Analysis")
    lines.append("")
    lines.append("## Design Choices")
    lines.append("- Embedding pipeline: local sentence-transformers")
    lines.append("- Embedding model: {}".format(config.embedding_model))
    lines.append("- Vector storage: FAISS (IndexFlatIP)")
    lines.append("- Similarity metric: cosine similarity")
    lines.append("- Retrieval extension: hybrid search (vector + keyword)")
    lines.append("- Default top-k: {}".format(config.top_k))
    lines.append("")
    lines.append("## Corpus")
    lines.append("- Chunk file: {}".format(str(chunk_file)))
    lines.append("- Number of chunks indexed: {}".format(chunk_count))
    lines.append("")
    lines.append("## Baseline Vs Hybrid")
    lines.append("| Method | Recall@{} | MRR@{} | Precision@{} | Top1 Accuracy |".format(config.top_k, config.top_k, config.top_k))
    lines.append("|---|---:|---:|---:|---:|")
    lines.append(
        "| Vector only | {:.4f} | {:.4f} | {:.4f} | {:.4f} |".format(
            b["recall_at_k"], b["mrr_at_k"], b["precision_at_k"], b["top1_accuracy"]
        )
    )
    lines.append(
        "| Hybrid | {:.4f} | {:.4f} | {:.4f} | {:.4f} |".format(
            h["recall_at_k"], h["mrr_at_k"], h["precision_at_k"], h["top1_accuracy"]
        )
    )
    lines.append("")
    lines.append("## Failure Case Summary")
    lines.append("- Failure queries evaluated: {}".format(failure_analysis["failure_queries_evaluated"]))
    lines.append("- Baseline failures: {}".format(failure_analysis["baseline_failure_count"]))
    lines.append("- Cases improved by hybrid: {}".format(failure_analysis["improved_count"]))
    lines.append("")
    lines.append("## Proposed Fix")
    lines.append("- Baseline issue: dense-vector-only retrieval misses keyword-heavy and table-like queries.")
    lines.append("- Implemented fix: hybrid scoring = alpha * vector_score + (1 - alpha) * keyword_score.")
    lines.append("- Alpha used: {:.2f}".format(config.hybrid_alpha))

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    code_root = script_path.parents[2]

    parser = argparse.ArgumentParser(description="Run custom retrieval system pipeline")
    parser.add_argument("--chunk-file", type=Path, default=None)
    parser.add_argument(
        "--queries",
        type=Path,
        default=code_root / "eval" / "retrieval_queries.json",
    )
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--embedding-model", type=str, default="sentence-transformers/all-MiniLM-L6-v2")
    parser.add_argument("--hybrid-alpha", type=float, default=0.55)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_path = Path(__file__).resolve()
    code_root = script_path.parents[2]

    chunk_file = pick_chunk_file(code_root=code_root, explicit_chunk_file=args.chunk_file)
    if not args.queries.exists():
        raise FileNotFoundError(f"Query file not found: {args.queries}")

    config = RetrievalConfig(
        embedding_model=args.embedding_model,
        top_k=int(args.top_k),
        hybrid_alpha=float(args.hybrid_alpha),
    )

    chunks = load_jsonl(chunk_file)
    query_specs = load_json_list(args.queries)

    faiss_dir = code_root / "indexes" / "faiss"
    metadata_dir = code_root / "indexes" / "metadata"
    eval_dir = code_root / "eval"
    docs_dir = code_root / "docs" / "manual_logs"
    logs_dir = code_root / "logs" / "experiments"

    faiss_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)
    eval_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    embeddings, model = build_embeddings(chunks=chunks, model_name=config.embedding_model)
    index = build_faiss_index(embeddings)

    faiss_index_path = faiss_dir / "retrieval.index"
    embeddings_path = faiss_dir / "chunk_embeddings.npy"
    faiss.write_index(index, str(faiss_index_path))
    np.save(embeddings_path, embeddings)

    lookup_path = save_chunk_lookup(chunks=chunks, metadata_dir=metadata_dir)

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform([chunk["text"] for chunk in chunks])

    baseline_eval = evaluate_method(
        method_name="vector_only",
        query_specs=query_specs,
        chunks=chunks,
        retrieve_fn=lambda q: retrieve_vector(
            query=q,
            model=model,
            index=index,
            chunks=chunks,
            top_k=config.top_k,
        ),
        top_k=config.top_k,
    )

    hybrid_eval = evaluate_method(
        method_name="hybrid",
        query_specs=query_specs,
        chunks=chunks,
        retrieve_fn=lambda q: retrieve_hybrid(
            query=q,
            model=model,
            embeddings=embeddings,
            vectorizer=vectorizer,
            tfidf_matrix=tfidf_matrix,
            chunks=chunks,
            top_k=config.top_k,
            alpha=config.hybrid_alpha,
        ),
        top_k=config.top_k,
    )

    failure_analysis = build_failure_analysis(
        baseline_eval=baseline_eval,
        hybrid_eval=hybrid_eval,
    )

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "design_choices": {
            "embedding_pipeline": "local sentence-transformers",
            "embedding_model": config.embedding_model,
            "vector_storage": "FAISS IndexFlatIP",
            "similarity_metric": "cosine",
            "extension": "hybrid search (keyword + vector)",
            "top_k": config.top_k,
            "hybrid_alpha": config.hybrid_alpha,
            "evaluation_queries": len(query_specs),
        },
        "corpus": {
            "chunk_file": str(chunk_file),
            "chunks_indexed": len(chunks),
        },
        "artifacts": {
            "faiss_index": str(faiss_index_path),
            "embeddings": str(embeddings_path),
            "chunk_lookup": str(lookup_path),
            "queries": str(args.queries),
        },
        "baseline": baseline_eval,
        "hybrid": hybrid_eval,
        "failure_case_analysis": failure_analysis,
    }

    eval_path = eval_dir / "retrieval_results.json"
    log_path = logs_dir / "retrieval_run_summary.json"
    report_path = docs_dir / "retrieval_analysis.md"

    write_json(eval_path, payload)
    write_json(log_path, payload)
    write_markdown_report(
        report_path=report_path,
        config=config,
        chunk_file=chunk_file,
        chunk_count=len(chunks),
        baseline_eval=baseline_eval,
        hybrid_eval=hybrid_eval,
        failure_analysis=failure_analysis,
    )

    print(f"Retrieval pipeline complete. Results: {eval_path}")
    print(f"Retrieval report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
