#!/usr/bin/env python3
"""Part E evaluation: adversarial testing and RAG vs pure LLM comparison."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

SCRIPT_PATH = Path(__file__).resolve()
CODE_ROOT = SCRIPT_PATH.parents[2]
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from backend.scripts.run_full_pipeline import load_env_from_file, run_pipeline


def load_json_list(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def select_adversarial_queries(all_queries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [q for q in all_queries if bool(q.get("failure_case", False))]


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def citation_count(text: str) -> int:
    return len(re.findall(r"\[[A-Za-z0-9_\-]+\]", text))


def keyword_coverage(response_text: str, must_contain_all: list[str]) -> float:
    if not must_contain_all:
        return 0.0
    lowered = response_text.lower()
    hits = sum(1 for t in must_contain_all if t.lower() in lowered)
    return hits / float(len(must_contain_all))


def auto_accuracy_label(coverage: float) -> str:
    if coverage >= 0.75:
        return "correct"
    if coverage >= 0.40:
        return "partial"
    return "incorrect"


def hallucination_flag(response_text: str, coverage: float, mode: str) -> tuple[bool, dict[str, bool]]:
    insufficient = response_text.strip() == "Insufficient evidence in retrieved context."
    has_citation = citation_count(response_text) > 0
    unsupported_claim_risk = (coverage < 0.50) and (not insufficient)
    citation_missing_risk = (mode == "rag") and (not has_citation) and (not insufficient)
    flagged = unsupported_claim_risk or citation_missing_risk
    return flagged, {
        "insufficient_evidence_used": insufficient,
        "has_citation": has_citation,
        "unsupported_claim_risk": unsupported_claim_risk,
        "citation_missing_risk": citation_missing_risk,
    }


def call_pure_llm(client: OpenAI, model: str, query: str) -> str:
    system_prompt = (
        "You are a concise assistant. Answer the user query directly."
        " If unsure, state uncertainty clearly."
    )
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": [{"type": "input_text", "text": system_prompt}]},
            {"role": "user", "content": [{"type": "input_text", "text": query}]},
        ],
        temperature=0.2,
        max_output_tokens=300,
    )
    return (response.output_text or "").strip()


def average_pairwise_jaccard(texts: list[str]) -> float:
    if len(texts) <= 1:
        return 1.0
    scores: list[float] = []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a = tokenize(texts[i])
            b = tokenize(texts[j])
            if not a and not b:
                scores.append(1.0)
            elif not a or not b:
                scores.append(0.0)
            else:
                scores.append(len(a & b) / float(len(a | b)))
    return float(statistics.mean(scores)) if scores else 1.0


def summarize_mode(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {}
    labels = [r["accuracy"]["label"] for r in rows]
    hallucinations = [1 if r["hallucination"]["flagged"] else 0 for r in rows]
    coverage = [r["accuracy"]["keyword_coverage"] for r in rows]
    return {
        "responses_evaluated": len(rows),
        "accuracy_rate_correct": labels.count("correct") / float(len(rows)),
        "accuracy_rate_partial": labels.count("partial") / float(len(rows)),
        "accuracy_rate_incorrect": labels.count("incorrect") / float(len(rows)),
        "avg_keyword_coverage": float(statistics.mean(coverage)) if coverage else 0.0,
        "hallucination_rate": float(statistics.mean(hallucinations)) if hallucinations else 0.0,
    }


def summarize_consistency(mode_rows: list[dict[str, Any]], runs_per_query: int) -> dict[str, Any]:
    by_query: dict[str, list[str]] = {}
    for row in mode_rows:
        by_query.setdefault(row["query_id"], []).append(row["response"])

    per_query: list[dict[str, Any]] = []
    scores: list[float] = []
    for query_id, responses in by_query.items():
        score = average_pairwise_jaccard(responses)
        scores.append(score)
        per_query.append(
            {
                "query_id": query_id,
                "runs_observed": len(responses),
                "runs_expected": runs_per_query,
                "consistency_score_jaccard": score,
            }
        )
    return {
        "avg_consistency_score_jaccard": float(statistics.mean(scores)) if scores else 0.0,
        "per_query": per_query,
    }


def write_markdown_report(path: Path, payload: dict[str, Any]) -> None:
    rag = payload["summary"]["rag"]
    pure = payload["summary"]["pure_llm"]
    rag_cons = payload["consistency"]["rag"]["avg_consistency_score_jaccard"]
    pure_cons = payload["consistency"]["pure_llm"]["avg_consistency_score_jaccard"]

    lines: list[str] = []
    lines.append("# Critical Evaluation and Adversarial Testing")
    lines.append("")
    lines.append("## Setup")
    lines.append("- Adversarial queries evaluated: {}".format(payload["design_choices"]["adversarial_queries"]))
    lines.append("- Modes compared: RAG pipeline vs pure LLM (no retrieval)")
    lines.append("- Runs per query per mode: {}".format(payload["design_choices"]["runs_per_query"]))
    lines.append("- Model for both modes: {}".format(payload["design_choices"]["llm_model"]))
    lines.append("")
    lines.append("## Metrics")
    lines.append("- Accuracy: keyword-coverage based label (correct/partial/incorrect)")
    lines.append("- Hallucination rate: unsupported-claim risk; for RAG also missing citation risk")
    lines.append("- Response consistency: average pairwise Jaccard similarity over repeated runs")
    lines.append("")
    lines.append("## RAG vs Pure LLM")
    lines.append("| Mode | Correct | Partial | Incorrect | Avg Keyword Coverage | Hallucination Rate | Consistency |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    lines.append(
        "| RAG | {:.4f} | {:.4f} | {:.4f} | {:.4f} | {:.4f} | {:.4f} |".format(
            rag["accuracy_rate_correct"],
            rag["accuracy_rate_partial"],
            rag["accuracy_rate_incorrect"],
            rag["avg_keyword_coverage"],
            rag["hallucination_rate"],
            rag_cons,
        )
    )
    lines.append(
        "| Pure LLM | {:.4f} | {:.4f} | {:.4f} | {:.4f} | {:.4f} | {:.4f} |".format(
            pure["accuracy_rate_correct"],
            pure["accuracy_rate_partial"],
            pure["accuracy_rate_incorrect"],
            pure["avg_keyword_coverage"],
            pure["hallucination_rate"],
            pure_cons,
        )
    )
    lines.append("")
    lines.append("## Evidence-Based Conclusion")
    lines.append("- Comparison is based on generated outputs recorded in eval/adversarial_evaluation_results.json.")
    lines.append("- Query-level and run-level outputs for both modes are stored for audit and reproducibility.")
    lines.append("- Use docs/manual_logs/adversarial_manual_rubric_template.md to add manual correctness labels.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manual_template(path: Path, rows: list[dict[str, Any]]) -> None:
    lines: list[str] = []
    lines.append("# Manual Rubric Template (Adversarial Evaluation)")
    lines.append("")
    lines.append("Use this template to add human judgement on sampled outputs.")
    lines.append("")
    lines.append("| query_id | mode | run | auto_label | manual_label(correct/partial/incorrect) | notes |")
    lines.append("|---|---|---:|---|---|---|")
    for row in rows[:24]:
        lines.append(
            "| {} | {} | {} | {} |  |  |".format(
                row["query_id"],
                row["mode"],
                row["run_index"],
                row["accuracy"]["label"],
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    code_root = script_path.parents[2]
    parser = argparse.ArgumentParser(description="Run adversarial evaluation (RAG vs pure LLM)")
    parser.add_argument("--queries", type=Path, default=code_root / "eval" / "retrieval_queries.json")
    parser.add_argument("--runs-per-query", type=int, default=3)
    parser.add_argument("--llm-model", type=str, default="gpt-4o-mini")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--hybrid-alpha", type=float, default=0.55)
    parser.add_argument("--max-context-tokens", type=int, default=1200)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_path = Path(__file__).resolve()
    code_root = script_path.parents[2]
    load_env_from_file(code_root / ".env")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is missing in code/.env")

    all_queries = load_json_list(args.queries)
    adversarial_queries = select_adversarial_queries(all_queries)
    client = OpenAI(api_key=api_key)

    rows: list[dict[str, Any]] = []
    for query_spec in adversarial_queries:
        for run_index in range(1, int(args.runs_per_query) + 1):
            rag_payload, rag_log_path = run_pipeline(
                query=query_spec["query"],
                top_k=int(args.top_k),
                hybrid_alpha=float(args.hybrid_alpha),
                llm_model=args.llm_model,
                max_context_tokens=int(args.max_context_tokens),
                code_root=code_root,
            )
            rag_text = rag_payload["pipeline"]["response"]
            rag_cov = keyword_coverage(rag_text, query_spec.get("must_contain_all", []))
            rag_label = auto_accuracy_label(rag_cov)
            rag_hall, rag_diag = hallucination_flag(rag_text, rag_cov, mode="rag")
            rows.append(
                {
                    "query_id": query_spec["id"],
                    "query": query_spec["query"],
                    "mode": "rag",
                    "run_index": run_index,
                    "response": rag_text,
                    "log_path": str(rag_log_path),
                    "accuracy": {"keyword_coverage": rag_cov, "label": rag_label},
                    "hallucination": {"flagged": rag_hall, "details": rag_diag},
                }
            )

            pure_text = call_pure_llm(client=client, model=args.llm_model, query=query_spec["query"])
            pure_cov = keyword_coverage(pure_text, query_spec.get("must_contain_all", []))
            pure_label = auto_accuracy_label(pure_cov)
            pure_hall, pure_diag = hallucination_flag(pure_text, pure_cov, mode="pure_llm")
            rows.append(
                {
                    "query_id": query_spec["id"],
                    "query": query_spec["query"],
                    "mode": "pure_llm",
                    "run_index": run_index,
                    "response": pure_text,
                    "log_path": "",
                    "accuracy": {"keyword_coverage": pure_cov, "label": pure_label},
                    "hallucination": {"flagged": pure_hall, "details": pure_diag},
                }
            )

    rag_rows = [r for r in rows if r["mode"] == "rag"]
    pure_rows = [r for r in rows if r["mode"] == "pure_llm"]

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "design_choices": {
            "adversarial_queries": len(adversarial_queries),
            "query_ids": [q["id"] for q in adversarial_queries],
            "runs_per_query": int(args.runs_per_query),
            "llm_model": args.llm_model,
            "rag_retrieval_top_k": int(args.top_k),
            "rag_hybrid_alpha": float(args.hybrid_alpha),
            "rag_max_context_tokens": int(args.max_context_tokens),
        },
        "summary": {
            "rag": summarize_mode(rag_rows),
            "pure_llm": summarize_mode(pure_rows),
        },
        "consistency": {
            "rag": summarize_consistency(rag_rows, int(args.runs_per_query)),
            "pure_llm": summarize_consistency(pure_rows, int(args.runs_per_query)),
        },
        "runs": rows,
    }

    eval_path = code_root / "eval" / "adversarial_evaluation_results.json"
    log_path = code_root / "logs" / "experiments" / "adversarial_evaluation_run_summary.json"
    report_path = code_root / "docs" / "manual_logs" / "adversarial_evaluation.md"
    manual_template_path = code_root / "docs" / "manual_logs" / "adversarial_manual_rubric_template.md"

    write_json(eval_path, payload)
    write_json(log_path, payload)
    write_markdown_report(report_path, payload)
    write_manual_template(manual_template_path, rows)

    print(f"Adversarial evaluation complete. Results: {eval_path}")
    print(f"Adversarial report: {report_path}")
    print(f"Manual rubric template: {manual_template_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
