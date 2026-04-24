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
