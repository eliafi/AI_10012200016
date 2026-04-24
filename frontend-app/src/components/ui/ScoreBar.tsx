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
