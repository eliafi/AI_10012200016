"use client";

import { useEffect, useRef, ReactNode } from "react";
import { X } from "lucide-react";

interface Props {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: ReactNode;
}

/**
 * Mobile slide-up bottom sheet.
 *
 * - Slides in from bottom in 350ms (spec requirement)
 * - Backdrop fades in simultaneously
 * - Locks body scroll while open
 * - Closes on backdrop click or the × button
 * - On desktop (lg+) renders as a fixed right-side panel instead
 */
export default function BottomSheet({ isOpen, onClose, title, children }: Props) {
  const sheetRef = useRef<HTMLDivElement>(null);

  // Lock body scroll when open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => { document.body.style.overflow = ""; };
  }, [isOpen]);

  // Close on Escape
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape" && isOpen) onClose();
    };
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <>
      {/* Backdrop */}
      <div
        className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm animate-fade-in"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Sheet — slides up from bottom on mobile, panel from right on desktop */}
      <div
        ref={sheetRef}
        role="dialog"
        aria-modal="true"
        aria-label={title}
        className="
          fixed z-50 flex flex-col
          bg-[var(--bg-surface)] border-t border-[var(--border-glass)]

          /* Mobile: full-width panel from bottom, max 85vh */
          bottom-0 left-0 right-0
          max-h-[85dvh] rounded-t-2xl
          animate-slide-up

          /* Desktop: right sidebar */
          lg:bottom-0 lg:top-0 lg:left-auto lg:right-0
          lg:w-80 lg:max-h-none lg:rounded-none lg:rounded-l-2xl
          lg:border-t-0 lg:border-l
          lg:animate-none
        "
      >
        {/* Handle bar (mobile only) */}
        <div className="flex justify-center pt-3 pb-1 lg:hidden">
          <div className="w-10 h-1 rounded-full bg-[var(--border-subtle)]" />
        </div>

        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-[var(--border-subtle)] shrink-0">
          <h2 className="text-base font-semibold text-text-primary">{title}</h2>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close"
            className="
              min-w-[44px] min-h-[44px] flex items-center justify-center
              text-text-muted hover:text-ghana-gold rounded-xl
              active:scale-95 transition-all duration-150
              focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
            "
          >
            <X size={20} />
          </button>
        </div>

        {/* Content — scrollable */}
        <div className="flex-1 overflow-y-auto scroll-touch px-5 py-4 safe-area-bottom">
          {children}
        </div>
      </div>
    </>
  );
}
