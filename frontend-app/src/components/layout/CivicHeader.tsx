"use client";

import Image from "next/image";
import { Settings } from "lucide-react";

interface Props {
  onSettingsOpen: () => void;
}

/**
 * Top header bar.
 *
 * Mobile  (<lg): logo icon only + abbreviated title + icon buttons
 * Desktop (lg+): full logo + full title + labelled settings button
 *
 * The Ghana tricolour gradient is applied to the bottom border to
 * reinforce brand identity without overwhelming the dark surface.
 */
export default function CivicHeader({ onSettingsOpen }: Props) {
  return (
    <header
      className="
        relative z-20
        flex items-center justify-between
        px-4 lg:px-6
        h-14 lg:h-16
        bg-[var(--bg-surface)]/80 backdrop-blur-md
        border-b border-[var(--border-subtle)]
        shrink-0
      "
    >
      {/* Ghana tricolour accent line across the bottom of the header */}
      <div
        className="absolute bottom-0 left-0 right-0 h-[2px]"
        style={{ background: "var(--gradient-brand)" }}
      />

      {/* ── Left: brand ── */}
      <div className="flex items-center gap-3">
        {/* Navbar icon — always visible */}
        <div className="relative w-8 h-8 lg:w-9 lg:h-9 shrink-0">
          <Image
            src="/navbar-icon.png"
            alt="Ghana Civic RAG icon"
            fill
            className="object-contain"
            priority
          />
        </div>

        {/* Full logo — hidden on small screens to save space */}
        <div className="hidden sm:block relative w-24 h-8 lg:w-28 lg:h-9 shrink-0">
          <Image
            src="/logo.png"
            alt="Ghana Civic RAG logo"
            fill
            className="object-contain object-left"
            priority
          />
        </div>

        {/* Title text */}
        <div className="flex flex-col leading-tight">
          {/* Short form on mobile, full form on desktop */}
          <span
            className="
              text-text-primary font-extrabold uppercase tracking-widest
              text-[11px] sm:text-[13px] lg:text-sm
            "
          >
            <span className="lg:hidden">GH Civic RAG</span>
            <span className="hidden lg:inline">Ghana Civic RAG</span>
          </span>
          <span className="text-[9px] sm:text-[10px] text-text-muted font-medium tracking-wider uppercase">
            ACity · CS4241
          </span>
        </div>
      </div>

      {/* ── Right: actions ── */}
      <div className="flex items-center gap-2">
        {/* Settings button — icon only on mobile, labelled on desktop */}
        <button
          type="button"
          onClick={onSettingsOpen}
          aria-label="Open settings"
          className="
            flex items-center gap-1.5
            min-w-[44px] min-h-[44px] px-3
            rounded-xl text-text-secondary
            hover:text-ghana-gold hover:bg-[var(--bg-elevated)]
            active:scale-95
            transition-all duration-200
            focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
          "
        >
          <Settings size={18} />
          <span className="hidden lg:inline text-sm font-medium">Settings</span>
        </button>
      </div>
    </header>
  );
}
