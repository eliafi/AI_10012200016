"use client";

import { useState } from "react";
import { Copy, Check } from "lucide-react";
import Accordion from "@/components/ui/Accordion";

interface Props {
  prompt: string;
}

/**
 * Collapsible viewer for the final prompt sent to the LLM.
 * Displayed in JetBrains Mono inside a dark code surface.
 * Includes a copy-to-clipboard button that shows a tick confirmation.
 */
export default function PromptViewer({ prompt }: Props) {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(prompt);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // clipboard API not available (e.g. HTTP context) — silently ignore
    }
  }

  return (
    <Accordion
      title={
        <span className="flex items-center gap-2 text-sm font-medium text-text-secondary">
          <span className="text-ghana-gold font-mono text-xs">{"{ }"}</span>
          Final Prompt Sent to LLM
        </span>
      }
      defaultOpen={false}
      accent="muted"
    >
      {/* Code surface */}
      <div className="relative rounded-xl bg-[var(--bg-deep)] border border-[var(--border-subtle)] overflow-hidden">
        {/* Copy button */}
        <button
          type="button"
          onClick={handleCopy}
          aria-label="Copy prompt"
          className="
            absolute top-2 right-2 z-10
            flex items-center gap-1 px-2 py-1
            text-[10px] font-medium rounded-lg
            bg-[var(--bg-elevated)] border border-[var(--border-subtle)]
            text-text-muted hover:text-ghana-gold
            transition-colors duration-150
            min-h-[32px]
          "
        >
          {copied ? (
            <><Check size={11} className="text-ghana-green-bright" /><span className="text-ghana-green-bright">Copied</span></>
          ) : (
            <><Copy size={11} /><span>Copy</span></>
          )}
        </button>

        {/* Prompt text */}
        <pre
          className="
            overflow-x-auto scroll-touch
            p-4 pr-20
            text-[10px] sm:text-xs
            font-mono text-text-secondary leading-relaxed
            whitespace-pre-wrap break-words
            max-h-64
            overflow-y-auto
          "
        >
          {prompt}
        </pre>
      </div>
    </Accordion>
  );
}
