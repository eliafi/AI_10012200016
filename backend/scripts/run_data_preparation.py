#!/usr/bin/env python3
"""Part A pipeline: data cleaning, chunking design, and chunking impact comparison."""

from __future__ import annotations

import argparse
import json
import re
import statistics
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    import tiktoken
except ModuleNotFoundError:  # pragma: no cover - fallback when tiktoken is unavailable
    tiktoken = None


@dataclass(frozen=True)
class ChunkStrategy:
    name: str
    max_tokens: int
    overlap_tokens: int
    boundary_rule: str


STRATEGIES: list[ChunkStrategy] = [
    ChunkStrategy("small", max_tokens=180, overlap_tokens=30, boundary_rule="sentence-aware"),
    ChunkStrategy("medium", max_tokens=360, overlap_tokens=60, boundary_rule="sentence-aware"),
    ChunkStrategy("large", max_tokens=600, overlap_tokens=100, boundary_rule="sentence-aware"),
]


HEADER_PATTERN = re.compile(
    r"resetting the economy for the ghana we want\s+2025 budget\s+[ivxlcdm0-9]+", re.IGNORECASE
)
MULTISPACE_PATTERN = re.compile(r"\s+")
DOT_LEADER_PATTERN = re.compile(r"\.{3,}")


class Tokenizer:
    def __init__(self) -> None:
        self._encoder = None
        if tiktoken is not None:
            self._encoder = tiktoken.get_encoding("cl100k_base")

    def count(self, text: str) -> int:
        if self._encoder is None:
            return len(text.split())
        return len(self._encoder.encode(text))

    def truncate(self, text: str, max_tokens: int) -> str:
        if self._encoder is None:
            return " ".join(text.split()[:max_tokens])
        token_ids = self._encoder.encode(text)
        return self._encoder.decode(token_ids[:max_tokens])


def normalize_whitespace(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = DOT_LEADER_PATTERN.sub(" ", text)
    text = MULTISPACE_PATTERN.sub(" ", text)
    return text.strip()


def snake_case(name: str) -> str:
    name = name.strip().lower().replace("%", "percent")
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def clean_csv(csv_path: Path) -> tuple[pd.DataFrame, dict[str, Any]]:
    raw_df = pd.read_csv(csv_path)
    df = raw_df.copy()
    df.columns = [snake_case(col) for col in df.columns]

    object_columns = df.select_dtypes(include=["object", "string"]).columns
    for col in object_columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("\u00a0", " ", regex=False)
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
        )

    if "code" in df.columns:
        df["code"] = df["code"].str.upper()
    if "party" in df.columns:
        df["party"] = df["party"].str.upper()

    if "votes" in df.columns:
        df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
    if "votes_percent" in df.columns:
        df["votes_percent"] = pd.to_numeric(
            df["votes_percent"].astype(str).str.replace("%", "", regex=False),
            errors="coerce",
        )

    before_drop = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    after_drop = len(df)

    numeric_columns = ["votes", "votes_percent"]
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    if "votes" in df.columns:
        df["votes"] = df["votes"].astype(int)

    cleaning_stats = {
        "rows_before": int(before_drop),
        "rows_after": int(after_drop),
        "duplicates_removed": int(before_drop - after_drop),
        "missing_votes_after_cleaning": int(df["votes"].isna().sum()) if "votes" in df.columns else None,
        "missing_votes_percent_after_cleaning": int(df["votes_percent"].isna().sum())
        if "votes_percent" in df.columns
        else None,
    }
    return df, cleaning_stats


def clean_pdf_pages(pdf_path: Path) -> list[dict[str, Any]]:
    reader = PdfReader(str(pdf_path))
    cleaned_pages: list[dict[str, Any]] = []

    for idx, page in enumerate(reader.pages, start=1):
        raw_text = page.extract_text() or ""
        lowered = raw_text.lower()
        lowered = HEADER_PATTERN.sub(" ", lowered)
        cleaned_text = normalize_whitespace(lowered)
        if len(cleaned_text) < 25:
            continue
        cleaned_pages.append(
            {
                "source": "pdf",
                "doc_id": f"pdf_page_{idx:03d}",
                "page": idx,
                "text": cleaned_text,
            }
        )

    return cleaned_pages


def slugify(value: str) -> str:
    slug = value.lower().replace("&", "and")
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    return slug.strip("_")


def build_csv_documents(df: pd.DataFrame) -> list[dict[str, Any]]:
    required_cols = ["year", "new_region", "candidate", "party", "votes", "votes_percent"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns after cleaning: {missing}")

    documents: list[dict[str, Any]] = []
    grouped = df.sort_values(["year", "new_region", "votes"], ascending=[True, True, False]).groupby(
        ["year", "new_region"], sort=True
    )

    for (year, region), group_df in grouped:
        lines: list[str] = []
        for row in group_df.itertuples(index=False):
            line = (
                f"in {int(row.year)}, {row.candidate} of {row.party} received {int(row.votes)} votes "
                f"which is {float(row.votes_percent):.2f} percent in {row.new_region}."
            )
            lines.append(line)

        text = " ".join(lines)
        doc_id = f"csv_{int(year)}_{slugify(str(region))}"
        documents.append(
            {
                "source": "csv",
                "doc_id": doc_id,
                "year": int(year),
                "region": str(region),
                "text": normalize_whitespace(text.lower()),
            }
        )

    return documents


def split_sentences(text: str) -> list[str]:
    # Sentence-aware boundaries retain coherence while still enabling token-window control.
    parts = re.split(r"(?<=[.!?])\s+|(?<=:)\s+|(?<=;)\s+", text)
    sentences = [part.strip() for part in parts if part and part.strip()]
    return sentences if sentences else [text.strip()]


def build_chunks_for_document(
    document: dict[str, Any], strategy: ChunkStrategy, tokenizer: Tokenizer
) -> list[dict[str, Any]]:
    sentences = split_sentences(document["text"])
    sentence_tokens = [max(1, tokenizer.count(sentence)) for sentence in sentences]

    chunks: list[dict[str, Any]] = []
    i = 0
    while i < len(sentences):
        current_sentences: list[str] = []
        current_tokens = 0
        j = i

        while j < len(sentences):
            sent = sentences[j]
            sent_tokens = sentence_tokens[j]

            if not current_sentences and sent_tokens > strategy.max_tokens:
                truncated = tokenizer.truncate(sent, strategy.max_tokens)
                current_sentences.append(truncated)
                current_tokens = tokenizer.count(truncated)
                j += 1
                break

            if current_tokens + sent_tokens > strategy.max_tokens:
                break

            current_sentences.append(sent)
            current_tokens += sent_tokens
            j += 1

        if not current_sentences:
            i += 1
            continue

        chunk_text = " ".join(current_sentences).strip()
        chunk_number = len(chunks) + 1
        chunks.append(
            {
                "chunk_id": f"{strategy.name}_{document['doc_id']}_{chunk_number:03d}",
                "strategy": strategy.name,
                "source": document["source"],
                "doc_id": document["doc_id"],
                "text": chunk_text,
                "token_count": tokenizer.count(chunk_text),
                "metadata": {k: v for k, v in document.items() if k not in {"text"}},
            }
        )

        if j >= len(sentences):
            break

        if strategy.overlap_tokens <= 0:
            i = j
            continue

        overlap_start = j
        overlap_total = 0
        while overlap_start > i and overlap_total < strategy.overlap_tokens:
            overlap_start -= 1
            overlap_total += sentence_tokens[overlap_start]

        if overlap_start <= i:
            i = i + 1
        else:
            i = overlap_start

    return chunks


def build_chunks(
    documents: Iterable[dict[str, Any]], strategy: ChunkStrategy, tokenizer: Tokenizer
) -> list[dict[str, Any]]:
    all_chunks: list[dict[str, Any]] = []
    for doc in documents:
        all_chunks.extend(build_chunks_for_document(doc, strategy, tokenizer))
    return all_chunks


def load_query_specs(queries_path: Path) -> list[dict[str, Any]]:
    return json.loads(queries_path.read_text(encoding="utf-8"))


def is_relevant(chunk: dict[str, Any], query_spec: dict[str, Any]) -> bool:
    expected_source = query_spec["expected_source"]
    if chunk["source"] != expected_source:
        return False

    text = chunk["text"].lower()
    must_all = [term.lower() for term in query_spec.get("must_contain_all", [])]
    must_any = [term.lower() for term in query_spec.get("must_contain_any", [])]

    if must_all and not all(term in text for term in must_all):
        return False
    if must_any and not any(term in text for term in must_any):
        return False
    return True


def evaluate_strategy(
    chunks: list[dict[str, Any]], query_specs: list[dict[str, Any]], top_k: int
) -> dict[str, Any]:
    if not chunks:
        raise ValueError("No chunks generated for strategy evaluation")

    texts = [chunk["text"] for chunk in chunks]
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(texts)

    per_query_results: list[dict[str, Any]] = []
    precision_values: list[float] = []
    recall_values: list[float] = []
    mrr_values: list[float] = []

    for query_spec in query_specs:
        query_text = query_spec["query"]
        query_vec = vectorizer.transform([query_text])
        similarities = cosine_similarity(query_vec, matrix).ravel()

        ranked_indices = similarities.argsort()[::-1][:top_k]
        retrieved = []
        hits = 0
        reciprocal_rank = 0.0

        total_relevant = sum(1 for chunk in chunks if is_relevant(chunk, query_spec))

        for rank, chunk_idx in enumerate(ranked_indices, start=1):
            chunk = chunks[int(chunk_idx)]
            rel = is_relevant(chunk, query_spec)
            if rel:
                hits += 1
                if reciprocal_rank == 0.0:
                    reciprocal_rank = 1.0 / rank

            retrieved.append(
                {
                    "rank": rank,
                    "chunk_id": chunk["chunk_id"],
                    "source": chunk["source"],
                    "score": float(similarities[int(chunk_idx)]),
                    "relevant": rel,
                }
            )

        precision_at_k = hits / float(top_k)
        recall_at_k = (hits / float(total_relevant)) if total_relevant > 0 else 0.0

        precision_values.append(precision_at_k)
        recall_values.append(recall_at_k)
        mrr_values.append(reciprocal_rank)

        per_query_results.append(
            {
                "query_id": query_spec["id"],
                "query": query_text,
                "expected_source": query_spec["expected_source"],
                "total_relevant_chunks": int(total_relevant),
                "precision_at_k": precision_at_k,
                "recall_at_k": recall_at_k,
                "mrr_at_k": reciprocal_rank,
                "retrieved": retrieved,
            }
        )

    summary = {
        "precision_at_k": float(statistics.mean(precision_values)) if precision_values else 0.0,
        "recall_at_k": float(statistics.mean(recall_values)) if recall_values else 0.0,
        "mrr_at_k": float(statistics.mean(mrr_values)) if mrr_values else 0.0,
        "queries_evaluated": len(query_specs),
        "top_k": top_k,
    }

    return {"summary": summary, "per_query": per_query_results}


def chunk_stats(chunks: list[dict[str, Any]]) -> dict[str, Any]:
    token_lengths = [int(chunk["token_count"]) for chunk in chunks]
    by_source: dict[str, int] = {}
    for chunk in chunks:
        by_source[chunk["source"]] = by_source.get(chunk["source"], 0) + 1

    return {
        "num_chunks": len(chunks),
        "avg_tokens": float(statistics.mean(token_lengths)) if token_lengths else 0.0,
        "median_tokens": float(statistics.median(token_lengths)) if token_lengths else 0.0,
        "min_tokens": min(token_lengths) if token_lengths else 0,
        "max_tokens": max(token_lengths) if token_lengths else 0,
        "chunks_by_source": by_source,
    }


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


def select_best_strategy(strategy_results: list[dict[str, Any]]) -> str:
    ranked = sorted(
        strategy_results,
        key=lambda item: (
            item["evaluation"]["summary"]["recall_at_k"],
            item["evaluation"]["summary"]["mrr_at_k"],
            item["evaluation"]["summary"]["precision_at_k"],
        ),
        reverse=True,
    )
    return ranked[0]["strategy"]


def build_markdown_report(
    cleaned_csv_stats: dict[str, Any],
    pdf_doc_count: int,
    csv_doc_count: int,
    strategy_results: list[dict[str, Any]],
    best_strategy: str,
    report_path: Path,
) -> None:
    lines: list[str] = []
    lines.append("# Part A: Data Engineering and Preparation")
    lines.append("")
    lines.append("## Fixed Design Choices")
    lines.append("- Number of chunking strategies: 3")
    lines.append("- Chunk unit: token-aware windows")
    lines.append("- Boundary rule: sentence-aware")
    lines.append("- Retrieval evaluation queries: 20")
    lines.append("- Relevance judgment: manual labels plus quantitative metrics")
    lines.append("- Primary comparison metric: Recall@5 (with MRR@5 and Precision@5 as secondary)")
    lines.append("")
    lines.append("## Data Cleaning Summary")
    lines.append(f"- CSV rows before deduplication: {cleaned_csv_stats['rows_before']}")
    lines.append(f"- CSV rows after deduplication: {cleaned_csv_stats['rows_after']}")
    lines.append(f"- Duplicates removed: {cleaned_csv_stats['duplicates_removed']}")
    lines.append(f"- Cleaned CSV region documents: {csv_doc_count}")
    lines.append(f"- Cleaned PDF page documents: {pdf_doc_count}")
    lines.append("")
    lines.append("## Chunking Strategies")
    lines.append("- small: 180 tokens with 30-token overlap")
    lines.append("- medium: 360 tokens with 60-token overlap")
    lines.append("- large: 600 tokens with 100-token overlap")
    lines.append("")
    lines.append("## Comparative Retrieval Results")
    lines.append("| Strategy | Chunks | Avg Tokens | Recall@5 | MRR@5 | Precision@5 |")
    lines.append("|---|---:|---:|---:|---:|---:|")

    for item in strategy_results:
        stats = item["chunk_stats"]
        summary = item["evaluation"]["summary"]
        lines.append(
            f"| {item['strategy']} | {stats['num_chunks']} | {stats['avg_tokens']:.1f} | "
            f"{summary['recall_at_k']:.4f} | {summary['mrr_at_k']:.4f} | {summary['precision_at_k']:.4f} |"
        )

    lines.append("")
    lines.append("## Recommended Strategy")
    lines.append(
        f"- Best strategy by ranking rule (Recall@5, then MRR@5, then Precision@5): {best_strategy}"
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    code_root = script_path.parents[2]

    parser = argparse.ArgumentParser(description="Run Part A data cleaning and chunking evaluation")
    parser.add_argument(
        "--raw-csv",
        type=Path,
        default=code_root / "data" / "raw" / "Ghana_Election_Result.csv",
    )
    parser.add_argument(
        "--raw-pdf",
        type=Path,
        default=code_root / "data" / "raw" / "2025-Budget-Statement-and-Economic-Policy_v4.pdf",
    )
    parser.add_argument(
        "--queries",
        type=Path,
        default=code_root / "eval" / "queries.json",
    )
    parser.add_argument("--top-k", type=int, default=5)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    tokenizer = Tokenizer()

    if not args.raw_csv.exists():
        raise FileNotFoundError(f"CSV file not found: {args.raw_csv}")
    if not args.raw_pdf.exists():
        raise FileNotFoundError(f"PDF file not found: {args.raw_pdf}")
    if not args.queries.exists():
        raise FileNotFoundError(f"Query spec file not found: {args.queries}")

    code_root = args.raw_csv.parents[2]

    interim_dir = code_root / "data" / "interim"
    processed_dir = code_root / "data" / "processed"
    eval_dir = code_root / "eval"
    logs_dir = code_root / "logs" / "experiments"
    docs_dir = code_root / "docs" / "manual_logs"

    interim_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    eval_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    cleaned_csv, cleaned_csv_stats = clean_csv(args.raw_csv)
    cleaned_csv_path = interim_dir / "ghana_election_results_cleaned.csv"
    cleaned_csv.to_csv(cleaned_csv_path, index=False)

    csv_documents = build_csv_documents(cleaned_csv)
    pdf_documents = clean_pdf_pages(args.raw_pdf)

    cleaned_pdf_pages_path = interim_dir / "budget_2025_pages_cleaned.jsonl"
    write_jsonl(cleaned_pdf_pages_path, pdf_documents)

    all_documents = csv_documents + pdf_documents
    all_documents_path = processed_dir / "documents.jsonl"
    write_jsonl(all_documents_path, all_documents)

    query_specs = load_query_specs(args.queries)

    strategy_results: list[dict[str, Any]] = []
    for strategy in STRATEGIES:
        chunks = build_chunks(all_documents, strategy=strategy, tokenizer=tokenizer)
        chunk_file = processed_dir / f"chunks_{strategy.name}.jsonl"
        write_jsonl(chunk_file, chunks)

        evaluation = evaluate_strategy(chunks, query_specs=query_specs, top_k=args.top_k)
        stats = chunk_stats(chunks)

        strategy_results.append(
            {
                "strategy": strategy.name,
                "strategy_config": {
                    "max_tokens": strategy.max_tokens,
                    "overlap_tokens": strategy.overlap_tokens,
                    "boundary_rule": strategy.boundary_rule,
                },
                "chunk_file": str(chunk_file),
                "chunk_stats": stats,
                "evaluation": evaluation,
            }
        )

    best_strategy = select_best_strategy(strategy_results)

    results_payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "part_a_design_choices": {
            "num_strategies": 3,
            "chunk_unit": "tokens",
            "boundary_rule": "sentence-aware",
            "query_count": len(query_specs),
            "relevance_method": "manual labels + metrics",
            "primary_metric": "Recall@5",
            "secondary_metrics": ["MRR@5", "Precision@5"],
        },
        "cleaning": {
            "csv_stats": cleaned_csv_stats,
            "csv_clean_output": str(cleaned_csv_path),
            "pdf_clean_pages_output": str(cleaned_pdf_pages_path),
            "csv_documents": len(csv_documents),
            "pdf_documents": len(pdf_documents),
            "combined_documents_output": str(all_documents_path),
        },
        "strategy_results": strategy_results,
        "best_strategy": best_strategy,
    }

    eval_json_path = eval_dir / "chunking_results.json"
    eval_json_path.write_text(json.dumps(results_payload, indent=2, ensure_ascii=True), encoding="utf-8")

    run_log_path = logs_dir / "run_summary.json"
    run_log_path.write_text(json.dumps(results_payload, indent=2, ensure_ascii=True), encoding="utf-8")

    report_path = docs_dir / "chunking_analysis.md"
    build_markdown_report(
        cleaned_csv_stats=cleaned_csv_stats,
        pdf_doc_count=len(pdf_documents),
        csv_doc_count=len(csv_documents),
        strategy_results=strategy_results,
        best_strategy=best_strategy,
        report_path=report_path,
    )

    print(f"Part A pipeline complete. Results: {eval_json_path}")
    print(f"Part A analysis report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
