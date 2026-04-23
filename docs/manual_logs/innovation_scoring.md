# Innovation Component: Domain-Specific Scoring

## Feature
- Introduced a domain-specific scoring function to improve retrieval on numeric/table and source-specific queries.
- Final score = 0.50*semantic + 0.25*keyword + 0.25*domain features.
- Domain features blend source-match bonus, numeric-focus bonus, and domain-term bonus.

## Comparison
| Method | Recall@5 | MRR@5 | Precision@5 | Top1 Accuracy |
|---|---:|---:|---:|---:|
| Vector | 0.5104 | 0.4396 | 0.1125 | 0.3750 |
| Hybrid | 0.7708 | 0.6635 | 0.2125 | 0.5625 |
| Hybrid + Domain | 0.7500 | 0.7135 | 0.2000 | 0.6250 |

## Evidence
- Detailed per-query outputs are saved in eval/innovation_scoring_results.json.
- This innovation targets domain-specific weaknesses from adversarial numeric and abbreviation queries.
