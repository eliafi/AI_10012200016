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
