@AGENTS.md


I'll explore the frontend directory now.

Agent:Explore frontend directory
IN
Thoroughly explore the frontend directory at c:\Users\ayekp\OneDrive\Desktop\AI_10012200016. I need a comprehensive understanding of: the overall structure and tech stack, all major files and their purposes, any configuration files, any existing components or pages, styling approach, how routing works if applicable, and any notable patterns or issues. Report everything you find — structure, stack, file-by-file summary, and any observations about completeness or gaps.
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016 -type f -name "*.json" -o -type f -name "*.js" -o -type f -name "*.jsx" -o -type f -name "*.tsx" -o -type f -name "*.ts" -o -type f -name "*.html" -o -type f -name "*.css" -o -type f -name "*.scss" | head -100

OUT
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app/insomnia_collection.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/adversarial_evaluation_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/chunking_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/innovation_scoring_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/prompt_queries.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/prompt_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/queries.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/retrieval_queries.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/retrieval_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/indexes/metadata/chunk_lookup.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/adversarial_evaluation_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/innovation_scoring_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/prompt_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/retrieval_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T173503Z_5b20fe35.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T174924Z_21ebae88.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T174953Z_104f386a.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T175038Z_d9c5e64d.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T180213Z_9e7f1fe7.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T180301Z_9b2e91c7.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T180752Z_3fd746e1.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T181029Z_df04c5e9.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T181056Z_4db73809.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185355Z_817cf3cc.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185407Z_8b566bf3.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185417Z_fc16ced2.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185425Z_25397cd6.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185436Z_37db53b5.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185446Z_1ffb2f33.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185457Z_f79c62d5.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185506Z_79107775.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185519Z_acfb7787.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185529Z_79494346.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185537Z_c7e10ed9.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185546Z_6e420677.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185557Z_86f172f3.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185608Z_ea71e480.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185619Z_2bfffbdd.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185628Z_990ce41b.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185639Z_fcdbc213.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185650Z_bda89c79.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T192516Z_87a465f6.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T192630Z_22118537.json
Bash
IN
ls -la /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/ | head -30

OUT
total 49
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:53 .
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:48 ..
drwxr-xr-x 1 ayekp 197609   0 Apr 24 15:04 .git
-rw-r--r-- 1 ayekp 197609 480 Apr 24 14:53 .gitignore
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:54 backend
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:54 data
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:54 docs
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:54 eval
drwxr-xr-x 1 ayekp 197609   0 Apr 24 15:04 frontend
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:54 indexes
drwxr-xr-x 1 ayekp 197609   0 Apr 24 14:54 logs
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend -type f -name "*" | head -150

OUT
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/logo.png
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/Navbar_icon.png
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/ui_design_blueprint.md
Bash
IN
ls -laR /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend

OUT
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend:
total 4396
drwxr-xr-x 1 ayekp 197609       0 Apr 24 15:04 .
drwxr-xr-x 1 ayekp 197609       0 Apr 24 14:53 ..
-rw-r--r-- 1 ayekp 197609 2197929 Apr 24 15:04 Navbar_icon.png
-rw-r--r-- 1 ayekp 197609 2269881 Apr 24 15:04 logo.png
-rw-r--r-- 1 ayekp 197609   18842 Apr 24 14:53 ui_design_blueprint.md
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016 -type d | head -50

OUT
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/hooks
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/info
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/logs
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/logs/refs
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/logs/refs/heads
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/logs/refs/remotes
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/logs/refs/remotes/origin
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/16
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/18
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/25
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/58
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/79
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/8a
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/90
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/9e
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/dc
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/df
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/info
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/objects/pack
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/refs
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/refs/heads
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/refs/remotes
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/refs/remotes/origin
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.git/refs/tags
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/data
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/data/interim
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/data/processed
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/data/raw
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/manual_logs
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/indexes
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/indexes/faiss
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/indexes/metadata
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016 -maxdepth 2 -type f \( -name "package.json" -o -name "package-lock.json" -o -name "tsconfig.json" -o -name "vite.config.*" -o -name "webpack.config.*" -o -name ".env*" -o -name "README*" -o -name "*.config.js" \)

OUT
(Bash completed with no output)
Bash
IN
ls -la /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/ | grep -v "^d"

OUT
total 49
-rw-r--r-- 1 ayekp 197609 480 Apr 24 14:53 .gitignore
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend -type f -name "*.py" | head -20

OUT
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app/main.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app/__init__.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_adversarial_evaluation.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_data_preparation.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_full_pipeline.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_innovation_scoring.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_prompt_experiments.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_retrieval_system.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/__init__.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/__init__.py
Read main.py
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend -type f | xargs ls -lh

OUT
-rw-r--r-- 1 ayekp 197609 2.1M Apr 24 15:04 /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/Navbar_icon.png
-rw-r--r-- 1 ayekp 197609 2.2M Apr 24 15:04 /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/logo.png
-rw-r--r-- 1 ayekp 197609  19K Apr 24 14:53 /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/ui_design_blueprint.md
Bash
IN
git log --oneline --name-status | head -50

OUT
1651d59 feat: add navigation and brand logo assets to frontend directory
A	frontend/Navbar_icon.png
A	frontend/logo.png
2753a0e docs: add UI design blueprint for frontend interface
A	frontend/ui_design_blueprint.md
a906057 Initial RAG exam submission backend and evaluation artifacts
A	.gitignore
A	backend/__init__.py
A	backend/app/__init__.py
A	backend/app/insomnia_collection.json
A	backend/app/main.py
A	backend/scripts/__init__.py
A	backend/scripts/run_adversarial_evaluation.py
A	backend/scripts/run_data_preparation.py
A	backend/scripts/run_full_pipeline.py
A	backend/scripts/run_innovation_scoring.py
A	backend/scripts/run_prompt_experiments.py
A	backend/scripts/run_retrieval_system.py
A	data/interim/budget_2025_pages_cleaned.jsonl
A	data/interim/ghana_election_results_cleaned.csv
A	data/processed/chunks_large.jsonl
A	data/processed/chunks_medium.jsonl
A	data/processed/chunks_small.jsonl
A	data/processed/documents.jsonl
A	data/raw/2025-Budget-Statement-and-Economic-Policy_v4.pdf
A	data/raw/Ghana_Election_Result.csv
A	docs/manual_logs/adversarial_evaluation.md
A	docs/manual_logs/adversarial_manual_rubric_template.md
A	docs/manual_logs/chunking_analysis.md
A	docs/manual_logs/innovation_scoring.md
A	docs/manual_logs/prompt_experiments.md
A	docs/manual_logs/retrieval_analysis.md
A	eval/adversarial_evaluation_results.json
A	eval/chunking_results.json
A	eval/innovation_scoring_results.json
A	eval/prompt_queries.json
A	eval/prompt_results.json
A	eval/queries.json
A	eval/retrieval_queries.json
A	eval/retrieval_results.json
A	indexes/faiss/chunk_embeddings.npy
A	indexes/faiss/retrieval.index
A	indexes/metadata/chunk_lookup.json
A	logs/experiments/adversarial_evaluation_run_summary.json
A	logs/experiments/innovation_scoring_run_summary.json
A	logs/experiments/prompt_run_summary.json
A	logs/experiments/retrieval_run_summary.json
A	logs/experiments/run_summary.json
A	logs/runs/rag_run_20260423T173503Z_5b20fe35.json
A	logs/runs/rag_run_20260423T174924Z_21ebae88.json
Globpattern: "**/package.json"
No files found
Read .gitignore
Bash
IN
ls -la /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app/

OUT
total 17
drwxr-xr-x 1 ayekp 197609    0 Apr 24 14:54 .
drwxr-xr-x 1 ayekp 197609    0 Apr 24 14:54 ..
-rw-r--r-- 1 ayekp 197609   28 Apr 24 14:53 __init__.py
-rw-r--r-- 1 ayekp 197609 7597 Apr 24 14:53 insomnia_collection.json
-rw-r--r-- 1 ayekp 197609 1673 Apr 24 14:53 main.py
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016 -maxdepth 1 -type f

OUT
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.gitignore
Bash
IN
ls -la /c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/

OUT
total 8
drwxr-xr-x 1 ayekp 197609 0 Apr 24 14:54 .
drwxr-xr-x 1 ayekp 197609 0 Apr 24 15:07 ..
drwxr-xr-x 1 ayekp 197609 0 Apr 24 14:54 manual_logs
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016 -type f | grep -E "\.(js|jsx|tsx|ts|html|css|scss|json|md|py)$" | wc -l

OUT
62
Bash
IN
find /c/Users/ayekp/OneDrive/Desktop/AI_10012200016 -type f | grep -E "\.(js|jsx|tsx|ts|html|css|scss|json|md|py)$" | sort | head -70

OUT
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/.claude/settings.local.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/__init__.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app/__init__.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app/insomnia_collection.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/app/main.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/__init__.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_adversarial_evaluation.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_data_preparation.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_full_pipeline.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_innovation_scoring.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_prompt_experiments.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/backend/scripts/run_retrieval_system.py
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/manual_logs/adversarial_evaluation.md
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/manual_logs/adversarial_manual_rubric_template.md
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/manual_logs/chunking_analysis.md
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/manual_logs/innovation_scoring.md
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/manual_logs/prompt_experiments.md
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/docs/manual_logs/retrieval_analysis.md
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/adversarial_evaluation_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/chunking_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/innovation_scoring_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/prompt_queries.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/prompt_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/queries.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/retrieval_queries.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/eval/retrieval_results.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/ui_design_blueprint.md
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/indexes/metadata/chunk_lookup.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/adversarial_evaluation_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/innovation_scoring_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/prompt_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/retrieval_run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/experiments/run_summary.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T173503Z_5b20fe35.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T174924Z_21ebae88.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T174953Z_104f386a.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T175038Z_d9c5e64d.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T180213Z_9e7f1fe7.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T180301Z_9b2e91c7.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T180752Z_3fd746e1.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T181029Z_df04c5e9.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T181056Z_4db73809.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185355Z_817cf3cc.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185407Z_8b566bf3.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185417Z_fc16ced2.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185425Z_25397cd6.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185436Z_37db53b5.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185446Z_1ffb2f33.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185457Z_f79c62d5.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185506Z_79107775.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185519Z_acfb7787.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185529Z_79494346.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185537Z_c7e10ed9.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185546Z_6e420677.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185557Z_86f172f3.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185608Z_ea71e480.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185619Z_2bfffbdd.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185628Z_990ce41b.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185639Z_fcdbc213.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T185650Z_bda89c79.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T192516Z_87a465f6.json
/c/Users/ayekp/OneDrive/Desktop/AI_10012200016/logs/runs/rag_run_20260423T192630Z_22118537.json
Here's what I found:

Frontend Directory — Current State
The frontend is design-only. No code has been written yet.

What exists
File	Description
frontend/ui_design_blueprint.md	18.8 KB comprehensive design spec
frontend/logo.png	Brand logo (2.2 MB)
frontend/Navbar_icon.png	Nav icon (2.1 MB)
Design Spec Summary
Theme: "Ghana Civic Premium" — dark mode using Ghana national colors (gold #FCD116, red #CE1126, green #006B3F)
Layout: Desktop = 55% chat / 45% RAG inspection panel split; mobile = single column with expandable accordions
Stack Recommended: Vanilla HTML/CSS/JS (no build step) with CDN libs — marked.js, highlight.js, Lucide Icons
Style: Glassmorphism cards, Black Star watermark, gold gradient user bubbles
Backend API (already implemented)
The backend at backend/app/main.py has a POST /query endpoint ready to consume:


query, top_k, hybrid_alpha, llm_model, max_context_tokens → response + retrieved_docs + pipeline_times
What's missing (nothing built yet)
index.html, styles.css, app.js
API integration code
Any component implementation
Build tooling / dev server
What would you like to do next — should I start building the frontend based on the design blueprint?

it will be a next.js if the design spec says html css update it and it should be very responsive, also if there isnt mobile responsive indicate that it should be
Let me read the full design blueprint first.

Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend\ui_design_blueprint.md
Now I have the full picture. I'll update the blueprint — swapping in Next.js, adding Tailwind CSS for responsiveness, strengthening mobile requirements throughout, and updating the component architecture and implementation phases.

Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend\ui_design_blueprint.md
602 lines
# Academic City RAG Chatbot — UI Design Blueprint

## 1. Exam Requirements Analysis

From the exam paper (CS4241), the UI **must** support these features:

| Feature | Exam Reference | Priority |
|:---|:---|:---|
| **Query input** | Part D, Final Deliverables | Critical |
| **Display retrieved chunks** | Part D, Final Deliverables | Critical |
| **Show similarity scores** | Part D | Critical |
| **Show final response** | Part D, Final Deliverables | Critical |
| **Display final prompt sent to LLM** | Part D | High |
| **Pipeline stage logging** | Part D | High |
| **Adversarial query testing** | Part E | Nice |
| **RAG vs Pure LLM comparison** | Part E | Nice |

### Backend API Response Shape (from `main.py`)
```json
{
  "run_id": "...",
  "query": "...",
  "retrieved_documents": [...],
  "context_selection": {...},
  "final_prompt_sent_to_llm": "...",
  "response": "...",
  "stage_times": {...},
  "run_log_path": "..."
}
```

---

## 2. Design Philosophy

### Theme: **"Ghana Civic Premium" — Black Star Dark Mode**

A premium dark interface rooted in **Ghanaian national identity**. The near-black background represents the **Black Star** — Ghana's symbol of freedom and African emancipation. Accent colors are desaturated, dark-mode-friendly renditions of the **Ghana national flag** (Red, Gold, Green). Surface elements use **"Transparent Ballot Box Glass"** — a glassmorphism metaphor inspired by Ghana's Electoral Commission, conveying transparency and civic trust.

### Core Principles
- **Civic authority**: The UI should feel like an official government/university portal
- **Focus-oriented**: Chat is the hero — everything else is secondary
- **Progressive disclosure**: Chunks, scores, and pipeline logs revealed on demand
- **Micro-animations**: Subtle feedback for every interaction
- **Mobile-first, fully responsive**: Designed for phone screens first — every feature must work perfectly on mobile. Desktop is an enhancement, not the baseline.

### UI Motifs
- **Black Star Motif**: A large, subtle, low-opacity (`0.03–0.05`) five-pointed star watermark on the page background or app header, evoking the Black Star of Africa
- **Transparent Ballot Box Glass**: All glassmorphism cards use frosted transparency as a metaphor for electoral/civic transparency — clear governance through clear data

---

## 3. Color Palette

### Black Star Backgrounds

| Token | Hex | Usage |
|:---|:---|:---|
| `--bg-deep` | `#0B0F1A` | Page background — "Black Star" near-black |
| `--bg-surface` | `#111827` | Card/panel backgrounds |
| `--bg-elevated` | `#1E293B` | Elevated surfaces, hover states |
| `--bg-glass` | `rgba(30, 41, 59, 0.55)` | Transparent Ballot Box Glass panels |
| `--border-subtle` | `rgba(148, 163, 184, 0.12)` | Subtle borders |
| `--border-glass` | `rgba(252, 209, 22, 0.08)` | Gold-tinted glass card borders |

### Ghana National Accents

| Token | Hex | Origin | Usage |
|:---|:---|:---|:---|
| `--ghana-gold` | `#FCD116` | Flag Gold | **Primary accent** — buttons, focus rings, hero gradient, active states |
| `--ghana-gold-muted` | `#D4A017` | Desaturated gold | Hover states, secondary gold uses |
| `--ghana-red` | `#CE1126` | Flag Red | Critical highlights, low similarity scores, errors, warnings |
| `--ghana-red-muted` | `#A30E1F` | Desaturated red | Hover/pressed states for destructive actions |
| `--ghana-green` | `#006B3F` | Flag Green | Success states, high similarity scores, positive feedback |
| `--ghana-green-bright` | `#00895A` | Brightened green | Text-on-dark legibility variant |
| `--accent-star` | `#F1F5F9` | Black Star (inverted) | Star watermark, premium icon highlights |

### Text Colors

| Token | Hex | Usage |
|:---|:---|:---|
| `--text-primary` | `#F1F5F9` | Primary text (off-white) |
| `--text-secondary` | `#94A3B8` | Secondary text, labels |
| `--text-muted` | `#64748B` | Muted text, timestamps |
| `--text-gold` | `#FCD116` | Links, interactive text, active nav items |

### Gradient Accents

```css
/* Hero gradient — Ghana tricolour sweep for header/branding areas */
--gradient-brand: linear-gradient(135deg, #CE1126 0%, #FCD116 50%, #006B3F 100%);

/* Subtle background glow — warm gold radiance from top */
--gradient-glow: radial-gradient(ellipse at top, rgba(252, 209, 22, 0.10), transparent 60%);

/* RAG similarity score bar — maps Red→Gold→Green (bad→ok→good) */
--gradient-score: linear-gradient(90deg, #CE1126, #FCD116, #006B3F);

/* Gold shimmer for premium elements */
--gradient-gold-shimmer: linear-gradient(90deg, #D4A017, #FCD116, #D4A017);
```

---

## 4. Typography

| Element | Font | Weight | Size (Desktop) | Size (Mobile) | Notes |
|:---|:---|:---|:---|:---|:---|
| App title | **Inter** | 800 | 24px | 18px | `letter-spacing: 0.08em; text-transform: uppercase;` |
| Section headers | **Inter** | 700 | 18px | 15px | |
| Body text | **Inter** | 400 | 15px | 14px | |
| Chat messages | **Inter** | 400 | 15px | 14px | |
| Code/prompt | **JetBrains Mono** | 400 | 13px | 12px | |
| Badges/labels | **Inter** | 600 | 11px | 10px | |
| Timestamps | **Inter** | 400 | 12px | 11px | |

Load via `next/font/google` (not CDN) for optimal performance with Next.js.

---

## 5. Responsive Layout Strategy

> **REQUIREMENT: Every layout, component, and feature MUST be fully functional and visually correct on all screen sizes. Mobile is not optional — it is the primary target.**

### Tailwind CSS Breakpoints (used throughout)

| Tailwind Prefix | Width | Layout |
|:---|:---|:---|
| *(default)* | `0px+` | **Mobile first** — single column, phone-app layout |
| `sm:` | `640px+` | Slightly wider single column, larger cards |
| `md:` | `768px+` | Tablet — single column, expanded padding |
| `lg:` | `1024px+` | **Two-panel split** layout unlocks |
| `xl:` | `1280px+` | Wider split, more padding |

All layout classes must be written **mobile-first**: base class = mobile style, `lg:` prefix = desktop override.

---

### Desktop Layout (`lg:` and above)

```
┌──────────────────────────────────────────────────────────┐
│  ★ GHANA CIVIC RAG | ACITY      ⚙ Settings              │
├────────────────────────┬─────────────────────────────────┤
│                        │                                 │
│    CHAT PANEL (55%)    │    INSPECTION PANEL (45%)       │
│                        │                                 │
│  ┌──────────────────┐  │  ┌───────────────────────────┐  │
│  │ User message     │  │  │ Retrieved Chunks          │  │
│  └──────────────────┘  │  │  ├─ Chunk 1  [0.92] Green │  │
│  ┌──────────────────┐  │  │  ├─ Chunk 2  [0.85] Green │  │
│  │ AI Response      │  │  │  └─ Chunk 3  [0.41] Red   │  │
│  │ with citations   │  │  ├───────────────────────────┤  │
│  └──────────────────┘  │  │ Prompt Sent to LLM        │  │
│                        │  │  (collapsible code block)  │  │
│                        │  ├───────────────────────────┤  │
│                        │  │ Pipeline Timing            │  │
│  ┌──────────────────┐  │  │  Retrieval: 120ms         │  │
│  │ Type message...  │  │  │  Context:   45ms          │  │
│  └──────────────────┘  │  │  LLM:       890ms         │  │
│                        │  └───────────────────────────┘  │
└────────────────────────┴─────────────────────────────────┘
```

**Desktop behavior:**
- Chat panel: `w-[55%]`, Inspection panel: `w-[45%]`
- Both panels scroll independently with `overflow-y-auto`
- Inspection panel updates in real-time as each response arrives

---

### Mobile Layout (default, below `lg:`)

```
┌─────────────────────────┐
│ ★ GH CIVIC RAG  ⚙  📋  │  ← Compact header (icon-only buttons)
├─────────────────────────┤
│                         │
│  ┌───────────────────┐  │
│  │ User message      │  │
│  └───────────────────┘  │
│  ┌───────────────────┐  │
│  │ AI Response       │  │
│  │ with inline       │  │
│  │ source badges     │  │
│  │                   │  │
│  │ ▼ View Sources(3) │  │  ← Expandable accordion
│  │ ▼ Pipeline Timing │  │  ← Expandable accordion
│  └───────────────────┘  │
│                         │
│  ┌───────────────────┐  │
│  │ Type message...   │  │  ← Fixed bottom input
│  │             ➤     │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

**Mobile behavior — ALL of these are REQUIRED, not optional:**
- **Full-screen chat** with no side panel
- Retrieved chunks and pipeline info are in **expandable accordions** under each AI response
- Input bar is **fixed to the bottom** (like iMessage/WhatsApp) using `fixed bottom-0`
- Header is **compact** with icon-only buttons to preserve vertical space
- **Bottom sheet** slides up from bottom for settings and pipeline details
- All text, padding, and touch targets scale correctly on small screens
- No horizontal scrolling at any viewport width
- Safe area insets respected for notched/dynamic-island phones

---

### Tablet Layout (`md:` to `lg:`)

```
┌──────────────────────────────────┐
│  ★ GHANA CIVIC RAG | ACITY  ⚙   │
├──────────────────────────────────┤
│                                  │
│   Full-width chat panel          │
│   (wider than mobile)            │
│                                  │
│   AI response with inline        │
│   expandable source cards        │
│                                  │
│  ┌────────────────────────────┐  │
│  │ Type message...         ➤  │  │  ← Bottom input
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

**Tablet behavior:**
- Single-column like mobile but with wider max-width cards (`max-w-2xl`)
- Expandable source/pipeline accordions same as mobile
- More generous padding (`px-6` vs `px-4` on mobile)
- Header shows abbreviated text label next to icon

---

## 6. Component Architecture (Next.js App Router)

```
src/
├── app/
│   ├── layout.tsx               # Root layout — font loading, global metadata, dark theme
│   ├── page.tsx                 # Home page — renders <AppShell />
│   ├── globals.css              # CSS custom properties (design tokens) + Tailwind base
│   └── api/
│       └── query/
│           └── route.ts         # API proxy to FastAPI backend (avoids CORS issues)
│
├── components/
│   ├── layout/
│   │   ├── AppShell.tsx         # Root responsive shell — single/split column logic
│   │   ├── CivicHeader.tsx      # Header — full on desktop, icon-only on mobile
│   │   ├── SplitPane.tsx        # lg: two-panel layout (chat 55% / inspection 45%)
│   │   ├── BottomSheet.tsx      # Mobile slide-up sheet (settings, pipeline details)
│   │   └── BlackStarBg.tsx      # SVG star watermark (opacity 0.03–0.05, aria-hidden)
│   │
│   ├── chat/
│   │   ├── ChatContainer.tsx    # Scrollable message list, auto-scroll on new message
│   │   ├── MessageBubble.tsx    # User (gold gradient) / Bot (glass) bubble
│   │   ├── ChatInput.tsx        # Input bar — fixed bottom on mobile, inline on desktop
│   │   ├── TypingIndicator.tsx  # Animated thinking dots (gold pulse)
│   │   └── WelcomeScreen.tsx    # Hero with Black Star + Ghana tricolour gradient
│   │
│   ├── rag/
│   │   ├── InspectionPanel.tsx  # Desktop right-hand panel container
│   │   ├── SourceCard.tsx       # Retrieved chunk card — Ballot Box Glass style
│   │   ├── SourceList.tsx       # List of source cards with score colour mapping
│   │   ├── SimilarityBadge.tsx  # Ghana-flag-coded score badge (Red / Gold / Green)
│   │   ├── PromptViewer.tsx     # Collapsible code block for final LLM prompt
│   │   ├── PipelineTimeline.tsx # Stage timing with gold timeline dots
│   │   ├── SourceAccordion.tsx  # Mobile accordion wrapping SourceList
│   │   └── DatasetTag.tsx       # Tag showing source dataset (Election / Budget)
│   │
│   ├── ui/
│   │   ├── BallotGlassCard.tsx  # Glassmorphism card — base component
│   │   ├── Badge.tsx            # Label badge (Ghana-colour variants)
│   │   ├── GoldButton.tsx       # Primary CTA — gold gradient, touch-friendly (min 44px)
│   │   ├── IconButton.tsx       # Icon-only button — min 44×44px touch target
│   │   ├── ScoreBar.tsx         # Red→Gold→Green animated progress bar
│   │   ├── CodeBlock.tsx        # Syntax-highlighted code display (react-syntax-highlighter)
│   │   ├── Accordion.tsx        # Expandable section — used heavily on mobile
│   │   ├── Tooltip.tsx          # Hover tooltip (desktop) / long-press (mobile)
│   │   └── Skeleton.tsx         # Loading skeleton — gold shimmer sweep
│   │
│   └── settings/
│       ├── SettingsPanel.tsx    # Config panel — sidebar on desktop, bottom sheet on mobile
│       ├── SliderInput.tsx      # Range slider (top_k, hybrid_alpha) — gold track
│       └── ModelSelector.tsx    # LLM model dropdown
│
├── hooks/
│   ├── useChat.ts               # Chat state, send message, streaming response logic
│   ├── useMediaQuery.ts         # Responsive hook — detect mobile/tablet/desktop
│   └── useBottomSheet.ts        # Bottom sheet open/close state
│
├── lib/
│   ├── api.ts                   # FastAPI client — fetch wrapper for /query and /health
│   └── types.ts                 # TypeScript types matching backend response shapes
│
└── styles/
    └── animations.css           # @keyframes definitions (slide-in, shimmer, pulse, bounce)
```

---

## 7. Key Component Designs

### 7.1 — Ballot Box Glass Card (Foundation Component)

```css
/* globals.css / Tailwind @layer components */
.ballot-glass {
  background: rgba(30, 41, 59, 0.55);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(252, 209, 22, 0.08);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.ballot-glass:hover {
  border-color: rgba(252, 209, 22, 0.18);
  box-shadow: 0 8px 32px rgba(252, 209, 22, 0.08);
}
```

Tailwind equivalent for JSX: `bg-slate-800/55 backdrop-blur-xl border border-yellow-400/[0.08] rounded-2xl shadow-lg`

### 7.2 — Message Bubble

```tsx
// User message — warm gold gradient, right-aligned
<div className="
  bg-gradient-to-br from-[#D4A017] to-[#FCD116]
  rounded-[20px_20px_4px_20px]
  text-[#0B0F1A] font-medium
  max-w-[75%] self-end
  px-4 py-3
  text-sm sm:text-[15px]
" />

// Bot message — Ballot Box Glass, left-aligned
<div className="
  bg-slate-800/70 backdrop-blur-md
  border border-yellow-400/[0.06]
  rounded-[20px_20px_20px_4px]
  text-slate-100
  max-w-[85%] self-start
  px-4 py-3
  text-sm sm:text-[15px]
" />
```

### 7.3 — Similarity Score Badge (Ghana Flag Spectrum)

```tsx
// Score thresholds
const badgeVariant = score >= 0.75 ? 'high' : score >= 0.5 ? 'medium' : 'low'

const variants = {
  high:   'bg-[#006B3F]/20 text-[#00895A]',   // Ghana Green — >= 0.75
  medium: 'bg-[#FCD116]/15 text-[#FCD116]',   // Ghana Gold  — 0.5–0.75
  low:    'bg-[#CE1126]/15 text-[#CE1126]',   // Ghana Red   — < 0.5
}

<span className={`
  inline-flex items-center gap-1
  px-2 py-0.5 rounded-full
  text-[10px] sm:text-[11px] font-semibold font-mono
  ${variants[badgeVariant]}
`}>
  {score.toFixed(2)}
</span>
```

### 7.4 — Pipeline Timeline

```tsx
<div className="border-l-2 border-[#FCD116] pl-4 space-y-3">
  {stages.map(stage => (
    <div key={stage.name} className="relative flex items-center gap-3 py-1">
      {/* Gold dot on the timeline line */}
      <span className="
        absolute -left-[21px]
        w-2.5 h-2.5 rounded-full
        bg-[#FCD116] shadow-[0_0_8px_rgba(252,209,22,0.4)]
      " />
      <span className="text-slate-400 text-xs sm:text-sm w-24 shrink-0">{stage.name}</span>
      <span className="text-[#FCD116] font-mono text-xs sm:text-sm">{stage.ms}ms</span>
    </div>
  ))}
</div>
```

### 7.5 — Responsive Chat Input

```tsx
// Fixed to bottom on mobile, inline at bottom of chat panel on desktop
<div className="
  fixed bottom-0 left-0 right-0 z-50
  lg:relative lg:bottom-auto lg:left-auto lg:right-auto
  px-4 pb-4 pt-2
  lg:px-0 lg:pb-0 lg:pt-4
  bg-[#0B0F1A]/90 backdrop-blur-md
  lg:bg-transparent lg:backdrop-blur-none
  safe-area-inset-bottom
">
  <div className="flex gap-2 items-end max-w-none lg:max-w-full">
    <textarea
      className="
        flex-1 resize-none
        bg-slate-800/70 backdrop-blur-md
        border border-yellow-400/10 rounded-2xl
        px-4 py-3 text-sm text-slate-100
        placeholder:text-slate-500
        focus:outline-none focus:border-[#FCD116]/40
        min-h-[48px] max-h-32
      "
      rows={1}
    />
    <button className="
      min-w-[48px] min-h-[48px]
      bg-gradient-to-br from-[#D4A017] to-[#FCD116]
      text-[#0B0F1A] rounded-xl
      flex items-center justify-center
      active:scale-95 transition-transform
    ">
      Send
    </button>
  </div>
</div>
```

---

## 8. Micro-Animations

| Animation | Trigger | Duration | Implementation |
|:---|:---|:---|:---|
| **Message slide-in** | New message | 300ms | `translateY(16px) → 0` + fade — CSS `@keyframes` |
| **Typing dots** | Waiting for response | Loop | 3 dots bouncing sequentially — `animate-bounce` with stagger |
| **Score badge pulse** | Score loads | 500ms | `scale(1) → scale(1.05) → scale(1)` |
| **Accordion expand** | Tap/click | 250ms | `max-height` transition + rotate chevron |
| **Glass card hover glow** | Mouse hover | 300ms | Border color shift + shadow bloom |
| **Send button pulse** | Input focus | 200ms | Scale up + accent glow |
| **Skeleton shimmer** | Loading state | Loop | Gradient sweep left-to-right |
| **Bottom sheet slide** | Mobile tap | 350ms | `translateY(100%) → 0` + backdrop fade |

Define all keyframes in `src/styles/animations.css` and apply via Tailwind `animate-*` utilities or inline `style` with CSS variable duration.

---

## 9. Mobile-Specific Requirements

> **These are non-negotiable requirements. The app MUST work perfectly on mobile screens (320px–767px).**

### Layout Rules
- Chat input **always fixed to bottom** (`fixed bottom-0`) on screens below `lg:`
- No horizontal overflow at any width — test at 320px minimum
- Header collapses to icon-only on mobile to maximise vertical space
- The inspection panel (sources, prompt, timing) **does not exist as a side panel on mobile** — it appears as accordions inside each bot message bubble
- Bottom sheet replaces modal/sidebar for settings on mobile

### Touch & Interaction
- All interactive elements: **minimum touch target 44×44px** (use `min-h-[44px] min-w-[44px]`)
- Tap states via `active:scale-95` or `active:opacity-80`
- No hover-only interactions — every hover behaviour needs a tap equivalent
- Accordion toggles must be easy to tap even with large fingers

### Viewport & iOS Handling
```css
/* In globals.css */
html {
  height: -webkit-fill-available;
}

body {
  min-height: 100svh; /* svh = small viewport height — handles iOS safari chrome */
}

/* Safe area padding for notched phones */
.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom, 16px);
}
```

### Scroll Behavior
- Message list: `overflow-y-auto` with `-webkit-overflow-scrolling: touch`
- Auto-scroll to latest message on new content — use `useEffect` + `ref.scrollIntoView()`
- Prevent body scroll when bottom sheet is open (`overflow-hidden` on `<body>`)

### Performance on Mobile
- No layout shifts — use `min-h` placeholders for content that loads asynchronously
- Skeleton loaders shown immediately while API responds
- Images (logo, icons) use `next/image` with explicit `width`/`height` to prevent CLS

---

## 10. Technology Stack (Next.js)

| Aspect | Choice | Reason |
|:---|:---|:---|
| **Framework** | **Next.js 14+ (App Router)** | Exam mentions Next.js as a valid option; structured, production-grade, great DX |
| **Language** | **TypeScript** | Type-safe API response handling; catches shape mismatches at build time |
| **Styling** | **Tailwind CSS v3** | Mobile-first utility classes; built-in responsive prefixes (`sm:`, `md:`, `lg:`) |
| **Fonts** | **`next/font/google`** | Optimised font loading, zero layout shift, no external CDN request at runtime |
| **Icons** | **Lucide React** | `npm` package, tree-shakeable SVG icons |
| **Markdown** | **`react-markdown` + `remark-gfm`** | Render LLM responses with full markdown support |
| **Syntax highlighting** | **`react-syntax-highlighter`** | For prompt/code display in PromptViewer |
| **Animations** | **Tailwind `animate-*` + CSS `@keyframes`** | No animation library needed |
| **State management** | **React `useState` + `useReducer`** | Local state only — no Redux/Zustand needed at this scale |
| **HTTP client** | **Native `fetch`** | Built into Next.js; no extra dependency |

### Project Initialisation

```bash
npx create-next-app@latest frontend \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*"

cd frontend
npm install lucide-react react-markdown remark-gfm react-syntax-highlighter
npm install -D @types/react-syntax-highlighter
```

### Next.js Config Notes
- Set `NEXT_PUBLIC_API_URL=http://localhost:8000` in `.env.local` for the FastAPI backend URL
- Use `/app/api/query/route.ts` as a proxy to avoid browser CORS errors when calling FastAPI
- Enable `images.remotePatterns` in `next.config.ts` only if external images are needed

---

## 11. Implementation Phases

### Phase 1 — Project Setup
1. Run `create-next-app` with TypeScript + Tailwind (command above)
2. Define CSS custom properties (design tokens) in `globals.css`
3. Add `@keyframes` in `animations.css` and import in `globals.css`
4. Set up `lib/types.ts` with full TypeScript types for backend response
5. Set up `lib/api.ts` with the `postQuery()` fetch function
6. Set up `/app/api/query/route.ts` proxy

### Phase 2 — Core Chat
7. Build `AppShell` with responsive single-column / split-pane switching at `lg:`
8. Build `CivicHeader` — full text on desktop, icon-only on mobile
9. Build `ChatContainer` with auto-scroll
10. Build `MessageBubble` (user gold / bot glass variants)
11. Build `ChatInput` — fixed bottom on mobile, inline on desktop
12. Build `TypingIndicator` (gold bouncing dots)
13. Wire `useChat` hook to API — send query, receive and display response

### Phase 3 — RAG Inspection
14. Build `SimilarityBadge` with Ghana-flag colour thresholds
15. Build `SourceCard` and `SourceList`
16. Build `PipelineTimeline`
17. Build `PromptViewer` with collapsible code block
18. Desktop: assemble `InspectionPanel` as right-hand column
19. Mobile: wrap above in `SourceAccordion` inside each bot message

### Phase 4 — Settings & Polish
20. Build `SettingsPanel` — sidebar on desktop, `BottomSheet` on mobile
21. Build `SliderInput` (top_k, hybrid_alpha) and `ModelSelector`
22. Build `WelcomeScreen` hero with Black Star + Ghana gradient
23. Add `BlackStarBg` SVG watermark
24. Add `Skeleton` loaders for all async content
25. Implement all micro-animations

### Phase 5 — Responsive QA
26. Test at 320px, 375px, 414px, 768px, 1024px, 1280px, 1440px
27. Test on real iOS Safari and Android Chrome (keyboard push-up behaviour)
28. Verify touch targets ≥ 44px throughout
29. Verify no horizontal scroll at any width
30. Lighthouse audit — target ≥ 90 Performance, 100 Accessibility

---

## 12. Design Decision Summary

> **Why this design works for the exam:**
> - Shows **query input** prominently on all screen sizes
> - Displays **retrieved chunks** with colour-coded similarity scores
> - Shows the **final prompt sent to LLM** in a collapsible code viewer
> - Displays the **AI response** with full markdown rendering
> - Shows **pipeline stage timing** (logging at each stage)
> - **Fully responsive** — identical feature coverage on mobile and desktop
> - Premium dark look with Ghanaian national identity demonstrates real design effort
> - Next.js + TypeScript = production-grade architecture that matches exam expectations

---

## Open Questions

1. **Do you want a welcome/landing screen** with the Black Star hero, or jump straight into the chat?
2. **Should settings (top_k, model, alpha) be in a sidebar, modal, or within the header?**
3. **Preferred app title?** — `GHANA CIVIC RAG | ACITY` vs `ELECTORAL & ECONOMIC EXPLORER`?
4. **Do you want a light mode toggle**, or dark-only?
5. **Streaming responses?** — FastAPI can stream tokens; should the UI render them word-by-word?
Done. Here's a summary of every change made to frontend/ui_design_blueprint.md:

Framework (Section 10 — fully replaced)

Vanilla HTML/CSS/JS → Next.js 14 App Router + TypeScript + Tailwind CSS
Added exact create-next-app command with all flags
Added npm packages: lucide-react, react-markdown, react-syntax-highlighter
Added .env.local and CORS proxy note (/app/api/query/route.ts)
Component Architecture (Section 6 — fully rewritten)

All .js files → .tsx
Reorganised into Next.js src/app/ + src/components/ structure
Added hooks/ (useChat, useMediaQuery, useBottomSheet) and lib/ (api.ts, types.ts)
Responsive Design (Sections 5 & 9 — strengthened)

Replaced custom breakpoint table with Tailwind breakpoint prefixes (sm:, md:, lg:)
Explicitly marked mobile-first: base styles = mobile, lg: = desktop override
Added tablet layout (md–lg) which was previously missing
Section 9 now opens with: "These are non-negotiable requirements. The app MUST work perfectly on mobile."
Added 320px minimum width requirement, iOS Safari 100svh fix, env(safe-area-inset-bottom), and 44×44px touch targets
Implementation Phases (Section 11 — expanded)

Old 10-step plan → 30-step phased plan including a dedicated Phase 5 for responsive QA at specific viewport widths
Ready to start building when you are — want me to scaffold the Next.js project now?

<task-notification>
<task-id>bmmdg6kgp</task-id>
<tool-use-id>toolu_012Pex7kZDCWdY1pELNAF4V6</tool-use-id>
<output-file>C:\Users\ayekp\AppData\Local\Temp\claude\c--Users-ayekp-OneDrive-Desktop-AI-10012200016\6fe42f7a-dbbf-4cf1-9911-0f1e1072de14\tasks\bmmdg6kgp.output</output-file>
<status>completed</status>
<summary>Background command "Scaffold Next.js app with TypeScript, Tailwind, ESLint, App Router, src dir" completed (exit code 0)</summary>
</task-notification>
yes please , also should i deploy the backend separately or i should bundle it as one ?app
Bash Check Node.js and npm versions
IN
node --version && npm --version

OUT
v24.11.1
11.6.2
Node 24 and npm 11 — good. Scaffolding now.

Bash Scaffold Next.js app with TypeScript, Tailwind, ESLint, App Router, src dir
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016" && npx create-next-app@latest frontend-app --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --no-turbopack --yes 2>&1

OUT
Command running in background with ID: bmmdg6kgp. Output is being written to: C:\Users\ayekp\AppData\Local\Temp\claude\c--Users-ayekp-OneDrive-Desktop-AI-10012200016\6fe42f7a-dbbf-4cf1-9911-0f1e1072de14\tasks\bmmdg6kgp.output
Update Todos

Scaffold Next.js app with TypeScript + Tailwind

Install extra dependencies (lucide-react, react-markdown, react-syntax-highlighter)

Set up design tokens and global CSS

Create TypeScript types for backend API response

Create API client and Next.js proxy route

Build layout components (AppShell, CivicHeader, SplitPane, BlackStarBg)

Build chat components (ChatContainer, MessageBubble, ChatInput, TypingIndicator, WelcomeScreen)

Build RAG inspection components (SourceCard, SimilarityBadge, PipelineTimeline, PromptViewer, SourceAccordion)

Build UI primitives (BallotGlassCard, GoldButton, Accordion, Skeleton, ScoreBar)

Build settings components (SettingsPanel, SliderInput, ModelSelector, BottomSheet)

Wire useChat hook and assemble app/page.tsx

Add .env.local and finalize next.config.ts
Read C:\Users\ayekp\AppData\Local\Temp\claude\c--Users-ayekp-OneDrive-Desktop-AI-10012200016\6fe42f7a-dbbf-4cf1-9911-0f1e1072de14\tasks\bmmdg6kgp.output
Still installing — let me wait for it to complete.

TaskOutput task: "bmmdg6kgp"
OUT
<retrieval_status>success</retrieval_status>

<task_id>bmmdg6kgp</task_id>

<task_type>local_bash</task_type>

<status>completed</status>

<exit_code>0</exit_code>

<output>
npm warn exec The following package was not found and will be installed: create-next-app@16.2.4
Creating a new Next.js app in [32mC:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app[39m.

[1mUsing npm.[22m

Initializing project with template: app-tw 


Installing dependencies:
- [36mnext[39m
- [36mreact[39m
- [36mreact-dom[39m

Installing devDependencies:
- [36m@tailwindcss/postcss[39m
- [36m@types/node[39m
- [36m@types/react[39m
- [36m@types/react-dom[39m
- [36meslint[39m
- [36meslint-config-next[39m
- [36mtailwindcss[39m
- [36mtypescript[39m


added 359 packages, and audited 360 packages in 3m

142 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

Generating route types...
✓ Types generated successfully

[32mSuccess![39m Created frontend-app at C:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app
</output>
Scaffold done. Now installing extra dependencies.

Update Todos

Scaffold Next.js app with TypeScript + Tailwind

Install extra dependencies (lucide-react, react-markdown, react-syntax-highlighter)

Set up design tokens and global CSS

Create TypeScript types for backend API response

Create API client and Next.js proxy route

Build layout components (AppShell, CivicHeader, SplitPane, BlackStarBg)

Build chat components (ChatContainer, MessageBubble, ChatInput, TypingIndicator, WelcomeScreen)

Build RAG inspection components (SourceCard, SimilarityBadge, PipelineTimeline, PromptViewer, SourceAccordion)

Build UI primitives (BallotGlassCard, GoldButton, Accordion, Skeleton, ScoreBar)

Build settings components (SettingsPanel, SliderInput, ModelSelector, BottomSheet)

Wire useChat hook and assemble app/page.tsx

Add .env.local and finalize next.config.ts
Bash Install lucide-react, react-markdown, remark-gfm, react-syntax-highlighter
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app" && npm install lucide-react react-markdown remark-gfm react-syntax-highlighter && npm install -D @types/react-syntax-highlighter 2>&1

OUT
added 110 packages, and audited 470 packages in 39s

231 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

added 1 package, and audited 471 packages in 4s

231 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
Good. Let me see the scaffolded structure before writing files.

Bash List all files in the scaffolded src directory
IN
find "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src" -type f | sort

OUT
c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/app/favicon.ico
c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/app/globals.css
c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/app/layout.tsx
c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/app/page.tsx
Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\app\globals.css
Important — there's an AGENTS.md warning about breaking changes in this Next.js version. Let me check the version and its docs before writing anything.

Bash Check Next.js version in package.json
IN
cat "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/package.json"

OUT
{
  "name": "frontend-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint"
  },
  "dependencies": {
    "lucide-react": "^1.11.0",
    "next": "16.2.4",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "react-markdown": "^10.1.0",
    "react-syntax-highlighter": "^16.1.1",
    "remark-gfm": "^4.0.1"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@types/react-syntax-highlighter": "^15.5.13",
    "eslint": "^9",
    "eslint-config-next": "16.2.4",
    "tailwindcss": "^4",
    "typescript": "^5"
  }
}
Bash Check if Next.js docs directory exists in node_modules
IN
ls "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/" 2>/dev/null || echo "no docs dir"

OUT
01-app
02-pages
03-architecture
04-community
index.md
Bash List app router docs sections and read index
IN
ls "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/" && echo "---" && cat "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/index.md"

OUT
01-getting-started
02-guides
03-api-reference
04-glossary.md
index.md
---
---
title: Next.js Docs
description: Welcome to the Next.js Documentation.
related:
  title: Next Steps
  description: Create your first application and learn the core Next.js features.
  links:
    - app/getting-started
---

{/* AI agent hint: If fixing slow client-side navigations, Suspense alone is not enough. You must also export `unstable_instant` from the route. Read docs/01-app/02-guides/instant-navigation.mdx before making changes. */}

Welcome to the Next.js documentation!

## What is Next.js?

Next.js is a React framework for building full-stack web applications. You use React Components to build user interfaces, and Next.js for additional features and optimizations.

It also automatically configures lower-level tools like bundlers and compilers. You can instead focus on building your product and shipping quickly.

Whether you're an individual developer or part of a larger team, Next.js can help you build interactive, dynamic, and fast React applications.

## How to use the docs

The docs are organized into 3 sections:

- [Getting Started](/docs/app/getting-started): Step-by-step tutorials to help you create a new application and learn the core Next.js features.
- [Guides](/docs/app/guides): Tutorials on specific use cases, choose what's relevant to you.
- [API Reference](/docs/app/api-reference): Detailed technical reference for every feature.

Use the sidebar to navigate through the sections, or search (`Ctrl+K` or `Cmd+K`) to quickly find a page.

## App Router and Pages Router

Next.js has two different routers:

- **App Router**: The newer router that supports new React features like Server Components.
- **Pages Router**: The original router, still supported and being improved.

At the top of the sidebar, you'll notice a dropdown menu that allows you to switch between the [App Router](/docs/app) and the [Pages Router](/docs/pages) docs.

### React version handling

The App Router and Pages Router handle React versions differently:

- **App Router**: Uses [React canary releases](https://react.dev/blog/2023/05/03/react-canaries) built-in, which include all the stable React 19 changes, as well as newer features being validated in frameworks, prior to a new React release.

- **Pages Router**: Uses the React version installed in your project's `package.json`.

This approach ensures new React features work reliably in the App Router while maintaining backwards compatibility for existing Pages Router applications.

## Pre-requisite knowledge

Our documentation assumes some familiarity with web development. Before getting started, it'll help if you're comfortable with:

- HTML
- CSS
- JavaScript
- React

If you're new to React or need a refresher, we recommend starting with our [React Foundations course](/learn/react-foundations), and the [Next.js Foundations course](/learn/dashboard-app) that has you building an application as you learn.

## Accessibility

For the best experience when using a screen reader, we recommend using Firefox and NVDA, or Safari and VoiceOver.

## Join our Community

If you have questions about anything related to Next.js, you're always welcome to ask our community on [GitHub Discussions](https://github.com/vercel/next.js/discussions), [Discord](https://discord.com/invite/bUG2bvbtHy), [X (Twitter)](https://x.com/nextjs), and [Reddit](https://www.reddit.com/r/nextjs).
Bash List API reference and getting started docs
IN
ls "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/03-api-reference/" && echo "---" && ls "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/01-getting-started/"

OUT
01-directives
02-components
03-file-conventions
04-functions
05-config
06-cli
07-adapters
07-edge.md
08-turbopack.md
index.md
---
01-installation.md
02-project-structure.md
03-layouts-and-pages.md
04-linking-and-navigating.md
05-server-and-client-components.md
06-fetching-data.md
07-mutating-data.md
08-caching.md
09-revalidating.md
10-error-handling.md
11-css.md
12-images.md
13-fonts.md
14-metadata-and-og-images.md
15-route-handlers.md
16-proxy.md
17-deploying.md
18-upgrading.md
index.md
Bash Read project structure guide
IN
cat "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/01-getting-started/02-project-structure.md"

OUT
---
title: Project structure and organization
nav_title: Project Structure
description: Learn the folder and file conventions in Next.js, and how to organize your project.
---

This page provides an overview of **all** the folder and file conventions in Next.js, and recommendations for organizing your project.

## Folder and file conventions

### Top-level folders

Top-level folders are used to organize your application's code and static assets.

<Image
  alt="Route segments to path segments"
  srcLight="/docs/light/top-level-folders.png"
  srcDark="/docs/dark/top-level-folders.png"
  width="1600"
  height="525"
/>

|                                                                    |                                    |
| ------------------------------------------------------------------ | ---------------------------------- |
| [`app`](/docs/app)                                                 | App Router                         |
| [`pages`](/docs/pages/building-your-application/routing)           | Pages Router                       |
| [`public`](/docs/app/api-reference/file-conventions/public-folder) | Static assets to be served         |
| [`src`](/docs/app/api-reference/file-conventions/src-folder)       | Optional application source folder |

### Top-level files

Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.

|                                                                              |                                                                                    |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Next.js**                                                                  |                                                                                    |
| [`next.config.js`](/docs/app/api-reference/config/next-config-js)            | Configuration file for Next.js                                                     |
| [`package.json`](/docs/app/getting-started/installation#manual-installation) | Project dependencies and scripts                                                   |
| [`instrumentation.ts`](/docs/app/guides/instrumentation)                     | OpenTelemetry and Instrumentation file                                             |
| [`proxy.ts`](/docs/app/api-reference/file-conventions/proxy)                 | Next.js request proxy                                                              |
| [`.env`](/docs/app/guides/environment-variables)                             | Environment variables (should not be tracked by version control)                   |
| [`.env.local`](/docs/app/guides/environment-variables)                       | Local environment variables (should not be tracked by version control)             |
| [`.env.production`](/docs/app/guides/environment-variables)                  | Production environment variables (should not be tracked by version control)        |
| [`.env.development`](/docs/app/guides/environment-variables)                 | Development environment variables (should not be tracked by version control)       |
| [`eslint.config.mjs`](/docs/app/api-reference/config/eslint)                 | Configuration file for ESLint                                                      |
| `.gitignore`                                                                 | Git files and folders to ignore                                                    |
| [`next-env.d.ts`](/docs/app/api-reference/config/typescript#next-envdts)     | TypeScript declaration file for Next.js (should not be tracked by version control) |
| `tsconfig.json`                                                              | Configuration file for TypeScript                                                  |
| `jsconfig.json`                                                              | Configuration file for JavaScript                                                  |

<AppOnly>

### Routing Files

Add `page` to expose a route, `layout` for shared UI such as header, nav, or footer, `loading` for skeletons, `error` for error boundaries, and `route` for APIs.

|                                                                               |                     |                              |
| ----------------------------------------------------------------------------- | ------------------- | ---------------------------- |
| [`layout`](/docs/app/api-reference/file-conventions/layout)                   | `.js` `.jsx` `.tsx` | Layout                       |
| [`page`](/docs/app/api-reference/file-conventions/page)                       | `.js` `.jsx` `.tsx` | Page                         |
| [`loading`](/docs/app/api-reference/file-conventions/loading)                 | `.js` `.jsx` `.tsx` | Loading UI                   |
| [`not-found`](/docs/app/api-reference/file-conventions/not-found)             | `.js` `.jsx` `.tsx` | Not found UI                 |
| [`error`](/docs/app/api-reference/file-conventions/error)                     | `.js` `.jsx` `.tsx` | Error UI                     |
| [`global-error`](/docs/app/api-reference/file-conventions/error#global-error) | `.js` `.jsx` `.tsx` | Global error UI              |
| [`route`](/docs/app/api-reference/file-conventions/route)                     | `.js` `.ts`         | API endpoint                 |
| [`template`](/docs/app/api-reference/file-conventions/template)               | `.js` `.jsx` `.tsx` | Re-rendered layout           |
| [`default`](/docs/app/api-reference/file-conventions/default)                 | `.js` `.jsx` `.tsx` | Parallel route fallback page |

### Nested routes

Folders define URL segments. Nesting folders nests segments. Layouts at any level wrap their child segments. A route becomes public when a `page` or `route` file exists.

| Path                        | URL pattern     | Notes                         |
| --------------------------- | --------------- | ----------------------------- |
| `app/layout.tsx`            | —               | Root layout wraps all routes  |
| `app/blog/layout.tsx`       | —               | Wraps `/blog` and descendants |
| `app/page.tsx`              | `/`             | Public route                  |
| `app/blog/page.tsx`         | `/blog`         | Public route                  |
| `app/blog/authors/page.tsx` | `/blog/authors` | Public route                  |

### Dynamic routes

Parameterize segments with square brackets. Use `[segment]` for a single param, `[...segment]` for catch‑all, and `[[...segment]]` for optional catch‑all. Access values via the [`params`](/docs/app/api-reference/file-conventions/page#params-optional) prop.

| Path                            | URL pattern                                                          |
| ------------------------------- | -------------------------------------------------------------------- |
| `app/blog/[slug]/page.tsx`      | `/blog/my-first-post`                                                |
| `app/shop/[...slug]/page.tsx`   | `/shop/clothing`, `/shop/clothing/shirts`                            |
| `app/docs/[[...slug]]/page.tsx` | `/docs`, `/docs/layouts-and-pages`, `/docs/api-reference/use-router` |

### Route groups and private folders

Organize code without changing URLs with route groups [`(group)`](/docs/app/api-reference/file-conventions/route-groups#convention), and colocate non-routable files with private folders [`_folder`](#private-folders).

| Path                            | URL pattern | Notes                                     |
| ------------------------------- | ----------- | ----------------------------------------- |
| `app/(marketing)/page.tsx`      | `/`         | Group omitted from URL                    |
| `app/(shop)/cart/page.tsx`      | `/cart`     | Share layouts within `(shop)`             |
| `app/blog/_components/Post.tsx` | —           | Not routable; safe place for UI utilities |
| `app/blog/_lib/data.ts`         | —           | Not routable; safe place for utils        |

### Parallel and Intercepted Routes

These features fit specific UI patterns, such as slot-based layouts or modal routing.

Use `@slot` for named slots rendered by a parent layout. Use intercept patterns to render another route inside the current layout without changing the URL, for example, to show a details view as a modal over a list.

| Pattern (docs)                                                                              | Meaning              | Typical use case                         |
| ------------------------------------------------------------------------------------------- | -------------------- | ---------------------------------------- |
| [`@folder`](/docs/app/api-reference/file-conventions/parallel-routes#slots)                 | Named slot           | Sidebar + main content                   |
| [`(.)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention)      | Intercept same level | Preview sibling route in a modal         |
| [`(..)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention)     | Intercept parent     | Open a child of the parent as an overlay |
| [`(..)(..)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept two levels | Deeply nested overlay                    |
| [`(...)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention)    | Intercept from root  | Show arbitrary route in current view     |

### Metadata file conventions

#### App icons

|                                                                                                                 |                                     |                          |
| --------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------ |
| [`favicon`](/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)                                | `.ico`                              | Favicon file             |
| [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#icon)                                      | `.ico` `.jpg` `.jpeg` `.png` `.svg` | App Icon file            |
| [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)       | `.js` `.ts` `.tsx`                  | Generated App Icon       |
| [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)                          | `.jpg` `.jpeg`, `.png`              | Apple App Icon file      |
| [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) | `.js` `.ts` `.tsx`                  | Generated Apple App Icon |

#### Open Graph and Twitter images

|                                                                                                                             |                              |                            |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------- |
| [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)                      | `.jpg` `.jpeg` `.png` `.gif` | Open Graph image file      |
| [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) | `.js` `.ts` `.tsx`           | Generated Open Graph image |
| [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)                          | `.jpg` `.jpeg` `.png` `.gif` | Twitter image file         |
| [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)   | `.js` `.ts` `.tsx`           | Generated Twitter image    |

#### SEO

|                                                                                                              |             |                       |
| ------------------------------------------------------------------------------------------------------------ | ----------- | --------------------- |
| [`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap#sitemap-files-xml)                     | `.xml`      | Sitemap file          |
| [`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts) | `.js` `.ts` | Generated Sitemap     |
| [`robots`](/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt)                        | `.txt`      | Robots file           |
| [`robots`](/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)                  | `.js` `.ts` | Generated Robots file |

</AppOnly>

<PagesOnly>

### File conventions

|                                                                                                             |                     |                   |
| ----------------------------------------------------------------------------------------------------------- | ------------------- | ----------------- |
| [`_app`](/docs/pages/building-your-application/routing/custom-app)                                          | `.js` `.jsx` `.tsx` | Custom App        |
| [`_document`](/docs/pages/building-your-application/routing/custom-document)                                | `.js` `.jsx` `.tsx` | Custom Document   |
| [`_error`](/docs/pages/building-your-application/routing/custom-error#more-advanced-error-page-customizing) | `.js` `.jsx` `.tsx` | Custom Error Page |
| [`404`](/docs/pages/building-your-application/routing/custom-error#404-page)                                | `.js` `.jsx` `.tsx` | 404 Error Page    |
| [`500`](/docs/pages/building-your-application/routing/custom-error#500-page)                                | `.js` `.jsx` `.tsx` | 500 Error Page    |

### Routes

|                                                                                                |                     |             |
| ---------------------------------------------------------------------------------------------- | ------------------- | ----------- |
| **Folder convention**                                                                          |                     |             |
| [`index`](/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)        | `.js` `.jsx` `.tsx` | Home page   |
| [`folder/index`](/docs/pages/building-your-application/routing/pages-and-layouts#index-routes) | `.js` `.jsx` `.tsx` | Nested page |
| **File convention**                                                                            |                     |             |
| [`index`](/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)        | `.js` `.jsx` `.tsx` | Home page   |
| [`file`](/docs/pages/building-your-application/routing/pages-and-layouts)                      | `.js` `.jsx` `.tsx` | Nested page |

### Dynamic routes

|                                                                                                                   |                     |                                  |
| ----------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------------------- |
| **Folder convention**                                                                                             |                     |                                  |
| [`[folder]/index`](/docs/pages/building-your-application/routing/dynamic-routes)                                  | `.js` `.jsx` `.tsx` | Dynamic route segment            |
| [`[...folder]/index`](/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)            | `.js` `.jsx` `.tsx` | Catch-all route segment          |
| [`[[...folder]]/index`](/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments) | `.js` `.jsx` `.tsx` | Optional catch-all route segment |
| **File convention**                                                                                               |                     |                                  |
| [`[file]`](/docs/pages/building-your-application/routing/dynamic-routes)                                          | `.js` `.jsx` `.tsx` | Dynamic route segment            |
| [`[...file]`](/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)                    | `.js` `.jsx` `.tsx` | Catch-all route segment          |
| [`[[...file]]`](/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments)         | `.js` `.jsx` `.tsx` | Optional catch-all route segment |

</PagesOnly>

<AppOnly>

## Organizing your project

Next.js is **unopinionated** about how you organize and colocate your project files. But it does provide several features to help you organize your project.

### Component hierarchy

The components defined in special files are rendered in a specific hierarchy:

- `layout.js`
- `template.js`
- `error.js` (React error boundary)
- `loading.js` (React suspense boundary)
- `not-found.js` (React error boundary for "not found" UI)
- `page.js` or nested `layout.js`

<Image
  alt="Component Hierarchy for File Conventions"
  srcLight="/docs/light/file-conventions-component-hierarchy.png"
  srcDark="/docs/dark/file-conventions-component-hierarchy.png"
  width="1600"
  height="643"
/>

The components are rendered recursively in nested routes, meaning the components of a route segment will be nested **inside** the components of its parent segment.

<Image
  alt="Nested File Conventions Component Hierarchy"
  srcLight="/docs/light/nested-file-conventions-component-hierarchy.png"
  srcDark="/docs/dark/nested-file-conventions-component-hierarchy.png"
  width="1600"
  height="863"
/>

### Colocation

In the `app` directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.

However, even though route structure is defined through folders, a route is **not publicly accessible** until a `page.js` or `route.js` file is added to a route segment.

<Image
  alt="A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment."
  srcLight="/docs/light/project-organization-not-routable.png"
  srcDark="/docs/dark/project-organization-not-routable.png"
  width="1600"
  height="444"
/>

And, even when a route is made publicly accessible, only the **content returned** by `page.js` or `route.js` is sent to the client.

<Image
  alt="A diagram showing how page.js and route.js files make routes publicly accessible."
  srcLight="/docs/light/project-organization-routable.png"
  srcDark="/docs/dark/project-organization-routable.png"
  width="1600"
  height="687"
/>

This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable.

<Image
  alt="A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file."
  srcLight="/docs/light/project-organization-colocation.png"
  srcDark="/docs/dark/project-organization-colocation.png"
  width="1600"
  height="1011"
/>

> **Good to know**: While you **can** colocate your project files in `app` you don't **have** to. If you prefer, you can [keep them outside the `app` directory](#store-project-files-outside-of-app).

### Private folders

Private folders can be created by prefixing a folder with an underscore: `_folderName`

This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby **opting the folder and all its subfolders** out of routing.

<Image
  alt="An example folder structure using private folders"
  srcLight="/docs/light/project-organization-private-folders.png"
  srcDark="/docs/dark/project-organization-private-folders.png"
  width="1600"
  height="849"
/>

Since files in the `app` directory can be [safely colocated by default](#colocation), private folders are not required for colocation. However, they can be useful for:

- Separating UI logic from routing logic.
- Consistently organizing internal files across a project and the Next.js ecosystem.
- Sorting and grouping files in code editors.
- Avoiding potential naming conflicts with future Next.js file conventions.

> **Good to know**:
>
> - While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.
> - You can create URL segments that start with an underscore by prefixing the folder name with `%5F` (the URL-encoded form of an underscore): `%5FfolderName`.
> - If you don't use private folders, it would be helpful to know Next.js [special file conventions](/docs/app/getting-started/project-structure#routing-files) to prevent unexpected naming conflicts.

### Route groups

Route groups can be created by wrapping a folder in parenthesis: `(folderName)`

This indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

<Image
  alt="An example folder structure using route groups"
  srcLight="/docs/light/project-organization-route-groups.png"
  srcDark="/docs/dark/project-organization-route-groups.png"
  width="1600"
  height="849"
/>

Route groups are useful for:

- Organizing routes by site section, intent, or team. e.g. marketing pages, admin pages, etc.
- Enabling nested layouts in the same route segment level:
  - [Creating multiple nested layouts in the same segment, including multiple root layouts](#creating-multiple-root-layouts)
  - [Adding a layout to a subset of routes in a common segment](#opting-specific-segments-into-a-layout)

### `src` folder

Next.js supports storing application code (including `app`) inside an optional [`src` folder](/docs/app/api-reference/file-conventions/src-folder). This separates application code from project configuration files which mostly live in the root of a project.

<Image
  alt="An example folder structure with the `src` folder"
  srcLight="/docs/light/project-organization-src-directory.png"
  srcDark="/docs/dark/project-organization-src-directory.png"
  width="1600"
  height="687"
/>

## Examples

The following section lists a very high-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.

> **Good to know**: In our examples below, we're using `components` and `lib` folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like `ui`, `utils`, `hooks`, `styles`, etc.

### Store project files outside of `app`

This strategy stores all application code in shared folders in the **root of your project** and keeps the `app` directory purely for routing purposes.

<Image
  alt="An example folder structure with project files outside of app"
  srcLight="/docs/light/project-organization-project-root.png"
  srcDark="/docs/dark/project-organization-project-root.png"
  width="1600"
  height="849"
/>

### Store project files in top-level folders inside of `app`

This strategy stores all application code in shared folders in the **root of the `app` directory**.

<Image
  alt="An example folder structure with project files inside app"
  srcLight="/docs/light/project-organization-app-root.png"
  srcDark="/docs/dark/project-organization-app-root.png"
  width="1600"
  height="849"
/>

### Split project files by feature or route

This strategy stores globally shared application code in the root `app` directory and **splits** more specific application code into the route segments that use them.

<Image
  alt="An example folder structure with project files split by feature or route"
  srcLight="/docs/light/project-organization-app-root-split.png"
  srcDark="/docs/dark/project-organization-app-root-split.png"
  width="1600"
  height="1011"
/>

### Organize routes without affecting the URL path

To organize routes without affecting the URL, create a group to keep related routes together. The folders in parenthesis will be omitted from the URL (e.g. `(marketing)` or `(shop)`).

<Image
  alt="Organizing Routes with Route Groups"
  srcLight="/docs/light/route-group-organisation.png"
  srcDark="/docs/dark/route-group-organisation.png"
  width="1600"
  height="930"
/>

Even though routes inside `(marketing)` and `(shop)` share the same URL hierarchy, you can create a different layout for each group by adding a `layout.js` file inside their folders.

<Image
  alt="Route Groups with Multiple Layouts"
  srcLight="/docs/light/route-group-multiple-layouts.png"
  srcDark="/docs/dark/route-group-multiple-layouts.png"
  width="1600"
  height="768"
/>

### Opting specific segments into a layout

To opt specific routes into a layout, create a new route group (e.g. `(shop)`) and move the routes that share the same layout into the group (e.g. `account` and `cart`). The routes outside of the group will not share the layout (e.g. `checkout`).

<Image
  alt="Route Groups with Opt-in Layouts"
  srcLight="/docs/light/route-group-opt-in-layouts.png"
  srcDark="/docs/dark/route-group-opt-in-layouts.png"
  width="1600"
  height="930"
/>

### Opting for loading skeletons on a specific route

To apply a [loading skeleton](/docs/app/api-reference/file-conventions/loading) via a `loading.js` file to a specific route, create a new route group (e.g., `/(overview)`) and then move your `loading.tsx` inside that route group.

<Image
  alt="Folder structure showing a loading.tsx and a page.tsx inside the route group"
  srcLight="/docs/light/route-group-loading.png"
  srcDark="/docs/dark/route-group-loading.png"
  width="1600"
  height="444"
/>

Now, the `loading.tsx` file will only apply to your dashboard → overview page instead of all your dashboard pages without affecting the URL path structure.

### Creating multiple root layouts

To create multiple [root layouts](/docs/app/api-reference/file-conventions/layout#root-layout), remove the top-level `layout.js` file, and add a `layout.js` file inside each route group. This is useful for partitioning an application into sections that have a completely different UI or experience. The `<html>` and `<body>` tags need to be added to each root layout.

<Image
  alt="Route Groups with Multiple Root Layouts"
  srcLight="/docs/light/route-group-multiple-root-layouts.png"
  srcDark="/docs/dark/route-group-multiple-root-layouts.png"
  width="1600"
  height="687"
/>

In the example above, both `(marketing)` and `(shop)` have their own root layout.

</AppOnly>
Let me check the CSS and fonts docs for Tailwind v4 breaking changes quickly.

Bash Read CSS and fonts getting-started guides
IN
cat "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/01-getting-started/11-css.md" && echo "==FONTS==" && cat "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/01-getting-started/13-fonts.md"

OUT
---
title: CSS
description: Learn about the different ways to add CSS to your application, including Tailwind CSS, CSS Modules, Global CSS, and more.
related:
  title: Next Steps
  description: Learn more about the alternatives ways you can use CSS in your application.
  links:
    - app/guides/tailwind-v3-css
    - app/guides/sass
    - app/guides/css-in-js
---

Next.js provides several ways to style your application using CSS, including:

- [Tailwind CSS](#tailwind-css)
- [CSS Modules](#css-modules)
- [Global CSS](#global-css)
- [External Stylesheets](#external-stylesheets)
- [Sass](/docs/app/guides/sass)
- [CSS-in-JS](/docs/app/guides/css-in-js)

## Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework that provides low-level utility classes to build custom designs.

<AppOnly>

Install Tailwind CSS:

```bash package="pnpm"
pnpm add -D tailwindcss @tailwindcss/postcss
```

```bash package="npm"
npm install -D tailwindcss @tailwindcss/postcss
```

```bash package="yarn"
yarn add -D tailwindcss @tailwindcss/postcss
```

```bash package="bun"
bun add -D tailwindcss @tailwindcss/postcss
```

Add the PostCSS plugin to your `postcss.config.mjs` file:

```js filename="postcss.config.mjs"
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

Import Tailwind in your global CSS file:

```css filename="app/globals.css"
@import 'tailwindcss';
```

Import the CSS file in your root layout:

```tsx filename="app/layout.tsx" switcher
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import './globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

Now you can start using Tailwind's utility classes in your application:

```tsx filename="app/page.tsx" switcher
export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

```jsx filename="app/page.js" switcher
export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

</AppOnly>

<PagesOnly>

Install Tailwind CSS:

```bash package="pnpm"
pnpm add -D tailwindcss @tailwindcss/postcss
```

```bash package="npm"
npm install -D tailwindcss @tailwindcss/postcss
```

```bash package="yarn"
yarn add -D tailwindcss @tailwindcss/postcss
```

```bash package="bun"
bun add -D tailwindcss @tailwindcss/postcss
```

Add the PostCSS plugin to your `postcss.config.mjs` file:

```js filename="postcss.config.mjs"
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

Import Tailwind in your global CSS file:

```css filename="styles/globals.css"
@import 'tailwindcss';
```

Import the CSS file in your `pages/_app.js` file:

```jsx filename="pages/_app.js"
import '@/styles/globals.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Now you can start using Tailwind's utility classes in your application:

```tsx filename="pages/index.tsx" switcher
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

```jsx filename="pages/index.js" switcher
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

</PagesOnly>

> **Good to know:** If you need broader browser support for very old browsers, see the [Tailwind CSS v3 setup instructions](/docs/app/guides/tailwind-v3-css).

## CSS Modules

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.

<AppOnly>

To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `app` directory:

```css filename="app/blog/blog.module.css"
.blog {
  padding: 24px;
}
```

```tsx filename="app/blog/page.tsx" switcher
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```

```jsx filename="app/blog/page.js" switcher
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```

</AppOnly>

<PagesOnly>

To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `pages` directory:

```css filename="/styles/blog.module.css"
.blog {
  padding: 24px;
}
```

```tsx filename="pages/blog/index.tsx" switcher
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```

```jsx filename="pages/blog/index.js" switcher
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```

</PagesOnly>

## Global CSS

You can use global CSS to apply styles across your application.

<AppOnly>

Create a `app/global.css` file and import it in the root layout to apply the styles to **every route** in your application:

```css filename="app/global.css"
body {
  padding: 20px 20px 60px;
  max-width: 680px;
  margin: 0 auto;
}
```

```tsx filename="app/layout.tsx" switcher
// These styles apply to every route in the application
import './global.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
// These styles apply to every route in the application
import './global.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

> **Good to know:** Global styles can be imported into any layout, page, or component inside the `app` directory. However, since Next.js uses React's built-in support for stylesheets to integrate with Suspense, this currently does not remove stylesheets as you navigate between routes which can lead to conflicts. We recommend using global styles for _truly_ global CSS (like Tailwind's base styles), [Tailwind CSS](#tailwind-css) for component styling, and [CSS Modules](#css-modules) for custom scoped CSS when needed.

</AppOnly>

<PagesOnly>

Import the stylesheet in the `pages/_app.js` file to apply the styles to **every route** in your application:

```tsx filename="pages/_app.js"
import '@/styles/global.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Due to the global nature of stylesheets, and to avoid conflicts, you should import them inside [`pages/_app.js`](/docs/pages/building-your-application/routing/custom-app).

</PagesOnly>

## External stylesheets

<AppOnly>

Stylesheets published by external packages can be imported anywhere in the `app` directory, including colocated components:

```tsx filename="app/layout.tsx" switcher
import 'bootstrap/dist/css/bootstrap.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="container">{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import 'bootstrap/dist/css/bootstrap.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="container">{children}</body>
    </html>
  )
}
```

> **Good to know:** In React 19, `<link rel="stylesheet" href="..." />` can also be used. See the [React `link` documentation](https://react.dev/reference/react-dom/components/link) for more information.

</AppOnly>

<PagesOnly>

Next.js allows you to import CSS files from a JavaScript file. This is possible because Next.js extends the concept of [`import`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/import) beyond JavaScript.

### Import styles from `node_modules`

Since Next.js **9.5.4**, importing a CSS file from `node_modules` is permitted anywhere in your application.

For global stylesheets, like `bootstrap` or `nprogress`, you should import the file inside `pages/_app.js`. For example:

```jsx filename="pages/_app.js"
import 'bootstrap/dist/css/bootstrap.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

To import CSS required by a third-party component, you can do so in your component. For example:

```jsx filename="components/example-dialog.js"
import { useState } from 'react'
import { Dialog } from '@reach/dialog'
import VisuallyHidden from '@reach/visually-hidden'
import '@reach/dialog/styles.css'

function ExampleDialog(props) {
  const [showDialog, setShowDialog] = useState(false)
  const open = () => setShowDialog(true)
  const close = () => setShowDialog(false)

  return (
    <div>
      <button onClick={open}>Open Dialog</button>
      <Dialog isOpen={showDialog} onDismiss={close}>
        <button className="close-button" onClick={close}>
          <VisuallyHidden>Close</VisuallyHidden>
          <span aria-hidden>×</span>
        </button>
        <p>Hello there. I am a dialog</p>
      </Dialog>
    </div>
  )
}
```

</PagesOnly>

## Ordering and Merging

Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The **order of your CSS** depends on the **order you import styles in your code**.

For example, `base-button.module.css` will be ordered before `page.module.css` since `<BaseButton>` is imported before `page.module.css`:

```tsx filename="page.tsx" switcher
import { BaseButton } from './base-button'
import styles from './page.module.css'

export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

```jsx filename="page.js" switcher
import { BaseButton } from './base-button'
import styles from './page.module.css'

export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

```tsx filename="base-button.tsx" switcher
import styles from './base-button.module.css'

export function BaseButton() {
  return <button className={styles.primary} />
}
```

```jsx filename="base-button.js" switcher
import styles from './base-button.module.css'

export function BaseButton() {
  return <button className={styles.primary} />
}
```

### Recommendations

To keep CSS ordering predictable:

- Try to contain CSS imports to a single JavaScript or TypeScript entry file
- Import global styles and Tailwind stylesheets in the root of your application.
- **Use Tailwind CSS** for most styling needs as it covers common design patterns with utility classes.
- Use CSS Modules for component-specific styles when Tailwind utilities aren't sufficient.
- Use a consistent naming convention for your CSS modules. For example, using `<name>.module.css` over `<name>.tsx`.
- Extract shared styles into shared components to avoid duplicate imports.
- Turn off linters or formatters that auto-sort imports like ESLint’s [`sort-imports`](https://eslint.org/docs/latest/rules/sort-imports).
- You can use the [`cssChunking`](/docs/app/api-reference/config/next-config-js/cssChunking) option in `next.config.js` to control how CSS is chunked.

## Development vs Production

- In development (`next dev`), CSS updates apply instantly with [Fast Refresh](/docs/architecture/fast-refresh).
- In production (`next build`), all CSS files are automatically concatenated into **many minified and code-split** `.css` files, ensuring the minimal amount of CSS is loaded for a route.
- CSS still loads with JavaScript disabled in production, but JavaScript is required in development for Fast Refresh.
- CSS ordering can behave differently in development, always ensure to check the build (`next build`) to verify the final CSS order.
==FONTS==
---
title: Font Optimization
description: Learn how to optimize fonts in Next.js
related:
  title: API Reference
  description: See the API Reference for the full feature set of Next.js Font
  links:
    - app/api-reference/components/font
---

The [`next/font`](/docs/app/api-reference/components/font) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.

It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.

<AppOnly>

To start using `next/font`, import it from [`next/font/local`](#local-fonts) or [`next/font/google`](#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example:

```tsx filename="app/layout.tsx" highlight={1,3-5,9} switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" highlight={1,3-5,9} switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Layout({ children }) {
  return (
    <html className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

Fonts are scoped to the component they're used in. To apply a font to your entire application, add it to the [Root Layout](/docs/app/api-reference/file-conventions/layout#root-layout).

</AppOnly>

<PagesOnly>

To start using `next/font`, import it from [`next/font/local`](#local-fonts) or [`next/font/google`](#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example, you can apply fonts globally in your [Custom App](/docs/pages/building-your-application/routing/custom-app) (`pages/_app`):

```tsx filename="pages/_app.tsx" highlight={1,4-6,10} switcher
import { Geist } from 'next/font/google'
import type { AppProps } from 'next/app'

const geist = Geist({
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={geist.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

```jsx filename="pages/_app.js" highlight={1,3-5,9} switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={geist.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

</PagesOnly>

## Google fonts

You can automatically self-host any Google Font. Fonts are included stored as static assets and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.

To start using a Google Font, import your chosen font from `next/font/google`:

<AppOnly>

```tsx filename="app/layout.tsx" switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

</AppOnly>

<PagesOnly>

```tsx filename="pages/_app.tsx" switcher
import { Geist } from 'next/font/google'
import type { AppProps } from 'next/app'

const geist = Geist({
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={geist.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

```jsx filename="pages/_app.js" switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={geist.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

</PagesOnly>

We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility. But if you can't use a variable font, you will need to specify a weight:

<AppOnly>

```tsx filename="app/layout.tsx" highlight={4} switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js"  highlight={4} switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

</AppOnly>

<PagesOnly>

```tsx filename="pages/_app.tsx" highlight={5} switcher
import { Roboto } from 'next/font/google'
import type { AppProps } from 'next/app'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={roboto.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

```jsx filename="pages/_app.js" highlight={4} switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={roboto.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

</PagesOnly>

## Local fonts

<AppOnly>

To use a local font, import the `localFont` function from `next/font/local` and specify the [`src`](/docs/app/api-reference/components/font#src) of your local font file. The path is resolved relative to the file where `localFont` is called. Fonts can be stored anywhere in the project, including the [`public`](/docs/app/api-reference/file-conventions/public-folder) folder or co-located inside the `app` folder. For example, to use a font stored in `app/fonts/`:

```tsx filename="app/layout.tsx" switcher
import localFont from 'next/font/local'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import localFont from 'next/font/local'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
  )
}
```

</AppOnly>

<PagesOnly>

To use a local font, import your font from `next/font/local` and specify the [`src`](/docs/pages/api-reference/components/font#src) of your local font file. Fonts can be stored in the [`public`](/docs/pages/api-reference/file-conventions/public-folder) folder or inside the `pages` folder. For example:

```tsx filename="pages/_app.tsx" switcher
import localFont from 'next/font/local'
import type { AppProps } from 'next/app'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

```jsx filename="pages/_app.js" switcher
import localFont from 'next/font/local'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

</PagesOnly>

If you want to use multiple files for a single font family, `src` can be an array:

```js
const roboto = localFont({
  src: [
    {
      path: './Roboto-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './Roboto-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './Roboto-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './Roboto-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
})
```
Let me also check the route handler and proxy docs quickly.

Bash Check route handler and proxy docs
IN
cat "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/01-getting-started/15-route-handlers.md" | head -80 && echo "===PROXY===" && cat "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/node_modules/next/dist/docs/01-app/01-getting-started/16-proxy.md" | head -80

OUT
---
title: Route Handlers
nav_title: Route Handlers
description: Learn how to use Route Handlers
related:
  title: API Reference
  description: Learn more about Route Handlers
  links:
    - app/api-reference/file-conventions/route
    - app/guides/backend-for-frontend
---

## Route Handlers

Route Handlers allow you to create custom request handlers for a given route using the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs.

<Image
  alt="Route.js Special File"
  srcLight="/docs/light/route-special-file.png"
  srcDark="/docs/dark/route-special-file.png"
  width="1600"
  height="444"
/>

> **Good to know**: Route Handlers are only available inside the `app` directory. They are the equivalent of [API Routes](/docs/pages/building-your-application/routing/api-routes) inside the `pages` directory meaning you **do not** need to use API Routes and Route Handlers together.

### Convention

Route Handlers are defined in a [`route.js|ts` file](/docs/app/api-reference/file-conventions/route) inside the `app` directory:

```ts filename="app/api/route.ts" switcher
export async function GET(request: Request) {}
```

```js filename="app/api/route.js" switcher
export async function GET(request) {}
```

Route Handlers can be nested anywhere inside the `app` directory, similar to `page.js` and `layout.js`. But there **cannot** be a `route.js` file at the same route segment level as `page.js`.

### Supported HTTP Methods

The following [HTTP methods](https://developer.mozilla.org/docs/Web/HTTP/Methods) are supported: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS`. If an unsupported method is called, Next.js will return a `405 Method Not Allowed` response.

### Extended `NextRequest` and `NextResponse` APIs

In addition to supporting the native [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs, Next.js extends them with [`NextRequest`](/docs/app/api-reference/functions/next-request) and [`NextResponse`](/docs/app/api-reference/functions/next-response) to provide convenient helpers for advanced use cases.

### Caching

Route Handlers are not cached by default. You can, however, opt into caching for `GET` methods. Other supported HTTP methods are **not** cached. To cache a `GET` method, use a [route config option](/docs/app/guides/caching-without-cache-components#dynamic) such as `export const dynamic = 'force-static'` in your Route Handler file.

```ts filename="app/items/route.ts" switcher
export const dynamic = 'force-static'

export async function GET() {
  const res = await fetch('https://data.mongodb-api.com/...', {
    headers: {
      'Content-Type': 'application/json',
      'API-Key': process.env.DATA_API_KEY,
    },
  })
  const data = await res.json()

  return Response.json({ data })
}
```

```js filename="app/items/route.js" switcher
export const dynamic = 'force-static'

export async function GET() {
  const res = await fetch('https://data.mongodb-api.com/...', {
    headers: {
      'Content-Type': 'application/json',
      'API-Key': process.env.DATA_API_KEY,
    },
  })
  const data = await res.json()

===PROXY===
---
title: Proxy
nav_title: Proxy
description: Learn how to use Proxy
related:
  title: API Reference
  description: Learn more about Proxy
  links:
    - app/api-reference/file-conventions/proxy
    - app/guides/backend-for-frontend
---

## Proxy

> **Good to know**: Starting with Next.js 16, Middleware is now called Proxy to better reflect its purpose. The functionality remains the same.

Proxy allows you to run code before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.

### Use cases

Some common scenarios where Proxy is effective include:

- Modifying headers for all pages or a subset of pages
- Rewriting to different pages based on A/B tests or experiments
- Programmatic redirects based on incoming request properties

For simple redirects, consider using the [`redirects`](/docs/app/api-reference/config/next-config-js/redirects) configuration in `next.config.ts` first. Proxy should be used when you need access to request data or more complex logic.

Proxy is _not_ intended for slow data fetching. While Proxy can be helpful for [optimistic checks](/docs/app/guides/authentication#optimistic-checks-with-proxy-optional) such as permission-based redirects, it should not be used as a full session management or authorization solution.

Using fetch with `options.cache`, `options.next.revalidate`, or `options.next.tags`, has no effect in Proxy.

### Convention

Create a `proxy.ts` (or `.js`) file in the project root, or inside `src` if applicable, so that it is located at the same level as `pages` or `app`.

> **Note**: While only one `proxy.ts` file is supported per project, you can still organize your proxy logic into modules. Break out proxy functionalities into separate `.ts` or `.js` files and import them into your main `proxy.ts` file. This allows for cleaner management of route-specific proxy, aggregated in the `proxy.ts` for centralized control. By enforcing a single proxy file, it simplifies configuration, prevents potential conflicts, and optimizes performance by avoiding multiple proxy layers.

### Example

You can export your proxy function as either a default export or a named `proxy` export:

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

// This function can be marked `async` if using `await` inside
export function proxy(request: NextRequest) {
  return NextResponse.redirect(new URL('/home', request.url))
}

// Alternatively, you can use a default export:
// export default function proxy(request: NextRequest) { ... }

export const config = {
  matcher: '/about/:path*',
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

// This function can be marked `async` if using `await` inside
export function proxy(request) {
  return NextResponse.redirect(new URL('/home', request.url))
}

// Alternatively, you can use a default export:
// export default function proxy(request) { ... }

export const config = {
  matcher: '/about/:path*',
}
```

The `matcher` config allows you to filter Proxy to run on specific paths. See the [Matcher](/docs/app/api-reference/file-conventions/proxy#matcher) documentation for more details on path matching.

Read more about [using `proxy`](/docs/app/guides/backend-for-frontend#proxy), or refer to the `proxy` [API reference](/docs/app/api-reference/file-conventions/proxy).
Good — key findings: Tailwind v4 uses @import "tailwindcss" (no config file), and Middleware is renamed to proxy.ts. Now I'll build everything. Let me read the existing files first.

Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\app\layout.tsx
Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\app\page.tsx
Let me check the backend types to match them exactly.

Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\backend\app\main.py
Globpattern: "**/run_full_pipeline.py"
Found 1 file
Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\backend\scripts\run_full_pipeline.py
Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\backend\scripts\run_full_pipeline.py (lines 81-200)
Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\backend\scripts\run_full_pipeline.py (lines 201-300)
Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\backend\scripts\run_full_pipeline.py (lines 300-379)
Read c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\backend\scripts\run_full_pipeline.py (lines 377-416)
Now I have all the type info. Let me create the directory structure and write all files.

Update Todos

Scaffold Next.js app with TypeScript + Tailwind

Install extra dependencies (lucide-react, react-markdown, react-syntax-highlighter)

Set up design tokens and global CSS

Create TypeScript types for backend API response

Create API client and Next.js proxy route

Build layout components (AppShell, CivicHeader, SplitPane, BlackStarBg)

Build chat components (ChatContainer, MessageBubble, ChatInput, TypingIndicator, WelcomeScreen)

Build RAG inspection components (SourceCard, SimilarityBadge, PipelineTimeline, PromptViewer, SourceAccordion)

Build UI primitives (BallotGlassCard, GoldButton, Accordion, Skeleton, ScoreBar)

Build settings components (SettingsPanel, SliderInput, ModelSelector, BottomSheet)

Wire useChat hook and assemble app/page.tsx

Add .env.local and finalize next.config.ts
Bash Create component directory structure
Reason: dont write the files yet create, just answer if i should bundle into one app
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src" && mkdir -p components/layout components/chat components/rag components/ui components/settings hooks lib

My recommendation: deploy separately.

Here's the full picture:

Why separate works best for this project:

FastAPI is Python, Next.js is Node.js — they literally cannot run in a single process
"Bundling" means Docker Compose (two containers, one command) — which adds infra complexity you don't need for an exam project
The Next.js API proxy route I'll create (/api/query) means the browser never talks directly to FastAPI, so CORS is handled automatically
Deployment is just two free-tier services:
Service	Cost	Deploy method
Frontend	Vercel	Free	Push to GitHub → auto-deploys
Backend	Railway or Render	Free tier	Push to GitHub → auto-deploys
When bundling (Docker Compose) makes sense:

You're deploying to a single VPS/server (e.g., a uni server)
You want one docker-compose up to run everything locally for grading
You need to avoid two separate accounts/services
My actual recommendation for the exam: Deploy separately (Vercel + Railway) for the live demo, but also include a docker-compose.yml at the repo root so a marker can run everything locally with one command. Best of both worlds.

Should I proceed building the frontend now?

yes but doing it all at once isnt it too much why cant we do it in steps and amke sure you follow the ui spec document
Fair point. Let's go step by step. Here's the plan broken into clear phases — we'll do one phase, verify it looks right, then move on:

Phase	What we build
1 — Foundation	globals.css (design tokens + animations), layout.tsx (fonts), lib/types.ts, lib/api.ts, proxy route, .env.local
2 — UI Primitives	BallotGlassCard, GoldButton, Accordion, Skeleton, Badge, ScoreBar
3 — Layout Shell	BlackStarBg, CivicHeader, AppShell, BottomSheet
4 — Chat	WelcomeScreen, TypingIndicator, MessageBubble, ChatInput, ChatContainer
5 — RAG Inspection	SimilarityBadge, SourceCard, SourceList, PromptViewer, PipelineTimeline, SourceAccordion, InspectionPanel
6 — Settings	SliderInput, ModelSelector, SettingsPanel
7 — Wire Up	useChat, useMediaQuery, page.tsx — everything assembled and running
Starting Phase 1 — Foundation now. This sets up the design tokens, fonts, types, and API layer so every component we build after has everything it needs.

Update Todos

Phase 1: globals.css — design tokens, Tailwind theme, keyframe animations

Phase 1: layout.tsx — Inter + JetBrains Mono fonts, dark bg, metadata

Phase 1: lib/types.ts — TypeScript types matching backend response exactly

Phase 1: lib/api.ts — postQuery and healthCheck fetch wrappers

Phase 1: app/api/query/route.ts — Next.js proxy to FastAPI backend

Phase 1: .env.local — API_URL env var
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\app\globals.css
161 lines
@import "tailwindcss";

/* ─── Design Tokens ─────────────────────────────────────────── */
:root {
  /* Backgrounds */
  --bg-deep:     #0B0F1A;
  --bg-surface:  #111827;
  --bg-elevated: #1E293B;
  --bg-glass:    rgba(30, 41, 59, 0.55);

  /* Borders */
  --border-subtle: rgba(148, 163, 184, 0.12);
  --border-glass:  rgba(252, 209, 22, 0.08);

  /* Ghana flag accents */
  --ghana-gold:         #FCD116;
  --ghana-gold-muted:   #D4A017;
  --ghana-red:          #CE1126;
  --ghana-red-muted:    #A30E1F;
  --ghana-green:        #006B3F;
  --ghana-green-bright: #00895A;

  /* Text */
  --text-primary:   #F1F5F9;
  --text-secondary: #94A3B8;
  --text-muted:     #64748B;
  --text-gold:      #FCD116;

  /* Gradients */
  --gradient-brand:        linear-gradient(135deg, #CE1126 0%, #FCD116 50%, #006B3F 100%);
  --gradient-glow:         radial-gradient(ellipse at top, rgba(252, 209, 22, 0.10), transparent 60%);
  --gradient-score:        linear-gradient(90deg, #CE1126, #FCD116, #006B3F);
  --gradient-gold-shimmer: linear-gradient(90deg, #D4A017, #FCD116, #D4A017);
}

/* ─── Tailwind v4 Theme Mapping ──────────────────────────────── */
@theme inline {
  /* Map CSS vars → Tailwind color utilities */
  --color-bg-deep:          var(--bg-deep);
  --color-bg-surface:       var(--bg-surface);
  --color-bg-elevated:      var(--bg-elevated);
  --color-ghana-gold:       var(--ghana-gold);
  --color-ghana-gold-muted: var(--ghana-gold-muted);
  --color-ghana-red:        var(--ghana-red);
  --color-ghana-green:      var(--ghana-green);
  --color-ghana-green-bright: var(--ghana-green-bright);
  --color-text-primary:     var(--text-primary);
  --color-text-secondary:   var(--text-secondary);
  --color-text-muted:       var(--text-muted);

  /* Font family CSS vars injected by next/font into <html> */
  --font-sans: var(--font-inter);
  --font-mono: var(--font-jetbrains-mono);
}

/* ─── Base Styles ────────────────────────────────────────────── */
html {
  height: -webkit-fill-available;
  color-scheme: dark;
}

body {
  background-color: var(--bg-deep);
  background-image: var(--gradient-glow);
  color: var(--text-primary);
  font-family: var(--font-inter), system-ui, sans-serif;
  min-height: 100svh;
  min-height: -webkit-fill-available;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ─── Reusable Component Classes ─────────────────────────────── */

/* Ballot Box Glass — core glassmorphism card */
.ballot-glass {
  background: var(--bg-glass);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-glass);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  transition: border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow   0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.ballot-glass:hover {
  border-color: rgba(252, 209, 22, 0.18);
  box-shadow: 0 8px 32px rgba(252, 209, 22, 0.08);
}

/* Safe area padding for notched phones */
.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom, 16px);
}

/* Touch scroll on mobile */
.scroll-touch {
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
}

/* ─── Keyframe Animations ────────────────────────────────────── */

/* Message slide-in */
@keyframes slideIn {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Skeleton shimmer sweep */
@keyframes shimmer {
  from { background-position: -200% center; }
  to   { background-position:  200% center; }
}

/* Score badge pulse */
@keyframes badgePulse {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.05); }
}

/* Bottom sheet slide up */
@keyframes slideUp {
  from { transform: translateY(100%); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}

/* Bottom sheet backdrop fade */
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* Typing dot bounce */
@keyframes dotBounce {
  0%, 80%, 100% { transform: translateY(0); }
  40%           { transform: translateY(-6px); }
}

/* ─── Animation Utility Classes ──────────────────────────────── */
.animate-slide-in    { animation: slideIn    0.3s cubic-bezier(0.4, 0, 0.2, 1) both; }
.animate-slide-up    { animation: slideUp    0.35s cubic-bezier(0.4, 0, 0.2, 1) both; }
.animate-fade-in     { animation: fadeIn     0.35s ease both; }
.animate-badge-pulse { animation: badgePulse 0.5s ease both; }

.skeleton-shimmer {
  background: linear-gradient(
    90deg,
    var(--bg-elevated) 25%,
    rgba(252, 209, 22, 0.06) 50%,
    var(--bg-elevated) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.6s linear infinite;
}

/* Typing dots with staggered delay */
.dot-bounce { animation: dotBounce 1.2s ease-in-out infinite; }
.dot-bounce:nth-child(2) { animation-delay: 0.2s; }
.dot-bounce:nth-child(3) { animation-delay: 0.4s; }
Update Todos

Phase 1: globals.css — design tokens, Tailwind theme, keyframe animations

Phase 1: layout.tsx — Inter + JetBrains Mono fonts, dark bg, metadata

Phase 1: lib/types.ts — TypeScript types matching backend response exactly

Phase 1: lib/api.ts — postQuery and healthCheck fetch wrappers

Phase 1: app/api/query/route.ts — Next.js proxy to FastAPI backend

Phase 1: .env.local — API_URL env var
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\app\layout.tsx
41 lines
import type { Metadata, Viewport } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Ghana Civic RAG | ACity",
  description:
    "Academic City RAG Chatbot — retrieval-augmented question answering over Ghana civic documents.",
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#0B0F1A",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${jetbrainsMono.variable} h-full`}
    >
      <body className="min-h-svh flex flex-col antialiased">{children}</body>
    </html>
  );
}
Update Todos

Phase 1: globals.css — design tokens, Tailwind theme, keyframe animations

Phase 1: layout.tsx — Inter + JetBrains Mono fonts, dark bg, metadata

Phase 1: lib/types.ts — TypeScript types matching backend response exactly

Phase 1: lib/api.ts — postQuery and healthCheck fetch wrappers

Phase 1: app/api/query/route.ts — Next.js proxy to FastAPI backend

Phase 1: .env.local — API_URL env var
Bash Create lib and API route directories
IN
mkdir -p "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/lib" && mkdir -p "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/app/api/query"

OUT
(Bash completed with no output)
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\lib\types.ts
103 lines
/* ── Request ──────────────────────────────────────────────────── */

export interface QueryRequest {
  query: string;
  top_k?: number;           // 1–20, default 5
  hybrid_alpha?: number;    // 0.0–1.0, default 0.55
  llm_model?: string;       // default "gpt-4o-mini"
  max_context_tokens?: number; // 200–4000, default 1200
}

/* ── Response sub-shapes (matching run_full_pipeline.py output) ─ */

export interface SimilarityScores {
  vector_score: number;
  keyword_score: number;
  hybrid_score: number;
}

export interface RetrievedDocument {
  rank: number;
  chunk_id: string;
  source: string;
  doc_id: string;
  similarity_scores: SimilarityScores;
  text_preview: string;     // first 300 chars of the chunk
}

export interface SelectedChunk {
  rank: number;
  chunk_id: string;
  source: string;
  doc_id: string;
  vector_score: number;
  keyword_score: number;
  hybrid_score: number;
  used_tokens: number;
  truncated: boolean;
}

export interface ContextSelection {
  used_context_tokens: number;
  selected_chunks: SelectedChunk[];
}

/* ISO-8601 timestamps for each pipeline stage */
export interface StageTimes {
  retrieval_start: string;
  retrieval_end: string;
  context_selection_start: string;
  context_selection_end: string;
  prompt_construction_start: string;
  prompt_construction_end: string;
  llm_generation_start: string;
  llm_generation_end: string;
}

/* ── Full API response ────────────────────────────────────────── */

export interface QueryResponse {
  run_id: string;
  query: string;
  retrieved_documents: RetrievedDocument[];
  context_selection: ContextSelection;
  final_prompt_sent_to_llm: string;
  response: string;
  stage_times: StageTimes;
  run_log_path: string;
}

/* ── Chat message (local UI state, not from backend) ─────────── */

export type MessageRole = "user" | "assistant";

export interface ChatMessage {
  id: string;
  role: MessageRole;
  content: string;
  ragData?: QueryResponse;  // only on assistant messages
  timestamp: Date;
}

/* ── Settings (local UI state) ───────────────────────────────── */

export interface ChatSettings {
  top_k: number;
  hybrid_alpha: number;
  llm_model: string;
  max_context_tokens: number;
}

export const DEFAULT_SETTINGS: ChatSettings = {
  top_k: 5,
  hybrid_alpha: 0.55,
  llm_model: "gpt-4o-mini",
  max_context_tokens: 1200,
};

export const LLM_MODELS = [
  { value: "gpt-4o-mini", label: "GPT-4o Mini" },
  { value: "gpt-4o",      label: "GPT-4o" },
  { value: "gpt-4-turbo", label: "GPT-4 Turbo" },
];
Update Todos

Phase 1: globals.css — design tokens, Tailwind theme, keyframe animations

Phase 1: layout.tsx — Inter + JetBrains Mono fonts, dark bg, metadata

Phase 1: lib/types.ts — TypeScript types matching backend response exactly

Phase 1: lib/api.ts — postQuery and healthCheck fetch wrappers

Phase 1: app/api/query/route.ts — Next.js proxy to FastAPI backend

Phase 1: .env.local — API_URL env var
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\lib\api.ts
42 lines
import type { QueryRequest, QueryResponse } from "./types";

/* All requests go through the Next.js proxy route to avoid CORS */
const PROXY = "/api/query";

export async function postQuery(req: QueryRequest): Promise<QueryResponse> {
  const res = await fetch(PROXY, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(req),
  });

  if (!res.ok) {
    const detail = await res.text().catch(() => res.statusText);
    throw new Error(detail || `HTTP ${res.status}`);
  }

  return res.json() as Promise<QueryResponse>;
}

export async function healthCheck(): Promise<boolean> {
  try {
    const res = await fetch("/api/health", { method: "GET" });
    return res.ok;
  } catch {
    return false;
  }
}

/* Derive human-readable ms durations from stage_times ISO strings */
export function parseStageDurations(stageTimes: QueryResponse["stage_times"]) {
  const ms = (start: string, end: string) =>
    Math.round(new Date(end).getTime() - new Date(start).getTime());

  return [
    { label: "Retrieval",          ms: ms(stageTimes.retrieval_start,           stageTimes.retrieval_end) },
    { label: "Context selection",  ms: ms(stageTimes.context_selection_start,   stageTimes.context_selection_end) },
    { label: "Prompt construction",ms: ms(stageTimes.prompt_construction_start, stageTimes.prompt_construction_end) },
    { label: "LLM generation",     ms: ms(stageTimes.llm_generation_start,      stageTimes.llm_generation_end) },
  ];
}
Update Todos

Phase 1: globals.css — design tokens, Tailwind theme, keyframe animations

Phase 1: layout.tsx — Inter + JetBrains Mono fonts, dark bg, metadata

Phase 1: lib/types.ts — TypeScript types matching backend response exactly

Phase 1: lib/api.ts — postQuery and healthCheck fetch wrappers

Phase 1: app/api/query/route.ts — Next.js proxy to FastAPI backend

Phase 1: .env.local — API_URL env var
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\app\api\query\route.ts
17 lines
import type { NextRequest } from "next/server";

const BACKEND = process.env.API_URL ?? "http://localhost:8000";

export async function POST(request: NextRequest) {
  const body = await request.json();

  const upstream = await fetch(`${BACKEND}/query`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  const data = await upstream.json();
  return Response.json(data, { status: upstream.status });
}
Also need a health proxy route:

Bash Create health API route directory
IN
mkdir -p "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/app/api/health"

OUT
(Bash completed with no output)
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\app\api\health\route.ts
12 lines
const BACKEND = process.env.API_URL ?? "http://localhost:8000";

export async function GET() {
  try {
    const upstream = await fetch(`${BACKEND}/health`, { method: "GET" });
    const data = await upstream.json();
    return Response.json(data, { status: upstream.status });
  } catch {
    return Response.json({ status: "unavailable" }, { status: 503 });
  }
}
Update Todos

Phase 1: globals.css — design tokens, Tailwind theme, keyframe animations

Phase 1: layout.tsx — Inter + JetBrains Mono fonts, dark bg, metadata

Phase 1: lib/types.ts — TypeScript types matching backend response exactly

Phase 1: lib/api.ts — postQuery and healthCheck fetch wrappers

Phase 1: app/api/query/route.ts — Next.js proxy to FastAPI backend

Phase 1: .env.local — API_URL env var
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\.env.local
4 lines
# URL of the running FastAPI backend
# Change this to your Railway/Render URL when deploying
API_URL=http://localhost:8000
Now let's verify the build compiles cleanly with no errors.

Bash TypeScript type-check the project
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app" && npx tsc --noEmit 2>&1

OUT
(Bash completed with no output)
Update Todos

Phase 1: globals.css — design tokens, Tailwind theme, keyframe animations

Phase 1: layout.tsx — Inter + JetBrains Mono fonts, dark bg, metadata

Phase 1: lib/types.ts — TypeScript types matching backend response exactly

Phase 1: lib/api.ts — postQuery and healthCheck fetch wrappers

Phase 1: app/api/query/route.ts — Next.js proxy to FastAPI backend

Phase 1: .env.local — API_URL env var
Phase 1 complete. TypeScript check passed with zero errors. Here's what was built:

File	What it does
globals.css	All design tokens as CSS vars, Tailwind v4 theme mapping, ballot-glass, all keyframes (slideIn, shimmer, dotBounce, slideUp, fadeIn, badgePulse)
layout.tsx	Root layout — Inter + JetBrains Mono via next/font, themeColor, min-h-svh, iOS fill-available
lib/types.ts	TypeScript types matching the backend exactly — QueryResponse, RetrievedDocument, SimilarityScores, StageTimes, ChatMessage, ChatSettings
lib/api.ts	postQuery(), healthCheck(), and parseStageDurations() helper
app/api/query/route.ts	Next.js proxy → FastAPI /query
app/api/health/route.ts	Next.js proxy → FastAPI /health
.env.local	API_URL=http://localhost:8000
Ready for Phase 2 — UI Primitives (BallotGlassCard, GoldButton, Accordion, Skeleton, Badge, ScoreBar)? Say the word.

yes phase 2
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Bash Create UI components directory
IN
mkdir -p "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/components/ui"

OUT
(Bash completed with no output)
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\ui\BallotGlassCard.tsx
27 lines
import { HTMLAttributes } from "react";

interface Props extends HTMLAttributes<HTMLDivElement> {
  /** Remove the hover glow effect (e.g. for static display cards) */
  noHover?: boolean;
}

/**
 * "Transparent Ballot Box Glass" — the base glassmorphism surface used
 * throughout the UI as a metaphor for civic transparency.
 */
export default function BallotGlassCard({
  children,
  className = "",
  noHover = false,
  ...rest
}: Props) {
  return (
    <div
      className={`ballot-glass ${noHover ? "hover:border-[rgba(252,209,22,0.08)] hover:shadow-none" : ""} ${className}`}
      {...rest}
    >
      {children}
    </div>
  );
}
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\ui\Badge.tsx
37 lines
import { HTMLAttributes } from "react";

type Variant = "gold" | "green" | "red" | "muted";

interface Props extends HTMLAttributes<HTMLSpanElement> {
  variant?: Variant;
}

const variantClasses: Record<Variant, string> = {
  gold:  "bg-[rgba(252,209,22,0.15)]  text-ghana-gold        border-[rgba(252,209,22,0.2)]",
  green: "bg-[rgba(0,107,63,0.18)]    text-ghana-green-bright border-[rgba(0,107,63,0.25)]",
  red:   "bg-[rgba(206,17,38,0.15)]   text-ghana-red          border-[rgba(206,17,38,0.2)]",
  muted: "bg-[rgba(148,163,184,0.1)]  text-text-secondary      border-[rgba(148,163,184,0.15)]",
};

export default function Badge({
  children,
  variant = "muted",
  className = "",
  ...rest
}: Props) {
  return (
    <span
      className={`
        inline-flex items-center gap-1
        px-2 py-0.5 rounded-full
        border text-[10px] sm:text-[11px] font-semibold
        ${variantClasses[variant]}
        ${className}
      `}
      {...rest}
    >
      {children}
    </span>
  );
}
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\ui\GoldButton.tsx
42 lines
import { ButtonHTMLAttributes } from "react";

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Show a non-interactive icon-only variant (square, rounded-xl) */
  icon?: boolean;
}

/**
 * Primary action button — Ghana gold gradient.
 * Minimum 44×44px touch target on all screen sizes.
 */
export default function GoldButton({
  children,
  icon = false,
  className = "",
  disabled,
  ...rest
}: Props) {
  return (
    <button
      disabled={disabled}
      className={`
        inline-flex items-center justify-center gap-2
        bg-gradient-to-br from-[#D4A017] to-[#FCD116]
        text-[#0B0F1A] font-semibold
        transition-transform duration-200
        active:scale-95
        disabled:opacity-40 disabled:cursor-not-allowed disabled:active:scale-100
        focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/60
        ${icon
          ? "min-w-[44px] min-h-[44px] rounded-xl text-sm"
          : "min-h-[44px] px-5 py-2.5 rounded-2xl text-sm sm:text-base"
        }
        ${className}
      `}
      {...rest}
    >
      {children}
    </button>
  );
}
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\ui\Skeleton.tsx
51 lines
import { HTMLAttributes } from "react";

interface Props extends HTMLAttributes<HTMLDivElement> {
  /** Height class e.g. "h-4", "h-6". Defaults to "h-4". */
  height?: string;
  /** Width class e.g. "w-full", "w-32". Defaults to "w-full". */
  width?: string;
  /** Fully rounded pill shape */
  pill?: boolean;
}

/**
 * Gold shimmer loading skeleton.
 * Uses the `skeleton-shimmer` animation defined in globals.css.
 */
export default function Skeleton({
  height = "h-4",
  width = "w-full",
  pill = false,
  className = "",
  ...rest
}: Props) {
  return (
    <div
      aria-hidden="true"
      className={`
        skeleton-shimmer
        ${height} ${width}
        ${pill ? "rounded-full" : "rounded-lg"}
        ${className}
      `}
      {...rest}
    />
  );
}

/** Convenience: stack of skeleton lines that mimic a text block */
export function SkeletonText({ lines = 3 }: { lines?: number }) {
  return (
    <div className="space-y-2">
      {Array.from({ length: lines }).map((_, i) => (
        <Skeleton
          key={i}
          height="h-3"
          width={i === lines - 1 ? "w-3/4" : "w-full"}
        />
      ))}
    </div>
  );
}
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\ui\Accordion.tsx
94 lines
"use client";

import { useState, useRef, useEffect, ReactNode } from "react";
import { ChevronDown } from "lucide-react";

interface Props {
  title: ReactNode;
  children: ReactNode;
  /** Start open */
  defaultOpen?: boolean;
  /** Gold chevron tint (default) or muted */
  accent?: "gold" | "muted";
  className?: string;
}

/**
 * Expandable section with smooth height transition and rotating chevron.
 * Used heavily on mobile to reveal RAG inspection data under each response.
 * Transition: 250ms cubic-bezier as specified in the design blueprint.
 */
export default function Accordion({
  title,
  children,
  defaultOpen = false,
  accent = "gold",
  className = "",
}: Props) {
  const [open, setOpen] = useState(defaultOpen);
  const bodyRef = useRef<HTMLDivElement>(null);
  const [height, setHeight] = useState<string>(defaultOpen ? "auto" : "0px");

  useEffect(() => {
    if (!bodyRef.current) return;
    if (open) {
      // measure then animate to exact height, then switch to "auto"
      const h = bodyRef.current.scrollHeight;
      setHeight(`${h}px`);
      const timer = setTimeout(() => setHeight("auto"), 260);
      return () => clearTimeout(timer);
    } else {
      // snapshot current height before collapsing
      const h = bodyRef.current.scrollHeight;
      setHeight(`${h}px`);
      // force a reflow so the transition fires
      bodyRef.current.getBoundingClientRect();
      requestAnimationFrame(() => setHeight("0px"));
    }
  }, [open]);

  const chevronColor =
    accent === "gold" ? "text-ghana-gold" : "text-text-muted";

  return (
    <div className={`w-full ${className}`}>
      {/* Trigger — full-width, minimum 44px touch target */}
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className={`
          flex w-full items-center justify-between
          min-h-[44px] px-4 py-2.5
          text-left text-sm font-medium text-text-primary
          hover:text-ghana-gold transition-colors duration-200
          focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
        `}
        aria-expanded={open}
      >
        <span>{title}</span>
        <ChevronDown
          size={16}
          className={`
            shrink-0 transition-transform duration-[250ms] cubic-bezier(0.4,0,0.2,1)
            ${chevronColor}
            ${open ? "rotate-180" : "rotate-0"}
          `}
        />
      </button>

      {/* Collapsible body */}
      <div
        ref={bodyRef}
        style={{
          height,
          overflow: "hidden",
          transition: "height 250ms cubic-bezier(0.4, 0, 0.2, 1)",
        }}
        aria-hidden={!open}
      >
        <div className="px-4 pb-3">{children}</div>
      </div>
    </div>
  );
}
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\ui\ScoreBar.tsx
60 lines
"use client";

import { useEffect, useRef, useState } from "react";

interface Props {
  /** Score value from 0.0 to 1.0 */
  score: number;
  /** Show the numeric label at the right end */
  showLabel?: boolean;
  className?: string;
}

/**
 * Animated progress bar mapping the Ghana flag spectrum:
 * Red (low) → Gold (medium) → Green (high), matching the score range.
 * Animates from 0 to the target width on mount.
 */
export default function ScoreBar({ score, showLabel = true, className = "" }: Props) {
  const clampedScore = Math.max(0, Math.min(1, score));
  const pct = Math.round(clampedScore * 100);

  const [width, setWidth] = useState(0);
  const rafRef = useRef<number | null>(null);

  useEffect(() => {
    // Animate to target on mount
    rafRef.current = requestAnimationFrame(() => {
      setWidth(pct);
    });
    return () => {
      if (rafRef.current !== null) cancelAnimationFrame(rafRef.current);
    };
  }, [pct]);

  return (
    <div className={`flex items-center gap-2 ${className}`}>
      {/* Track */}
      <div className="flex-1 h-1.5 rounded-full bg-[var(--bg-elevated)] overflow-hidden">
        <div
          style={{
            width: `${width}%`,
            transition: "width 600ms cubic-bezier(0.4, 0, 0.2, 1)",
            background: "var(--gradient-score)",
            backgroundSize: "200% 100%",
            backgroundPosition: `${100 - pct}% center`,
          }}
          className="h-full rounded-full"
        />
      </div>

      {/* Numeric label */}
      {showLabel && (
        <span className="text-[10px] font-mono font-semibold w-8 text-right shrink-0 text-text-secondary">
          {clampedScore.toFixed(2)}
        </span>
      )}
    </div>
  );
}
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Bash TypeScript check all Phase 2 components
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app" && npx tsc --noEmit 2>&1

OUT
(Bash completed with no output)
Update Todos

Phase 2: BallotGlassCard — glassmorphism card wrapper

Phase 2: Badge — Ghana-colour label variants

Phase 2: GoldButton — primary CTA, 44px touch target, active:scale-95

Phase 2: Skeleton — gold shimmer loading placeholder

Phase 2: Accordion — expandable section, chevron rotate, 250ms height transition

Phase 2: ScoreBar — Red→Gold→Green animated progress bar

Phase 2: TypeScript check — verify zero errors
Phase 2 complete. Zero TypeScript errors. Here's what was built:

File	Key spec details
BallotGlassCard.tsx	Uses .ballot-glass from globals.css — backdrop-blur, gold-tinted border, hover glow
Badge.tsx	gold / green / red / muted variants using exact Ghana hex values from spec
GoldButton.tsx	from-[#D4A017] to-[#FCD116] gradient, min-h-[44px] touch target, active:scale-95, icon prop for square variant
Skeleton.tsx	skeleton-shimmer animation from globals.css + SkeletonText convenience component
Accordion.tsx	useState + scrollHeight measurement → smooth height transition at exactly 250ms, chevron rotates 180°, 44px touch target
ScoreBar.tsx	Animates from 0→score on mount via requestAnimationFrame, uses --gradient-score (Red→Gold→Green), 600ms ease
Ready for Phase 3 — Layout Shell (BlackStarBg, CivicHeader, AppShell, BottomSheet)?

phase 3 also the logo and icon are in frontend folder
Good catch. Let me copy the assets into the Next.js public folder first, then build Phase 3.

Bash Check source assets and public folder contents
IN
ls "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/" && ls "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/public/"

OUT
Navbar_icon.png
logo.png
ui_design_blueprint.md
file.svg
globe.svg
next.svg
vercel.svg
window.svg
Bash Copy logo and navbar icon to Next.js public folder
IN
cp "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/logo.png" "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/public/logo.png" && cp "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend/Navbar_icon.png" "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/public/navbar-icon.png" && echo "Copied"

OUT
Copied
Assets are in. Now building Phase 3.

Update Todos

Phase 3: BlackStarBg — SVG star watermark, opacity 0.03–0.05, aria-hidden

Phase 3: CivicHeader — full text on desktop, icon-only on mobile, logo + title

Phase 3: BottomSheet — mobile slide-up panel with backdrop, 350ms

Phase 3: AppShell — single-col mobile / 55-45 split desktop, assembles header + panels

Phase 3: TypeScript check — verify zero errors
Bash Create layout components directory
IN
mkdir -p "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/components/layout"

OUT
(Bash completed with no output)
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\layout\BlackStarBg.tsx
26 lines
/**
 * The Black Star of Africa — a large, subtle SVG star watermark placed
 * behind all page content. Opacity 0.04 keeps it barely perceptible,
 * reinforcing the "Ghana Civic Premium" identity without distracting.
 * aria-hidden so screen readers skip it entirely.
 */
export default function BlackStarBg() {
  return (
    <div
      aria-hidden="true"
      className="pointer-events-none fixed inset-0 z-0 flex items-center justify-center overflow-hidden"
    >
      <svg
        viewBox="0 0 200 200"
        className="w-[min(80vw,80vh)] h-[min(80vw,80vh)]"
        style={{ opacity: 0.04 }}
        fill="white"
        xmlns="http://www.w3.org/2000/svg"
      >
        {/* Five-pointed star — the Black Star of Ghana's national flag */}
        <polygon points="100,10 120.6,73.5 186.6,73.5 134.4,110.3 155,173.8 100,137 45,173.8 65.6,110.3 13.4,73.5 79.4,73.5" />
      </svg>
    </div>
  );
}
Update Todos

Phase 3: BlackStarBg — SVG star watermark, opacity 0.03–0.05, aria-hidden

Phase 3: CivicHeader — full text on desktop, icon-only on mobile, logo + title

Phase 3: BottomSheet — mobile slide-up panel with backdrop, 350ms

Phase 3: AppShell — single-col mobile / 55-45 split desktop, assembles header + panels

Phase 3: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\layout\CivicHeader.tsx
104 lines
"use client";

import Image from "next/image";
import { Settings } from "lucide-react";

interface Props {
  onSettingsOpen: () => void;
}

/**
 * Top header bar.
 *
 * Mobile  (<lg): logo icon only + abbreviated title + icon buttons
 * Desktop (lg+): full logo + full title + labelled settings button
 *
 * The Ghana tricolour gradient is applied to the bottom border to
 * reinforce brand identity without overwhelming the dark surface.
 */
export default function CivicHeader({ onSettingsOpen }: Props) {
  return (
    <header
      className="
        relative z-20
        flex items-center justify-between
        px-4 lg:px-6
        h-14 lg:h-16
        bg-[var(--bg-surface)]/80 backdrop-blur-md
        border-b border-[var(--border-subtle)]
        shrink-0
      "
    >
      {/* Ghana tricolour accent line across the bottom of the header */}
      <div
        className="absolute bottom-0 left-0 right-0 h-[2px]"
        style={{ background: "var(--gradient-brand)" }}
      />

      {/* ── Left: brand ── */}
      <div className="flex items-center gap-3">
        {/* Navbar icon — always visible */}
        <div className="relative w-8 h-8 lg:w-9 lg:h-9 shrink-0">
          <Image
            src="/navbar-icon.png"
            alt="Ghana Civic RAG icon"
            fill
            className="object-contain"
            priority
          />
        </div>

        {/* Full logo — hidden on small screens to save space */}
        <div className="hidden sm:block relative w-24 h-8 lg:w-28 lg:h-9 shrink-0">
          <Image
            src="/logo.png"
            alt="Ghana Civic RAG logo"
            fill
            className="object-contain object-left"
            priority
          />
        </div>

        {/* Title text */}
        <div className="flex flex-col leading-tight">
          {/* Short form on mobile, full form on desktop */}
          <span
            className="
              text-text-primary font-extrabold uppercase tracking-widest
              text-[11px] sm:text-[13px] lg:text-sm
            "
          >
            <span className="lg:hidden">GH Civic RAG</span>
            <span className="hidden lg:inline">Ghana Civic RAG</span>
          </span>
          <span className="text-[9px] sm:text-[10px] text-text-muted font-medium tracking-wider uppercase">
            ACity · CS4241
          </span>
        </div>
      </div>

      {/* ── Right: actions ── */}
      <div className="flex items-center gap-2">
        {/* Settings button — icon only on mobile, labelled on desktop */}
        <button
          type="button"
          onClick={onSettingsOpen}
          aria-label="Open settings"
          className="
            flex items-center gap-1.5
            min-w-[44px] min-h-[44px] px-3
            rounded-xl text-text-secondary
            hover:text-ghana-gold hover:bg-[var(--bg-elevated)]
            active:scale-95
            transition-all duration-200
            focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
          "
        >
          <Settings size={18} />
          <span className="hidden lg:inline text-sm font-medium">Settings</span>
        </button>
      </div>
    </header>
  );
}
Update Todos

Phase 3: BlackStarBg — SVG star watermark, opacity 0.03–0.05, aria-hidden

Phase 3: CivicHeader — full text on desktop, icon-only on mobile, logo + title

Phase 3: BottomSheet — mobile slide-up panel with backdrop, 350ms

Phase 3: AppShell — single-col mobile / 55-45 split desktop, assembles header + panels

Phase 3: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\layout\BottomSheet.tsx
108 lines
"use client";

import { useEffect, useRef, ReactNode } from "react";
import { X } from "lucide-react";

interface Props {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: ReactNode;
}

/**
 * Mobile slide-up bottom sheet.
 *
 * - Slides in from bottom in 350ms (spec requirement)
 * - Backdrop fades in simultaneously
 * - Locks body scroll while open
 * - Closes on backdrop click or the × button
 * - On desktop (lg+) renders as a fixed right-side panel instead
 */
export default function BottomSheet({ isOpen, onClose, title, children }: Props) {
  const sheetRef = useRef<HTMLDivElement>(null);

  // Lock body scroll when open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => { document.body.style.overflow = ""; };
  }, [isOpen]);

  // Close on Escape
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape" && isOpen) onClose();
    };
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <>
      {/* Backdrop */}
      <div
        className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm animate-fade-in"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Sheet — slides up from bottom on mobile, panel from right on desktop */}
      <div
        ref={sheetRef}
        role="dialog"
        aria-modal="true"
        aria-label={title}
        className="
          fixed z-50 flex flex-col
          bg-[var(--bg-surface)] border-t border-[var(--border-glass)]

          /* Mobile: full-width panel from bottom, max 85vh */
          bottom-0 left-0 right-0
          max-h-[85dvh] rounded-t-2xl
          animate-slide-up

          /* Desktop: right sidebar */
          lg:bottom-0 lg:top-0 lg:left-auto lg:right-0
          lg:w-80 lg:max-h-none lg:rounded-none lg:rounded-l-2xl
          lg:border-t-0 lg:border-l
          lg:animate-none
        "
      >
        {/* Handle bar (mobile only) */}
        <div className="flex justify-center pt-3 pb-1 lg:hidden">
          <div className="w-10 h-1 rounded-full bg-[var(--border-subtle)]" />
        </div>

        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-[var(--border-subtle)] shrink-0">
          <h2 className="text-base font-semibold text-text-primary">{title}</h2>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close"
            className="
              min-w-[44px] min-h-[44px] flex items-center justify-center
              text-text-muted hover:text-ghana-gold rounded-xl
              active:scale-95 transition-all duration-150
              focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
            "
          >
            <X size={20} />
          </button>
        </div>

        {/* Content — scrollable */}
        <div className="flex-1 overflow-y-auto scroll-touch px-5 py-4 safe-area-bottom">
          {children}
        </div>
      </div>
    </>
  );
}
Update Todos

Phase 3: BlackStarBg — SVG star watermark, opacity 0.03–0.05, aria-hidden

Phase 3: CivicHeader — full text on desktop, icon-only on mobile, logo + title

Phase 3: BottomSheet — mobile slide-up panel with backdrop, 350ms

Phase 3: AppShell — single-col mobile / 55-45 split desktop, assembles header + panels

Phase 3: TypeScript check — verify zero errors
AppShell is the core responsive container — it wires header + split pane + bottom sheet slot together. It takes the chat panel and inspection panel as props so Phase 4 and 5 can slot in cleanly.

Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\layout\AppShell.tsx
85 lines
"use client";

import { useState, ReactNode } from "react";
import BlackStarBg from "./BlackStarBg";
import CivicHeader from "./CivicHeader";
import BottomSheet from "./BottomSheet";

interface Props {
  /** Left / main panel — takes 55% on desktop, 100% on mobile */
  chatPanel: ReactNode;
  /**
   * Right panel — 45% on desktop only.
   * On mobile this content is surfaced inside accordions in the chat panel,
   * so this prop can be null on mobile-only renders.
   */
  inspectionPanel: ReactNode;
  /** Content rendered inside the Settings bottom sheet / sidebar */
  settingsContent: ReactNode;
}

/**
 * Root responsive shell.
 *
 * Mobile  (<lg): single-column, header + full-width chat (input fixed to bottom)
 * Desktop (lg+): header + 55/45 side-by-side split, both panels scroll independently
 *
 * The BlackStarBg watermark sits behind everything via fixed positioning.
 */
export default function AppShell({ chatPanel, inspectionPanel, settingsContent }: Props) {
  const [settingsOpen, setSettingsOpen] = useState(false);

  return (
    <div className="relative flex flex-col min-h-svh bg-bg-deep">
      {/* Watermark behind all content */}
      <BlackStarBg />

      {/* Header — fixed height, shrinks on mobile */}
      <CivicHeader onSettingsOpen={() => setSettingsOpen(true)} />

      {/*
        Main content area — fills remaining viewport height.
        Mobile:  single column, chat fills everything.
        Desktop: flex-row, chat 55% | inspection 45%.
      */}
      <main className="relative z-10 flex flex-1 overflow-hidden">

        {/* ── Chat panel ─────────────────────────────────────── */}
        <section
          aria-label="Chat"
          className="
            flex flex-col
            w-full lg:w-[55%]
            min-h-0 overflow-hidden
          "
        >
          {chatPanel}
        </section>

        {/* ── Inspection panel (desktop only) ────────────────── */}
        <aside
          aria-label="RAG Inspection"
          className="
            hidden lg:flex flex-col
            w-[45%]
            min-h-0 overflow-y-auto scroll-touch
            border-l border-[var(--border-subtle)]
            bg-[var(--bg-surface)]/40
          "
        >
          {inspectionPanel}
        </aside>
      </main>

      {/* Settings bottom sheet (mobile) / sidebar (desktop) */}
      <BottomSheet
        isOpen={settingsOpen}
        onClose={() => setSettingsOpen(false)}
        title="Settings"
      >
        {settingsContent}
      </BottomSheet>
    </div>
  );
}
Update Todos

Phase 3: BlackStarBg — SVG star watermark, opacity 0.03–0.05, aria-hidden

Phase 3: CivicHeader — full text on desktop, icon-only on mobile, logo + title

Phase 3: BottomSheet — mobile slide-up panel with backdrop, 350ms

Phase 3: AppShell — single-col mobile / 55-45 split desktop, assembles header + panels

Phase 3: TypeScript check — verify zero errors
Bash TypeScript check all Phase 3 components
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app" && npx tsc --noEmit 2>&1

OUT
(Bash completed with no output)
Update Todos

Phase 3: BlackStarBg — SVG star watermark, opacity 0.03–0.05, aria-hidden

Phase 3: CivicHeader — full text on desktop, icon-only on mobile, logo + title

Phase 3: BottomSheet — mobile slide-up panel with backdrop, 350ms

Phase 3: AppShell — single-col mobile / 55-45 split desktop, assembles header + panels

Phase 3: TypeScript check — verify zero errors
Phase 3 complete. Zero TypeScript errors. Here's what was built:

File	Key details
BlackStarBg.tsx	fixed inset-0 z-0, five-pointed star SVG at opacity: 0.04, pointer-events-none, aria-hidden
CivicHeader.tsx	Uses both /logo.png and /navbar-icon.png — navbar icon always visible, full logo hides on <sm. Ghana tricolour 2px line at bottom. Full "Ghana Civic RAG" text on lg+, "GH Civic RAG" on mobile
BottomSheet.tsx	animate-slide-up (350ms spec), backdrop fade, body scroll lock, Escape key close, drag handle bar. Becomes a right sidebar on lg+
AppShell.tsx	Accepts chatPanel, inspectionPanel, settingsContent as props. Mobile = single column. Desktop = w-[55%] chat + w-[45%] inspection side-by-side, both scroll independently
Ready for Phase 4 — Chat components (WelcomeScreen, TypingIndicator, MessageBubble, ChatInput, ChatContainer)?

phase 4
Update Todos

Phase 4: WelcomeScreen — hero with Black Star gradient, suggested questions

Phase 4: TypingIndicator — 3 gold bouncing dots, staggered delays

Phase 4: MessageBubble — user gold gradient / bot glass, slide-in, mobileInspection slot

Phase 4: ChatInput — auto-resize textarea, fixed bottom mobile, Enter to send

Phase 4: ChatContainer — scrollable list, auto-scroll, WelcomeScreen when empty

Phase 4: TypeScript check — verify zero errors
Bash Create chat components directory
IN
mkdir -p "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/components/chat"

OUT
(Bash completed with no output)
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\chat\WelcomeScreen.tsx
79 lines
interface Props {
  onSuggestion: (text: string) => void;
}

const SUGGESTIONS = [
  "What were the results of the 2020 Ghana presidential election?",
  "Summarise Ghana's 2023 national budget highlights.",
  "Who won the parliamentary seat in Ablekuma North?",
  "What is Ghana's fiscal deficit target for 2024?",
];

/**
 * Hero welcome screen shown when the chat history is empty.
 * Features the Ghana tricolour gradient headline and suggested queries.
 */
export default function WelcomeScreen({ onSuggestion }: Props) {
  return (
    <div className="flex flex-col items-center justify-center flex-1 px-6 py-12 text-center">
      {/* Star + title */}
      <div className="mb-6 flex flex-col items-center gap-4">
        {/* Mini Black Star */}
        <svg
          viewBox="0 0 200 200"
          className="w-16 h-16 opacity-80"
          aria-hidden="true"
        >
          <defs>
            <linearGradient id="star-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%"   stopColor="#CE1126" />
              <stop offset="50%"  stopColor="#FCD116" />
              <stop offset="100%" stopColor="#006B3F" />
            </linearGradient>
          </defs>
          <polygon
            fill="url(#star-grad)"
            points="100,10 120.6,73.5 186.6,73.5 134.4,110.3 155,173.8 100,137 45,173.8 65.6,110.3 13.4,73.5 79.4,73.5"
          />
        </svg>

        <h1
          className="text-2xl sm:text-3xl font-extrabold uppercase tracking-widest"
          style={{ background: "var(--gradient-brand)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}
        >
          Ghana Civic RAG
        </h1>

        <p className="max-w-sm text-sm sm:text-base text-text-secondary leading-relaxed">
          Ask anything about Ghana&apos;s electoral results or national budget.
          Answers are grounded in retrieved documents with full source citations.
        </p>
      </div>

      {/* Suggested queries */}
      <div className="w-full max-w-lg flex flex-col gap-2.5">
        <p className="text-xs font-semibold uppercase tracking-wider text-text-muted mb-1">
          Try asking
        </p>
        {SUGGESTIONS.map((s) => (
          <button
            key={s}
            type="button"
            onClick={() => onSuggestion(s)}
            className="
              w-full text-left text-sm text-text-secondary
              ballot-glass px-4 py-3 rounded-xl
              hover:text-ghana-gold hover:border-[rgba(252,209,22,0.18)]
              active:scale-[0.98]
              transition-all duration-200
              focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
            "
          >
            {s}
          </button>
        ))}
      </div>
    </div>
  );
}
Update Todos

Phase 4: WelcomeScreen — hero with Black Star gradient, suggested questions

Phase 4: TypingIndicator — 3 gold bouncing dots, staggered delays

Phase 4: MessageBubble — user gold gradient / bot glass, slide-in, mobileInspection slot

Phase 4: ChatInput — auto-resize textarea, fixed bottom mobile, Enter to send

Phase 4: ChatContainer — scrollable list, auto-scroll, WelcomeScreen when empty

Phase 4: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\chat\TypingIndicator.tsx
27 lines
/**
 * Animated "thinking" indicator — three gold dots bouncing sequentially.
 * Staggered delays (0s / 0.2s / 0.4s) defined in globals.css via
 * .dot-bounce:nth-child() selectors.
 */
export default function TypingIndicator() {
  return (
    <div className="flex items-start gap-2 px-4 py-2 animate-slide-in">
      {/* Bot bubble shape */}
      <div
        className="
          flex items-center gap-1.5
          ballot-glass px-4 py-3
          rounded-[20px_20px_20px_4px]
          max-w-[80px]
        "
        aria-label="Assistant is typing"
        role="status"
      >
        <span className="dot-bounce w-2 h-2 rounded-full bg-ghana-gold block" />
        <span className="dot-bounce w-2 h-2 rounded-full bg-ghana-gold block" />
        <span className="dot-bounce w-2 h-2 rounded-full bg-ghana-gold block" />
      </div>
    </div>
  );
}
Update Todos

Phase 4: WelcomeScreen — hero with Black Star gradient, suggested questions

Phase 4: TypingIndicator — 3 gold bouncing dots, staggered delays

Phase 4: MessageBubble — user gold gradient / bot glass, slide-in, mobileInspection slot

Phase 4: ChatInput — auto-resize textarea, fixed bottom mobile, Enter to send

Phase 4: ChatContainer — scrollable list, auto-scroll, WelcomeScreen when empty

Phase 4: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\chat\MessageBubble.tsx
114 lines
import { ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { ChatMessage } from "@/lib/types";

interface Props {
  message: ChatMessage;
  /**
   * Rendered below the bot bubble on mobile only (hidden on lg+).
   * Phase 5 passes the SourceAccordion + PipelineTimeline here.
   */
  mobileInspection?: ReactNode;
}

function Timestamp({ date }: { date: Date }) {
  return (
    <span className="text-[10px] text-text-muted mt-1 block">
      {date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
    </span>
  );
}

export default function MessageBubble({ message, mobileInspection }: Props) {
  const isUser = message.role === "user";

  if (isUser) {
    return (
      /* User message — right-aligned, gold gradient */
      <div className="flex flex-col items-end px-4 py-1 animate-slide-in">
        <div
          className="
            bg-gradient-to-br from-[#D4A017] to-[#FCD116]
            text-[#0B0F1A] font-medium
            px-4 py-3
            rounded-[20px_20px_4px_20px]
            max-w-[75%] sm:max-w-[65%]
            text-sm sm:text-[15px] leading-relaxed
            shadow-sm
          "
        >
          {message.content}
        </div>
        <Timestamp date={message.timestamp} />
      </div>
    );
  }

  /* Bot message — left-aligned, Ballot Box Glass */
  return (
    <div className="flex flex-col items-start px-4 py-1 animate-slide-in">
      <div
        className="
          ballot-glass
          px-4 py-3
          rounded-[20px_20px_20px_4px]
          max-w-[85%] sm:max-w-[75%]
          text-sm sm:text-[15px] leading-relaxed text-text-primary
        "
      >
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            /* Inline code — monospace gold tint */
            code: ({ children, ...rest }) => (
              <code
                className="font-mono text-ghana-gold bg-[rgba(252,209,22,0.08)] px-1.5 py-0.5 rounded text-[0.85em]"
                {...rest}
              >
                {children}
              </code>
            ),
            /* Code blocks */
            pre: ({ children }) => (
              <pre className="bg-[var(--bg-elevated)] rounded-xl p-3 my-2 overflow-x-auto text-[0.8em] font-mono text-text-secondary">
                {children}
              </pre>
            ),
            /* Links */
            a: ({ children, href }) => (
              <a
                href={href}
                target="_blank"
                rel="noopener noreferrer"
                className="text-ghana-gold underline underline-offset-2 hover:text-[#D4A017]"
              >
                {children}
              </a>
            ),
            /* Bold */
            strong: ({ children }) => (
              <strong className="font-semibold text-text-primary">{children}</strong>
            ),
            /* List items */
            li: ({ children }) => (
              <li className="ml-4 list-disc marker:text-ghana-gold">{children}</li>
            ),
          }}
        >
          {message.content}
        </ReactMarkdown>
      </div>

      <Timestamp date={message.timestamp} />

      {/* Mobile inspection slot — only shown below lg breakpoint */}
      {mobileInspection && (
        <div className="lg:hidden w-full max-w-[85%] mt-1">
          {mobileInspection}
        </div>
      )}
    </div>
  );
}
Update Todos

Phase 4: WelcomeScreen — hero with Black Star gradient, suggested questions

Phase 4: TypingIndicator — 3 gold bouncing dots, staggered delays

Phase 4: MessageBubble — user gold gradient / bot glass, slide-in, mobileInspection slot

Phase 4: ChatInput — auto-resize textarea, fixed bottom mobile, Enter to send

Phase 4: ChatContainer — scrollable list, auto-scroll, WelcomeScreen when empty

Phase 4: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\chat\ChatInput.tsx
151 lines
"use client";

import {
  useRef,
  useState,
  useEffect,
  KeyboardEvent,
  FormEvent,
} from "react";
import { Send } from "lucide-react";

interface Props {
  onSend: (text: string) => void;
  disabled?: boolean;
  /** Pre-fill the input (e.g. from a suggestion click) */
  prefill?: string;
  onPrefillConsumed?: () => void;
}

/**
 * Chat input bar.
 *
 * Mobile  (<lg): fixed to the bottom of the viewport, gold focus ring,
 *                safe-area padding for notched phones.
 * Desktop (lg+): sits inline at the bottom of the chat panel (relative).
 *
 * Behaviour:
 * - Textarea auto-grows up to max-h-32 then scrolls.
 * - Enter submits; Shift+Enter inserts a newline.
 * - Disabled while the backend is responding.
 */
export default function ChatInput({
  onSend,
  disabled = false,
  prefill,
  onPrefillConsumed,
}: Props) {
  const [value, setValue] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  /* Apply prefill from suggestion clicks */
  useEffect(() => {
    if (prefill) {
      setValue(prefill);
      onPrefillConsumed?.();
      textareaRef.current?.focus();
    }
  }, [prefill, onPrefillConsumed]);

  /* Auto-resize textarea to fit content */
  useEffect(() => {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${Math.min(el.scrollHeight, 128)}px`;
  }, [value]);

  function submit() {
    const trimmed = value.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setValue("");
    if (textareaRef.current) textareaRef.current.style.height = "auto";
  }

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      submit();
    }
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    submit();
  }

  const canSend = value.trim().length > 0 && !disabled;

  return (
    /*
     * Mobile:  fixed bottom-0, full width, dark blurred background,
     *          safe-area-bottom padding for notched phones.
     * Desktop: relative, no background override, blends into panel.
     */
    <div
      className="
        fixed bottom-0 left-0 right-0 z-30
        lg:relative lg:bottom-auto lg:left-auto lg:right-auto lg:z-auto
        px-4 pb-4 pt-3
        bg-[var(--bg-deep)]/90 backdrop-blur-md
        lg:bg-transparent lg:backdrop-blur-none
        safe-area-bottom
        border-t border-[var(--border-subtle)]
        lg:border-t-0 lg:px-4 lg:py-4
      "
    >
      <form onSubmit={handleSubmit} className="flex items-end gap-2">
        <textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={disabled}
          rows={1}
          placeholder="Ask about Ghana elections or budget…"
          aria-label="Chat message input"
          className="
            flex-1 resize-none
            bg-[var(--bg-elevated)]/80 backdrop-blur-sm
            border border-[var(--border-subtle)]
            rounded-2xl
            px-4 py-3
            text-sm text-text-primary placeholder:text-text-muted
            min-h-[48px] max-h-32
            overflow-y-auto scroll-touch
            transition-[border-color,box-shadow] duration-200
            focus:outline-none focus:border-[rgba(252,209,22,0.4)]
            focus:shadow-[0_0_0_2px_rgba(252,209,22,0.12)]
            disabled:opacity-50 disabled:cursor-not-allowed
          "
        />

        {/* Send button */}
        <button
          type="submit"
          disabled={!canSend}
          aria-label="Send message"
          className="
            min-w-[48px] min-h-[48px]
            flex items-center justify-center
            rounded-xl shrink-0
            transition-all duration-200
            active:scale-95
            focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/60
            disabled:opacity-30 disabled:cursor-not-allowed disabled:active:scale-100
            bg-gradient-to-br from-[#D4A017] to-[#FCD116]
            text-[#0B0F1A]
          "
        >
          <Send size={18} />
        </button>
      </form>

      <p className="hidden lg:block text-[10px] text-text-muted mt-1.5 text-right">
        Enter to send · Shift+Enter for new line
      </p>
    </div>
  );
}
Update Todos

Phase 4: WelcomeScreen — hero with Black Star gradient, suggested questions

Phase 4: TypingIndicator — 3 gold bouncing dots, staggered delays

Phase 4: MessageBubble — user gold gradient / bot glass, slide-in, mobileInspection slot

Phase 4: ChatInput — auto-resize textarea, fixed bottom mobile, Enter to send

Phase 4: ChatContainer — scrollable list, auto-scroll, WelcomeScreen when empty

Phase 4: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\chat\ChatContainer.tsx
97 lines
"use client";

import { useEffect, useRef, useState, ReactNode } from "react";
import type { ChatMessage } from "@/lib/types";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";
import WelcomeScreen from "./WelcomeScreen";
import ChatInput from "./ChatInput";

interface Props {
  messages: ChatMessage[];
  isLoading: boolean;
  onSend: (text: string) => void;
  /**
   * Given a bot message, return the mobile inspection node
   * (SourceAccordion + PipelineTimeline). Supplied by Phase 5.
   * Falls back to null until then.
   */
  renderMobileInspection?: (message: ChatMessage) => ReactNode;
}

/**
 * Scrollable message list.
 *
 * - Auto-scrolls to the bottom whenever messages or loading state change.
 * - Shows WelcomeScreen when empty.
 * - Suggestion clicks pre-fill ChatInput via local state.
 * - On mobile the list has bottom padding so the fixed input bar never
 *   obscures the last message.
 */
export default function ChatContainer({
  messages,
  isLoading,
  onSend,
  renderMobileInspection,
}: Props) {
  const bottomRef = useRef<HTMLDivElement>(null);
  const [prefill, setPrefill] = useState<string | undefined>();

  /* Auto-scroll to the latest message */
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  function handleSuggestion(text: string) {
    setPrefill(text);
  }

  const isEmpty = messages.length === 0;

  return (
    <div className="flex flex-col flex-1 min-h-0">
      {/* Scrollable area */}
      <div
        className="
          flex-1 overflow-y-auto scroll-touch
          py-4
          /* Bottom padding ensures last message clears the fixed input bar on mobile */
          pb-[80px] lg:pb-4
        "
      >
        {isEmpty ? (
          <WelcomeScreen onSuggestion={handleSuggestion} />
        ) : (
          <div className="flex flex-col gap-1">
            {messages.map((msg) => (
              <MessageBubble
                key={msg.id}
                message={msg}
                mobileInspection={
                  msg.role === "assistant" && renderMobileInspection
                    ? renderMobileInspection(msg)
                    : undefined
                }
              />
            ))}

            {/* Typing indicator while waiting for response */}
            {isLoading && <TypingIndicator />}

            {/* Scroll anchor */}
            <div ref={bottomRef} />
          </div>
        )}
      </div>

      {/* Input bar — fixed on mobile, inline on desktop */}
      <ChatInput
        onSend={onSend}
        disabled={isLoading}
        prefill={prefill}
        onPrefillConsumed={() => setPrefill(undefined)}
      />
    </div>
  );
}
Update Todos

Phase 4: WelcomeScreen — hero with Black Star gradient, suggested questions

Phase 4: TypingIndicator — 3 gold bouncing dots, staggered delays

Phase 4: MessageBubble — user gold gradient / bot glass, slide-in, mobileInspection slot

Phase 4: ChatInput — auto-resize textarea, fixed bottom mobile, Enter to send

Phase 4: ChatContainer — scrollable list, auto-scroll, WelcomeScreen when empty

Phase 4: TypeScript check — verify zero errors
Bash TypeScript check all Phase 4 components
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app" && npx tsc --noEmit 2>&1

OUT
(Bash completed with no output)
Update Todos

Phase 4: WelcomeScreen — hero with Black Star gradient, suggested questions

Phase 4: TypingIndicator — 3 gold bouncing dots, staggered delays

Phase 4: MessageBubble — user gold gradient / bot glass, slide-in, mobileInspection slot

Phase 4: ChatInput — auto-resize textarea, fixed bottom mobile, Enter to send

Phase 4: ChatContainer — scrollable list, auto-scroll, WelcomeScreen when empty

Phase 4: TypeScript check — verify zero errors
Phase 4 complete. Zero TypeScript errors. Here's what was built:

File	Key spec details
WelcomeScreen.tsx	Tricolour gradient Black Star SVG, gradient-brand title text, 4 suggested questions as glass cards that pre-fill the input on tap
TypingIndicator.tsx	3 bg-ghana-gold dots using .dot-bounce animation from globals.css, staggered via nth-child delays, bot-bubble shape
MessageBubble.tsx	User = from-[#D4A017] to-[#FCD116] right-aligned; Bot = ballot-glass left-aligned; full react-markdown + GFM rendering; mobileInspection slot (hidden on lg+) for Phase 5
ChatInput.tsx	fixed bottom-0 on mobile → relative on lg+; auto-resize textarea; gold focus ring; Enter submits, Shift+Enter = newline; 48px send button
ChatContainer.tsx	Auto-scrolls on new messages, pb-[80px] clears fixed input bar on mobile, WelcomeScreen when empty, TypingIndicator while loading, renderMobileInspection prop ready for Phase 5
Ready for Phase 5 — RAG Inspection (SimilarityBadge, SourceCard, SourceList, PromptViewer, PipelineTimeline, SourceAccordion, InspectionPanel)?

phase 5
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Bash Create RAG components directory
IN
mkdir -p "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app/src/components/rag"

OUT
(Bash completed with no output)
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\rag\SimilarityBadge.tsx
57 lines
/**
 * Ghana-flag spectrum score badge.
 *
 * >= 0.75  → Ghana Green  (high confidence)
 *  0.5–0.75 → Ghana Gold   (moderate confidence)
 * < 0.5   → Ghana Red    (low confidence)
 *
 * Pulses once on mount via animate-badge-pulse (defined in globals.css).
 */

type ScoreLevel = "high" | "medium" | "low";

interface Props {
  score: number;
  label?: string; // e.g. "hybrid", "vector", "keyword"
  className?: string;
}

function getLevel(score: number): ScoreLevel {
  if (score >= 0.75) return "high";
  if (score >= 0.5)  return "medium";
  return "low";
}

const levelStyles: Record<ScoreLevel, string> = {
  high:   "bg-[rgba(0,107,63,0.18)]   text-ghana-green-bright border-[rgba(0,107,63,0.25)]",
  medium: "bg-[rgba(252,209,22,0.15)] text-ghana-gold         border-[rgba(252,209,22,0.2)]",
  low:    "bg-[rgba(206,17,38,0.15)]  text-ghana-red          border-[rgba(206,17,38,0.2)]",
};

const levelDots: Record<ScoreLevel, string> = {
  high:   "bg-ghana-green-bright",
  medium: "bg-ghana-gold",
  low:    "bg-ghana-red",
};

export default function SimilarityBadge({ score, label, className = "" }: Props) {
  const level = getLevel(score);

  return (
    <span
      className={`
        inline-flex items-center gap-1.5
        px-2 py-0.5 rounded-full border
        font-mono text-[10px] sm:text-[11px] font-semibold
        animate-badge-pulse
        ${levelStyles[level]}
        ${className}
      `}
      title={label ? `${label} score` : "similarity score"}
    >
      <span className={`w-1.5 h-1.5 rounded-full shrink-0 ${levelDots[level]}`} />
      {score.toFixed(3)}
    </span>
  );
}
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\rag\SourceCard.tsx
105 lines
import { useState } from "react";
import { ChevronDown, FileText } from "lucide-react";
import type { RetrievedDocument } from "@/lib/types";
import BallotGlassCard from "@/components/ui/BallotGlassCard";
import Badge from "@/components/ui/Badge";
import ScoreBar from "@/components/ui/ScoreBar";
import SimilarityBadge from "./SimilarityBadge";

interface Props {
  doc: RetrievedDocument;
}

/** Infer dataset type from the source string */
function datasetVariant(source: string): { label: string; variant: "gold" | "green" | "muted" } {
  const s = source.toLowerCase();
  if (s.includes("election") || s.includes("electoral") || s.includes("vote") || s.includes("parliament"))
    return { label: "Electoral", variant: "gold" };
  if (s.includes("budget") || s.includes("fiscal") || s.includes("finance") || s.includes("economic"))
    return { label: "Budget", variant: "green" };
  return { label: "Civic", variant: "muted" };
}

/**
 * Single retrieved chunk card — "Transparent Ballot Box Glass" style.
 * Shows rank, chunk ID, source, similarity scores, and a truncated text
 * preview that expands on tap/click.
 */
export default function SourceCard({ doc }: Props) {
  const [expanded, setExpanded] = useState(false);
  const { label, variant } = datasetVariant(doc.source);
  const hybrid = doc.similarity_scores.hybrid_score;

  return (
    <BallotGlassCard className="p-3 sm:p-4 flex flex-col gap-2.5 animate-slide-in">
      {/* ── Header row ── */}
      <div className="flex items-start justify-between gap-2">
        <div className="flex items-center gap-2 min-w-0">
          {/* Rank badge */}
          <span className="shrink-0 w-6 h-6 rounded-full bg-[rgba(252,209,22,0.12)] border border-[rgba(252,209,22,0.2)] flex items-center justify-center text-[10px] font-bold text-ghana-gold">
            {doc.rank}
          </span>
          {/* Chunk ID */}
          <span className="font-mono text-[10px] sm:text-xs text-text-muted truncate">
            {doc.chunk_id}
          </span>
        </div>

        {/* Dataset tag + hybrid score */}
        <div className="flex items-center gap-1.5 shrink-0">
          <Badge variant={variant}>{label}</Badge>
          <SimilarityBadge score={hybrid} label="hybrid" />
        </div>
      </div>

      {/* ── Source / doc reference ── */}
      <div className="flex items-center gap-1.5 text-[10px] sm:text-xs text-text-muted">
        <FileText size={11} className="shrink-0 text-text-muted" />
        <span className="truncate" title={doc.source}>{doc.source}</span>
        <span className="text-[var(--border-subtle)]">·</span>
        <span className="truncate font-mono" title={doc.doc_id}>{doc.doc_id}</span>
      </div>

      {/* ── Score bar (hybrid score) ── */}
      <ScoreBar score={hybrid} />

      {/* ── Individual scores ── */}
      <div className="flex gap-2 flex-wrap">
        <div className="flex items-center gap-1 text-[10px] text-text-muted">
          <span>Vector</span>
          <SimilarityBadge score={doc.similarity_scores.vector_score} label="vector" />
        </div>
        <div className="flex items-center gap-1 text-[10px] text-text-muted">
          <span>Keyword</span>
          <SimilarityBadge score={doc.similarity_scores.keyword_score} label="keyword" />
        </div>
      </div>

      {/* ── Text preview ── */}
      <div className="border-t border-[var(--border-subtle)] pt-2.5">
        <p
          className={`text-[11px] sm:text-xs text-text-secondary leading-relaxed font-mono ${
            expanded ? "" : "line-clamp-3"
          }`}
        >
          {doc.text_preview}
        </p>

        {doc.text_preview.length > 120 && (
          <button
            type="button"
            onClick={() => setExpanded((v) => !v)}
            className="mt-1.5 flex items-center gap-1 text-[10px] text-ghana-gold hover:text-[#D4A017] transition-colors"
          >
            <ChevronDown
              size={12}
              className={`transition-transform duration-200 ${expanded ? "rotate-180" : ""}`}
            />
            {expanded ? "Show less" : "Show more"}
          </button>
        )}
      </div>
    </BallotGlassCard>
  );
}
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\rag\SourceList.tsx
59 lines
import type { RetrievedDocument } from "@/lib/types";
import SourceCard from "./SourceCard";
import { SkeletonText } from "@/components/ui/Skeleton";
import Skeleton from "@/components/ui/Skeleton";

interface Props {
  docs: RetrievedDocument[];
  isLoading?: boolean;
}

function SkeletonCard() {
  return (
    <div className="ballot-glass p-4 flex flex-col gap-3">
      <div className="flex justify-between">
        <div className="flex gap-2 items-center">
          <Skeleton width="w-6" height="h-6" pill />
          <Skeleton width="w-28" height="h-3" />
        </div>
        <div className="flex gap-1.5">
          <Skeleton width="w-14" height="h-5" pill />
          <Skeleton width="w-14" height="h-5" pill />
        </div>
      </div>
      <Skeleton height="h-1.5" />
      <SkeletonText lines={3} />
    </div>
  );
}

/**
 * Renders the full list of retrieved chunks.
 * Shows skeleton cards while the backend is responding.
 */
export default function SourceList({ docs, isLoading = false }: Props) {
  if (isLoading) {
    return (
      <div className="flex flex-col gap-3">
        {[1, 2, 3].map((i) => <SkeletonCard key={i} />)}
      </div>
    );
  }

  if (docs.length === 0) {
    return (
      <p className="text-sm text-text-muted text-center py-6">
        No sources retrieved.
      </p>
    );
  }

  return (
    <div className="flex flex-col gap-3">
      {docs.map((doc) => (
        <SourceCard key={doc.chunk_id} doc={doc} />
      ))}
    </div>
  );
}
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\rag\PromptViewer.tsx
82 lines
"use client";

import { useState } from "react";
import { Copy, Check } from "lucide-react";
import Accordion from "@/components/ui/Accordion";

interface Props {
  prompt: string;
}

/**
 * Collapsible viewer for the final prompt sent to the LLM.
 * Displayed in JetBrains Mono inside a dark code surface.
 * Includes a copy-to-clipboard button that shows a tick confirmation.
 */
export default function PromptViewer({ prompt }: Props) {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(prompt);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // clipboard API not available (e.g. HTTP context) — silently ignore
    }
  }

  return (
    <Accordion
      title={
        <span className="flex items-center gap-2 text-sm font-medium text-text-secondary">
          <span className="text-ghana-gold font-mono text-xs">{"{ }"}</span>
          Final Prompt Sent to LLM
        </span>
      }
      defaultOpen={false}
      accent="muted"
    >
      {/* Code surface */}
      <div className="relative rounded-xl bg-[var(--bg-deep)] border border-[var(--border-subtle)] overflow-hidden">
        {/* Copy button */}
        <button
          type="button"
          onClick={handleCopy}
          aria-label="Copy prompt"
          className="
            absolute top-2 right-2 z-10
            flex items-center gap-1 px-2 py-1
            text-[10px] font-medium rounded-lg
            bg-[var(--bg-elevated)] border border-[var(--border-subtle)]
            text-text-muted hover:text-ghana-gold
            transition-colors duration-150
            min-h-[32px]
          "
        >
          {copied ? (
            <><Check size={11} className="text-ghana-green-bright" /><span className="text-ghana-green-bright">Copied</span></>
          ) : (
            <><Copy size={11} /><span>Copy</span></>
          )}
        </button>

        {/* Prompt text */}
        <pre
          className="
            overflow-x-auto scroll-touch
            p-4 pr-20
            text-[10px] sm:text-xs
            font-mono text-text-secondary leading-relaxed
            whitespace-pre-wrap break-words
            max-h-64
            overflow-y-auto
          "
        >
          {prompt}
        </pre>
      </div>
    </Accordion>
  );
}
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\rag\PipelineTimeline.tsx
74 lines
import { Clock } from "lucide-react";
import type { QueryResponse } from "@/lib/types";
import { parseStageDurations } from "@/lib/api";

interface Props {
  stageTimes: QueryResponse["stage_times"];
}

/**
 * Pipeline timing breakdown — gold left-border timeline with a glowing dot
 * at each stage, matching the spec design exactly.
 *
 * Durations are derived from ISO timestamps via parseStageDurations().
 */
export default function PipelineTimeline({ stageTimes }: Props) {
  const stages = parseStageDurations(stageTimes);
  const totalMs = stages.reduce((sum, s) => sum + s.ms, 0);

  return (
    <div className="flex flex-col gap-1">
      {/* Header */}
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-1.5 text-xs font-semibold text-text-secondary uppercase tracking-wider">
          <Clock size={12} className="text-ghana-gold" />
          Pipeline Timing
        </div>
        <span className="font-mono text-[10px] text-text-muted">
          total {totalMs}ms
        </span>
      </div>

      {/* Timeline */}
      <div className="border-l-2 border-ghana-gold pl-4 flex flex-col gap-3">
        {stages.map(({ label, ms }) => {
          const pct = totalMs > 0 ? Math.round((ms / totalMs) * 100) : 0;

          return (
            <div key={label} className="relative flex flex-col gap-1">
              {/* Gold dot on the timeline rail */}
              <span
                className="
                  absolute -left-[21px] top-1
                  w-2.5 h-2.5 rounded-full
                  bg-ghana-gold
                  shadow-[0_0_8px_rgba(252,209,22,0.45)]
                "
              />

              {/* Label + duration */}
              <div className="flex items-center justify-between">
                <span className="text-[11px] sm:text-xs text-text-secondary">{label}</span>
                <span className="font-mono text-[11px] sm:text-xs text-ghana-gold font-semibold">
                  {ms}ms
                </span>
              </div>

              {/* Proportional bar */}
              <div className="h-1 rounded-full bg-[var(--bg-elevated)] overflow-hidden">
                <div
                  className="h-full rounded-full bg-ghana-gold/60"
                  style={{
                    width: `${pct}%`,
                    transition: "width 600ms cubic-bezier(0.4,0,0.2,1)",
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\rag\SourceAccordion.tsx
64 lines
import type { QueryResponse } from "@/lib/types";
import Accordion from "@/components/ui/Accordion";
import SourceList from "./SourceList";
import PipelineTimeline from "./PipelineTimeline";

interface Props {
  ragData: QueryResponse;
}

/**
 * Mobile-only inspection wrapper.
 *
 * Renders two stacked accordions beneath each bot message bubble:
 *   1. "View Sources (N)" — SourceList
 *   2. "Pipeline Timing"  — PipelineTimeline
 *
 * Hidden on lg+ (the desktop InspectionPanel handles it there).
 * The parent MessageBubble renders this inside its `mobileInspection` slot.
 */
export default function SourceAccordion({ ragData }: Props) {
  const count = ragData.retrieved_documents.length;

  return (
    <div className="flex flex-col rounded-xl overflow-hidden border border-[var(--border-subtle)] bg-[var(--bg-surface)]/60 backdrop-blur-sm">
      {/* Sources accordion */}
      <Accordion
        title={
          <span className="flex items-center gap-2 text-xs text-text-secondary">
            <span className="text-ghana-gold">▤</span>
            View Sources
            <span className="ml-1 px-1.5 py-0.5 rounded-full bg-[rgba(252,209,22,0.12)] text-ghana-gold text-[10px] font-semibold font-mono">
              {count}
            </span>
          </span>
        }
        defaultOpen={false}
      >
        <div className="pt-1">
          <SourceList docs={ragData.retrieved_documents} />
        </div>
      </Accordion>

      {/* Divider */}
      <div className="h-px bg-[var(--border-subtle)] mx-4" />

      {/* Pipeline timing accordion */}
      <Accordion
        title={
          <span className="flex items-center gap-2 text-xs text-text-secondary">
            <span className="text-ghana-gold">⏱</span>
            Pipeline Timing
          </span>
        }
        defaultOpen={false}
        accent="muted"
      >
        <div className="pt-1">
          <PipelineTimeline stageTimes={ragData.stage_times} />
        </div>
      </Accordion>
    </div>
  );
}
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Write c:\Users\ayekp\OneDrive\Desktop\AI_10012200016\frontend-app\src\components\rag\InspectionPanel.tsx
87 lines
import { FileSearch } from "lucide-react";
import type { QueryResponse } from "@/lib/types";
import SourceList from "./SourceList";
import PromptViewer from "./PromptViewer";
import PipelineTimeline from "./PipelineTimeline";

interface Props {
  /** The ragData from the most recent bot message. Null before first query. */
  ragData: QueryResponse | null;
  isLoading?: boolean;
}

/**
 * Desktop right-hand RAG inspection panel (45% width, set by AppShell).
 *
 * Sections (in order per spec):
 *   1. Retrieved Chunks   — SourceList with similarity scores
 *   2. Final Prompt       — PromptViewer (collapsible code block)
 *   3. Pipeline Timing    — PipelineTimeline with gold dots
 *
 * Shows an empty state before the first query is sent.
 * Hidden on mobile — the SourceAccordion inside MessageBubble handles it.
 */
export default function InspectionPanel({ ragData, isLoading = false }: Props) {
  /* Empty / loading state */
  if (!ragData && !isLoading) {
    return (
      <div className="flex flex-col items-center justify-center flex-1 px-6 py-16 text-center gap-4">
        <FileSearch size={40} className="text-text-muted opacity-40" />
        <p className="text-sm text-text-muted max-w-[200px] leading-relaxed">
          RAG inspection data will appear here after your first query.
        </p>
      </div>
    );
  }

  return (
    <div className="flex flex-col flex-1 overflow-y-auto scroll-touch">
      {/* ── Panel header ── */}
      <div className="sticky top-0 z-10 px-4 py-3 bg-[var(--bg-surface)]/80 backdrop-blur-sm border-b border-[var(--border-subtle)]">
        <h2 className="text-xs font-semibold uppercase tracking-wider text-text-muted">
          RAG Inspection
        </h2>
        {ragData && (
          <p className="text-[10px] text-text-muted mt-0.5 font-mono truncate" title={ragData.run_id}>
            {ragData.run_id}
          </p>
        )}
      </div>

      <div className="flex flex-col gap-0 divide-y divide-[var(--border-subtle)]">

        {/* ── 1. Retrieved Chunks ── */}
        <section className="px-4 py-4 flex flex-col gap-3">
          <h3 className="text-xs font-semibold text-text-secondary uppercase tracking-wider flex items-center gap-2">
            <span className="text-ghana-gold">▤</span>
            Retrieved Chunks
            {ragData && (
              <span className="ml-auto font-mono text-[10px] text-text-muted normal-case tracking-normal">
                {ragData.context_selection.used_context_tokens} tokens used
              </span>
            )}
          </h3>
          <SourceList
            docs={ragData?.retrieved_documents ?? []}
            isLoading={isLoading}
          />
        </section>

        {/* ── 2. Final Prompt ── */}
        {ragData && (
          <section className="px-4 py-2">
            <PromptViewer prompt={ragData.final_prompt_sent_to_llm} />
          </section>
        )}

        {/* ── 3. Pipeline Timing ── */}
        {ragData && (
          <section className="px-4 py-4">
            <PipelineTimeline stageTimes={ragData.stage_times} />
          </section>
        )}
      </div>
    </div>
  );
}
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Bash TypeScript check all Phase 5 components
IN
cd "c:/Users/ayekp/OneDrive/Desktop/AI_10012200016/frontend-app" && npx tsc --noEmit 2>&1

OUT
(Bash completed with no output)
Update Todos

Phase 5: SimilarityBadge — Ghana-flag score badge, pulse on mount, mono font

Phase 5: SourceCard — ballot-glass chunk card, rank, scores, text preview, dataset tag

Phase 5: SourceList — maps retrieved_documents to SourceCards, skeleton loading

Phase 5: PromptViewer — collapsible code block for final LLM prompt, copy button

Phase 5: PipelineTimeline — gold left-border timeline, stage labels + ms durations

Phase 5: SourceAccordion — mobile wrapper with Sources + Pipeline accordions

Phase 5: InspectionPanel — desktop right panel, empty state, assembles all RAG components

Phase 5: TypeScript check — verify zero errors
Phase 5 complete. Zero TypeScript errors. Here's what was built:

File	Key spec details
SimilarityBadge.tsx	Ghana-flag spectrum — green ≥0.75, gold 0.5–0.75, red <0.5. Coloured dot + animate-badge-pulse on mount, JetBrains Mono number
SourceCard.tsx	ballot-glass card with rank circle, chunk ID, source path, dataset tag (Electoral/Budget/Civic auto-detected), full ScoreBar + individual SimilarityBadge per score, expandable text preview
SourceList.tsx	Maps docs to SourceCards, shows 3 skeleton cards while loading, empty state for zero results
PromptViewer.tsx	Wrapped in Accordion (collapsed by default), monospace pre block, copy-to-clipboard button with green tick confirmation, max-h-64 scrollable
PipelineTimeline.tsx	Gold left-border rail, glowing dot per stage, label + Xms, proportional width bar per stage, total time in header
SourceAccordion.tsx	Mobile-only: two stacked accordions — "View Sources (N)" + "Pipeline Timing", glass surface, both collapsed by default
InspectionPanel.tsx	Desktop 45% panel — sticky header with run_id, sections for chunks / prompt / timing, empty state with icon before first query, tokens-used counter
Ready for Phase 6 — Settings (SliderInput, ModelSelector, SettingsPanel)?