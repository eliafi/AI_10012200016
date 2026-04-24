import { ButtonHTMLAttributes } from "react";

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Show a non-interactive icon-only variant (square, rounded-xl) */
  icon?: boolean;
}

/**
 * Primary action button — Ghana gold gradient.
 * Minimum 44×44px touch target on all screen sizes.
 */
export default function GoldButton({
  children,
  icon = false,
  className = "",
  disabled,
  ...rest
}: Props) {
  return (
    <button
      disabled={disabled}
      className={`
        inline-flex items-center justify-center gap-2
        bg-gradient-to-br from-[#D4A017] to-[#FCD116]
        text-[#0B0F1A] font-semibold
        transition-transform duration-200
        active:scale-95
        disabled:opacity-40 disabled:cursor-not-allowed disabled:active:scale-100
        focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/60
        ${icon
          ? "min-w-[44px] min-h-[44px] rounded-xl text-sm"
          : "min-h-[44px] px-5 py-2.5 rounded-2xl text-sm sm:text-base"
        }
        ${className}
      `}
      {...rest}
    >
      {children}
    </button>
  );
}
