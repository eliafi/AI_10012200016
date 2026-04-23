# Critical Evaluation and Adversarial Testing

## Setup
- Adversarial queries evaluated: 6
- Modes compared: RAG pipeline vs pure LLM (no retrieval)
- Runs per query per mode: 3
- Model for both modes: gpt-4o-mini

## Metrics
- Accuracy: keyword-coverage based label (correct/partial/incorrect)
- Hallucination rate: unsupported-claim risk; for RAG also missing citation risk
- Response consistency: average pairwise Jaccard similarity over repeated runs

## RAG vs Pure LLM
| Mode | Correct | Partial | Incorrect | Avg Keyword Coverage | Hallucination Rate | Consistency |
|---|---:|---:|---:|---:|---:|---:|
| RAG | 0.3333 | 0.0556 | 0.6111 | 0.3565 | 0.2778 | 0.6395 |
| Pure LLM | 0.0000 | 0.5000 | 0.5000 | 0.3194 | 0.5000 | 0.6633 |

## Evidence-Based Conclusion
- Comparison is based on generated outputs recorded in eval/adversarial_evaluation_results.json.
- Query-level and run-level outputs for both modes are stored for audit and reproducibility.
- Use docs/manual_logs/adversarial_manual_rubric_template.md to add manual correctness labels.
