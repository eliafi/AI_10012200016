# Retrieval System Analysis

## Design Choices
- Embedding pipeline: local sentence-transformers
- Embedding model: sentence-transformers/all-MiniLM-L6-v2
- Vector storage: FAISS (IndexFlatIP)
- Similarity metric: cosine similarity
- Retrieval extension: hybrid search (vector + keyword)
- Default top-k: 5

## Corpus
- Chunk file: C:\Users\nbens\Desktop\AI_exam\code\data\processed\chunks_large.jsonl
- Number of chunks indexed: 796

## Baseline Vs Hybrid
| Method | Recall@5 | MRR@5 | Precision@5 | Top1 Accuracy |
|---|---:|---:|---:|---:|
| Vector only | 0.5104 | 0.4396 | 0.1125 | 0.3750 |
| Hybrid | 0.7708 | 0.6635 | 0.2125 | 0.5625 |

## Failure Case Summary
- Failure queries evaluated: 6
- Baseline failures: 5
- Cases improved by hybrid: 2

## Failure Case Examples (Before Vs After)
- Query r11 (NHF outstanding IPC invoice end-Dec 2024):
	Baseline failed to retrieve any relevant chunk in top-5 (Recall@5 = 0.0, MRR@5 = 0.0).
	Hybrid retrieved the first relevant chunk at rank 5 (large_pdf_page_026_001), improving to Recall@5 = 1.0 and MRR@5 = 0.2.
- Query r13 (Appendix 7B NTR/IGF 2024 actuals and 2025 projections):
	Baseline returned no relevant chunk in top-5 (Recall@5 = 0.0, MRR@5 = 0.0).
	Hybrid retrieved a relevant chunk at rank 4 (large_pdf_page_205_001), improving to Recall@5 = 0.3333 and MRR@5 = 0.25.

## Proposed Fix
- Baseline issue: dense-vector-only retrieval misses keyword-heavy and table-like queries.
- Implemented fix: hybrid scoring = alpha * vector_score + (1 - alpha) * keyword_score.
- Alpha used: 0.55
