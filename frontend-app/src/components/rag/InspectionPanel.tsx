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
