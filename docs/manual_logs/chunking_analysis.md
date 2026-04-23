# Part A: Data Engineering and Preparation

## Fixed Design Choices
- Number of chunking strategies: 3
- Chunk unit: token-aware windows
- Boundary rule: sentence-aware
- Retrieval evaluation queries: 20
- Relevance judgment: manual labels plus quantitative metrics
- Primary comparison metric: Recall@5 (with MRR@5 and Precision@5 as secondary)

## Data Cleaning Summary
- CSV rows before deduplication: 615
- CSV rows after deduplication: 615
- Duplicates removed: 0
- Cleaned CSV region documents: 98
- Cleaned PDF page documents: 251

## Chunking Strategies
- small: 180 tokens with 30-token overlap
- medium: 360 tokens with 60-token overlap
- large: 600 tokens with 100-token overlap

## Comparative Retrieval Results
| Strategy | Chunks | Avg Tokens | Recall@5 | MRR@5 | Precision@5 |
|---|---:|---:|---:|---:|---:|
| small | 1363 | 127.8 | 0.7792 | 0.5767 | 0.2100 |
| medium | 972 | 217.0 | 0.8738 | 0.7167 | 0.2400 |
| large | 796 | 307.4 | 0.9333 | 0.6333 | 0.2100 |

## Recommended Strategy
- Best strategy by ranking rule (Recall@5, then MRR@5, then Precision@5): large

The large strategy (600-token chunks with 100-token overlap) is preferred because it gives the highest Recall@5 on this mixed corpus and preserves more complete context for table-like budget content and multi-value election records in a single chunk. The 100-token overlap reduces boundary loss for facts that span sentence edges, while still keeping the total number of chunks lower than smaller strategies, which simplifies downstream indexing and retrieval coverage.
