"use client";

import { useState, useRef, useEffect, ReactNode } from "react";
import { ChevronDown } from "lucide-react";

interface Props {
  title: ReactNode;
  children: ReactNode;
  /** Start open */
  defaultOpen?: boolean;
  /** Gold chevron tint (default) or muted */
  accent?: "gold" | "muted";
  className?: string;
}

/**
 * Expandable section with smooth height transition and rotating chevron.
 * Used heavily on mobile to reveal RAG inspection data under each response.
 * Transition: 250ms cubic-bezier as specified in the design blueprint.
 */
export default function Accordion({
  title,
  children,
  defaultOpen = false,
  accent = "gold",
  className = "",
}: Props) {
  const [open, setOpen] = useState(defaultOpen);
  const bodyRef = useRef<HTMLDivElement>(null);
  const [height, setHeight] = useState<string>(defaultOpen ? "auto" : "0px");

  useEffect(() => {
    if (!bodyRef.current) return;
    if (open) {
      // measure then animate to exact height, then switch to "auto"
      const h = bodyRef.current.scrollHeight;
      setHeight(`${h}px`);
      const timer = setTimeout(() => setHeight("auto"), 260);
      return () => clearTimeout(timer);
    } else {
      // snapshot current height before collapsing
      const h = bodyRef.current.scrollHeight;
      setHeight(`${h}px`);
      // force a reflow so the transition fires
      bodyRef.current.getBoundingClientRect();
      requestAnimationFrame(() => setHeight("0px"));
    }
  }, [open]);

  const chevronColor =
    accent === "gold" ? "text-ghana-gold" : "text-text-muted";

  return (
    <div className={`w-full ${className}`}>
      {/* Trigger — full-width, minimum 44px touch target */}
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className={`
          flex w-full items-center justify-between
          min-h-[44px] px-4 py-2.5
          text-left text-sm font-medium text-text-primary
          hover:text-ghana-gold transition-colors duration-200
          focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
        `}
        aria-expanded={open}
      >
        <span>{title}</span>
        <ChevronDown
          size={16}
          className={`
            shrink-0 transition-transform duration-[250ms] cubic-bezier(0.4,0,0.2,1)
            ${chevronColor}
            ${open ? "rotate-180" : "rotate-0"}
          `}
        />
      </button>

      {/* Collapsible body */}
      <div
        ref={bodyRef}
        style={{
          height,
          overflow: "hidden",
          transition: "height 250ms cubic-bezier(0.4, 0, 0.2, 1)",
        }}
        aria-hidden={!open}
      >
        <div className="px-4 pb-3">{children}</div>
      </div>
    </div>
  );
}
