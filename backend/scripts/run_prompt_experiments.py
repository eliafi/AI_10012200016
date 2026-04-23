#!/usr/bin/env python3
"""Part C pipeline: prompt design, context-window control, and prompt experiments."""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

try:
    import tiktoken
except ModuleNotFoundError:  # pragma: no cover
    tiktoken = None


@dataclass(frozen=True)
class PromptVariant:
    key: str
    title: str
    system_message: str
    answer_style: str


VARIANTS: list[PromptVariant] = [
    PromptVariant(
        key="v1_basic",
        title="Basic Context Injection",
        system_message=(
            "You are a helpful assistant. Answer using only the provided context."
            " If context is missing, say so clearly."
        ),
        answer_style="Write a direct answer in 2-4 sentences.",
    ),
    PromptVariant(
        key="v2_grounded",
        title="Grounded With Strict Citations",
        system_message=(
            "You are a grounded RAG assistant. Use only retrieved context."
            " Every factual claim must include a citation in square brackets with chunk_id."
            " If evidence is insufficient, output exactly: Insufficient evidence in retrieved context."
        ),
        answer_style=(
            "Answer in concise bullet points. Add citation tags like [chunk_id] at the end of each fact."
        ),
    ),
    PromptVariant(
        key="v3_structured",
        title="Structured Answer + Citation Enforcement",
        system_message=(
            "You are a strict academic assistant. Use only provided context."
            " No external facts. Cite chunk_id for all factual claims."
            " If context is not enough, output exactly: Insufficient evidence in retrieved context."
        ),
        answer_style=(
            "Return exactly three sections: Answer, Evidence, Limits."
            " In Answer and Evidence sections, include citations like [chunk_id]."
        ),
    ),
]


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


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


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


def load_env_from_file(env_path: Path) -> None:
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def citation_count(text: str) -> int:
    return len(re.findall(r"\[[A-Za-z0-9_\-]+\]", text))


def query_keywords(query_spec: dict[str, Any]) -> list[str]:
    return [term.lower() for term in query_spec.get("must_contain_all", [])]


def select_query_specs(
    retrieval_queries: list[dict[str, Any]],
    prompt_plan: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_id = {row["id"]: row for row in retrieval_queries}
    selected: list[dict[str, Any]] = []
    for row in prompt_plan:
        base = by_id.get(row["id"])
        if base is None:
            continue
        merged = dict(base)
        merged["category"] = row["category"]
        selected.append(merged)
    return selected


def build_context_block(
    retrieved_rows: list[dict[str, Any]],
    chunks_by_id: dict[str, dict[str, Any]],
    tokenizer: Tokenizer,
    max_context_tokens: int,
) -> tuple[str, list[dict[str, Any]], int]:
    selected: list[dict[str, Any]] = []
    lines: list[str] = []
    used_tokens = 0

    for row in retrieved_rows:
        chunk_id = row["chunk_id"]
        chunk = chunks_by_id.get(chunk_id)
        if chunk is None:
            continue
        header = f"[{chunk_id}] source={chunk['source']} doc={chunk['doc_id']}"
        text = chunk["text"]
        block = header + "\n" + text
        block_tokens = tokenizer.count(block)

        if used_tokens + block_tokens <= max_context_tokens:
            lines.append(block)
            selected.append(
                {
                    "chunk_id": chunk_id,
                    "rank": row["rank"],
                    "source": chunk["source"],
                    "doc_id": chunk["doc_id"],
                    "used_tokens": block_tokens,
                    "truncated": False,
                }
            )
            used_tokens += block_tokens
            continue

        remaining = max_context_tokens - used_tokens
        if remaining <= 40:
            break
        header_tokens = tokenizer.count(header + "\n")
        text_budget = max(remaining - header_tokens, 1)
        truncated_text = tokenizer.truncate(text, max_tokens=text_budget)
        truncated_block = header + "\n" + truncated_text
        truncated_tokens = tokenizer.count(truncated_block)
        while truncated_tokens > remaining and text_budget > 1:
            text_budget -= 1
            truncated_text = tokenizer.truncate(text, max_tokens=text_budget)
            truncated_block = header + "\n" + truncated_text
            truncated_tokens = tokenizer.count(truncated_block)
        lines.append(truncated_block)
        selected.append(
            {
                "chunk_id": chunk_id,
                "rank": row["rank"],
                "source": chunk["source"],
                "doc_id": chunk["doc_id"],
                "used_tokens": truncated_tokens,
                "truncated": True,
            }
        )
        used_tokens += truncated_tokens
        break

    return "\n\n".join(lines), selected, used_tokens


def build_user_prompt(query: str, context_block: str, variant: PromptVariant) -> str:
    return (
        f"User query:\n{query}\n\n"
        f"Retrieved context:\n{context_block}\n\n"
        "Rules:\n"
        "- Use only retrieved context.\n"
        "- Do not invent facts.\n"
        "- If context is insufficient, say: Insufficient evidence in retrieved context.\n"
        f"- {variant.answer_style}\n"
    )


def call_openai(
    client: OpenAI,
    model: str,
    variant: PromptVariant,
    user_prompt: str,
) -> str:
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": [{"type": "input_text", "text": variant.system_message}]},
            {"role": "user", "content": [{"type": "input_text", "text": user_prompt}]},
        ],
        temperature=0.2,
        max_output_tokens=350,
    )
    return (response.output_text or "").strip()


def evaluate_response(
    response_text: str,
    query_spec: dict[str, Any],
) -> dict[str, Any]:
    lowered = response_text.lower()
    required_terms = query_keywords(query_spec)
    keyword_hits = sum(1 for term in required_terms if term in lowered)
    keyword_coverage = (keyword_hits / len(required_terms)) if required_terms else 0.0
    citations = citation_count(response_text)
    insufficient = response_text.strip() == "Insufficient evidence in retrieved context."
    return {
        "keyword_coverage": keyword_coverage,
        "citation_count": citations,
        "has_citation": citations > 0,
        "insufficient_evidence_used": insufficient,
    }


def summarize_variant(rows: list[dict[str, Any]]) -> dict[str, Any]:
    coverage = [r["evaluation"]["keyword_coverage"] for r in rows]
    citations = [r["evaluation"]["citation_count"] for r in rows]
    citation_compliance = [1 if r["evaluation"]["has_citation"] else 0 for r in rows]
    insuff = [1 if r["evaluation"]["insufficient_evidence_used"] else 0 for r in rows]
    return {
        "queries_evaluated": len(rows),
        "avg_keyword_coverage": float(statistics.mean(coverage)) if coverage else 0.0,
        "avg_citation_count": float(statistics.mean(citations)) if citations else 0.0,
        "citation_compliance_rate": float(statistics.mean(citation_compliance)) if citation_compliance else 0.0,
        "insufficient_evidence_rate": float(statistics.mean(insuff)) if insuff else 0.0,
    }


def write_report(
    report_path: Path,
    model: str,
    max_context_tokens: int,
    variants_summary: dict[str, dict[str, Any]],
) -> None:
    lines: list[str] = []
    lines.append("# Prompt Engineering Analysis")
    lines.append("")
    lines.append("## Design Choices")
    lines.append(f"- Model: {model}")
    lines.append("- Prompt variants: 3 (basic, grounded, structured)")
    lines.append(f"- Context window budget for retrieved chunks: {max_context_tokens} tokens")
    lines.append("- Hallucination control: strict 'Insufficient evidence in retrieved context.' fallback")
    lines.append("- Citation policy: factual claims must include [chunk_id] references")
    lines.append("")
    lines.append("## Prompt Iterations")
    for variant in VARIANTS:
        lines.append(f"- {variant.key}: {variant.title}")
    lines.append("")
    lines.append("## Quantitative Comparison")
    lines.append("| Variant | Keyword Coverage | Avg Citation Count | Citation Compliance | Insufficient-Evidence Rate |")
    lines.append("|---|---:|---:|---:|---:|")
    for variant in VARIANTS:
        s = variants_summary[variant.key]
        lines.append(
            "| {} | {:.4f} | {:.4f} | {:.4f} | {:.4f} |".format(
                variant.key,
                s["avg_keyword_coverage"],
                s["avg_citation_count"],
                s["citation_compliance_rate"],
                s["insufficient_evidence_rate"],
            )
        )
    lines.append("")
    lines.append("## Evidence of Improvement")
    lines.append("- v2_grounded and v3_structured are expected to improve citation compliance over v1_basic.")
    lines.append("- v2/v3 explicitly enforce insufficient-evidence fallback to reduce hallucinated completion.")
    lines.append("- See eval/prompt_results.json for per-query responses and scoring details.")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    code_root = script_path.parents[2]

    parser = argparse.ArgumentParser(description="Run Part C prompt experiments")
    parser.add_argument("--model", type=str, default="gpt-4o-mini")
    parser.add_argument("--max-context-tokens", type=int, default=1200)
    parser.add_argument("--retrieval-results", type=Path, default=code_root / "eval" / "retrieval_results.json")
    parser.add_argument("--retrieval-queries", type=Path, default=code_root / "eval" / "retrieval_queries.json")
    parser.add_argument("--prompt-queries", type=Path, default=code_root / "eval" / "prompt_queries.json")
    parser.add_argument("--chunk-file", type=Path, default=code_root / "data" / "processed" / "chunks_large.jsonl")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_path = Path(__file__).resolve()
    code_root = script_path.parents[2]
    load_env_from_file(code_root / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is missing. Add it to code/.env.")

    retrieval_results = load_json(args.retrieval_results)
    retrieval_queries = load_json_list(args.retrieval_queries)
    prompt_query_plan = load_json_list(args.prompt_queries)
    chunks = load_jsonl(args.chunk_file)
    chunks_by_id = {row["chunk_id"]: row for row in chunks}
    selected_queries = select_query_specs(retrieval_queries=retrieval_queries, prompt_plan=prompt_query_plan)

    hybrid_rows = {row["query_id"]: row for row in retrieval_results["hybrid"]["per_query"]}
    tokenizer = Tokenizer()
    client = OpenAI(api_key=api_key)

    all_runs: dict[str, list[dict[str, Any]]] = {variant.key: [] for variant in VARIANTS}

    for query_spec in selected_queries:
        retrieved = hybrid_rows[query_spec["id"]]["retrieved"]
        context_block, context_meta, used_tokens = build_context_block(
            retrieved_rows=retrieved,
            chunks_by_id=chunks_by_id,
            tokenizer=tokenizer,
            max_context_tokens=int(args.max_context_tokens),
        )

        for variant in VARIANTS:
            user_prompt = build_user_prompt(query=query_spec["query"], context_block=context_block, variant=variant)
            response_text = call_openai(
                client=client,
                model=args.model,
                variant=variant,
                user_prompt=user_prompt,
            )
            eval_row = evaluate_response(response_text=response_text, query_spec=query_spec)
            all_runs[variant.key].append(
                {
                    "query_id": query_spec["id"],
                    "category": query_spec["category"],
                    "query": query_spec["query"],
                    "expected_source": query_spec["expected_source"],
                    "context_window": {
                        "max_context_tokens": int(args.max_context_tokens),
                        "used_context_tokens": used_tokens,
                        "selected_chunks": context_meta,
                    },
                    "prompt_variant": variant.key,
                    "response": response_text,
                    "evaluation": eval_row,
                }
            )

    summaries = {key: summarize_variant(rows) for key, rows in all_runs.items()}
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "design_choices": {
            "model": args.model,
            "context_window_management": "ranked retrieval + token-budget truncation/filtering",
            "max_context_tokens": int(args.max_context_tokens),
            "hallucination_control": "strict insufficient-evidence fallback + citation requirement",
            "queries_evaluated": len(selected_queries),
            "prompt_variants": [variant.key for variant in VARIANTS],
        },
        "variants_summary": summaries,
        "runs": all_runs,
    }

    eval_path = code_root / "eval" / "prompt_results.json"
    log_path = code_root / "logs" / "experiments" / "prompt_run_summary.json"
    report_path = code_root / "docs" / "manual_logs" / "prompt_experiments.md"
    write_json(eval_path, payload)
    write_json(log_path, payload)
    write_report(report_path=report_path, model=args.model, max_context_tokens=int(args.max_context_tokens), variants_summary=summaries)

    print(f"Prompt experiments complete. Results: {eval_path}")
    print(f"Prompt report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
