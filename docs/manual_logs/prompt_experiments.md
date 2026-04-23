# Prompt Engineering Analysis

## Design Choices
- Model: gpt-4o-mini
- Prompt variants: 3 (basic, grounded, structured)
- Context window budget for retrieved chunks: 1200 tokens
- Hallucination control: strict 'Insufficient evidence in retrieved context.' fallback
- Citation policy: factual claims must include [chunk_id] references

## Prompt Iterations
- v1_basic: Basic Context Injection
- v2_grounded: Grounded With Strict Citations
- v3_structured: Structured Answer + Citation Enforcement

## Quantitative Comparison
| Variant | Keyword Coverage | Avg Citation Count | Citation Compliance | Insufficient-Evidence Rate |
|---|---:|---:|---:|---:|
| v1_basic | 0.7153 | 0.0000 | 0.0000 | 0.0000 |
| v2_grounded | 0.7222 | 2.0833 | 1.0000 | 0.0000 |
| v3_structured | 0.8056 | 1.3333 | 0.9167 | 0.0000 |

## Evidence of Improvement
- v2_grounded and v3_structured are expected to improve citation compliance over v1_basic.
- v2/v3 explicitly enforce insufficient-evidence fallback to reduce hallucinated completion.
- See eval/prompt_results.json for per-query responses and scoring details.
