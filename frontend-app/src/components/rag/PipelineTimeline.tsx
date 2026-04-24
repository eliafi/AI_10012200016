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
