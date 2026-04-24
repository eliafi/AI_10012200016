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
