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
