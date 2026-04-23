from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from backend.scripts.run_full_pipeline import run_pipeline


class QueryRequest(BaseModel):
    query: str = Field(min_length=3)
    top_k: int = Field(default=5, ge=1, le=20)
    hybrid_alpha: float = Field(default=0.55, ge=0.0, le=1.0)
    llm_model: str = Field(default="gpt-4o-mini")
    max_context_tokens: int = Field(default=1200, ge=200, le=4000)


app = FastAPI(title="Academic City RAG API", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/query")
def query_rag(request: QueryRequest) -> dict:
    try:
        payload, output_path = run_pipeline(
            query=request.query,
            top_k=request.top_k,
            hybrid_alpha=request.hybrid_alpha,
            llm_model=request.llm_model,
            max_context_tokens=request.max_context_tokens,
            code_root=Path(__file__).resolve().parents[2],
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return {
        "run_id": payload["run_id"],
        "query": payload["input"]["query"],
        "retrieved_documents": payload["pipeline"]["retrieved_documents"],
        "context_selection": payload["pipeline"]["context_selection"],
        "final_prompt_sent_to_llm": payload["pipeline"]["final_prompt_sent_to_llm"],
        "response": payload["pipeline"]["response"],
        "stage_times": payload["stage_times"],
        "run_log_path": str(output_path),
    }
