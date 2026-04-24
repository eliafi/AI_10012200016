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
