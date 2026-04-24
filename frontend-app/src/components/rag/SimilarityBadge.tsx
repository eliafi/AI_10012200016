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
