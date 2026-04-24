"use client";

import { useState, ReactNode } from "react";
import BlackStarBg from "./BlackStarBg";
import CivicHeader from "./CivicHeader";
import BottomSheet from "./BottomSheet";

interface Props {
  /** Left / main panel — takes 55% on desktop, 100% on mobile */
  chatPanel: ReactNode;
  /**
   * Right panel — 45% on desktop only.
   * On mobile this content is surfaced inside accordions in the chat panel,
   * so this prop can be null on mobile-only renders.
   */
  inspectionPanel: ReactNode;
  /** Content rendered inside the Settings bottom sheet / sidebar */
  settingsContent: ReactNode;
}

/**
 * Root responsive shell.
 *
 * Mobile  (<lg): single-column, header + full-width chat (input fixed to bottom)
 * Desktop (lg+): header + 55/45 side-by-side split, both panels scroll independently
 *
 * The BlackStarBg watermark sits behind everything via fixed positioning.
 */
export default function AppShell({ chatPanel, inspectionPanel, settingsContent }: Props) {
  const [settingsOpen, setSettingsOpen] = useState(false);

  return (
    <div className="relative flex flex-col min-h-svh bg-bg-deep">
      {/* Watermark behind all content */}
      <BlackStarBg />

      {/* Header — fixed height, shrinks on mobile */}
      <CivicHeader onSettingsOpen={() => setSettingsOpen(true)} />

      {/*
        Main content area — fills remaining viewport height.
        Mobile:  single column, chat fills everything.
        Desktop: flex-row, chat 55% | inspection 45%.
      */}
      <main className="relative z-10 flex flex-1 overflow-hidden">

        {/* ── Chat panel ─────────────────────────────────────── */}
        <section
          aria-label="Chat"
          className="
            flex flex-col
            w-full lg:w-[55%]
            min-h-0 overflow-hidden
          "
        >
          {chatPanel}
        </section>

        {/* ── Inspection panel (desktop only) ────────────────── */}
        <aside
          aria-label="RAG Inspection"
          className="
            hidden lg:flex flex-col
            w-[45%]
            min-h-0 overflow-y-auto scroll-touch
            border-l border-[var(--border-subtle)]
            bg-[var(--bg-surface)]/40
          "
        >
          {inspectionPanel}
        </aside>
      </main>

      {/* Settings bottom sheet (mobile) / sidebar (desktop) */}
      <BottomSheet
        isOpen={settingsOpen}
        onClose={() => setSettingsOpen(false)}
        title="Settings"
      >
        {settingsContent}
      </BottomSheet>
    </div>
  );
}
