"use client";

import {
  useRef,
  useState,
  useEffect,
  KeyboardEvent,
  FormEvent,
} from "react";
import { Send } from "lucide-react";

interface Props {
  onSend: (text: string) => void;
  disabled?: boolean;
  /** Pre-fill the input (e.g. from a suggestion click) */
  prefill?: string;
  onPrefillConsumed?: () => void;
}

/**
 * Chat input bar.
 *
 * Mobile  (<lg): fixed to the bottom of the viewport, gold focus ring,
 *                safe-area padding for notched phones.
 * Desktop (lg+): sits inline at the bottom of the chat panel (relative).
 *
 * Behaviour:
 * - Textarea auto-grows up to max-h-32 then scrolls.
 * - Enter submits; Shift+Enter inserts a newline.
 * - Disabled while the backend is responding.
 */
export default function ChatInput({
  onSend,
  disabled = false,
  prefill,
  onPrefillConsumed,
}: Props) {
  const [value, setValue] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  /* Apply prefill from suggestion clicks */
  useEffect(() => {
    if (prefill) {
      setValue(prefill);
      onPrefillConsumed?.();
      textareaRef.current?.focus();
    }
  }, [prefill, onPrefillConsumed]);

  /* Auto-resize textarea to fit content */
  useEffect(() => {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${Math.min(el.scrollHeight, 128)}px`;
  }, [value]);

  function submit() {
    const trimmed = value.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setValue("");
    if (textareaRef.current) textareaRef.current.style.height = "auto";
  }

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      submit();
    }
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    submit();
  }

  const canSend = value.trim().length > 0 && !disabled;

  return (
    /*
     * Mobile:  fixed bottom-0, full width, dark blurred background,
     *          safe-area-bottom padding for notched phones.
     * Desktop: relative, no background override, blends into panel.
     */
    <div
      className="
        fixed bottom-0 left-0 right-0 z-30
        lg:relative lg:bottom-auto lg:left-auto lg:right-auto lg:z-auto
        px-4 pb-4 pt-3
        bg-[var(--bg-deep)]/90 backdrop-blur-md
        lg:bg-transparent lg:backdrop-blur-none
        safe-area-bottom
        border-t border-[var(--border-subtle)]
        lg:border-t-0 lg:px-4 lg:py-4
      "
    >
      <form onSubmit={handleSubmit} className="flex items-end gap-2">
        <textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={disabled}
          rows={1}
          placeholder="Ask about Ghana elections or budget…"
          aria-label="Chat message input"
          className="
            flex-1 resize-none
            bg-[var(--bg-elevated)]/80 backdrop-blur-sm
            border border-[var(--border-subtle)]
            rounded-2xl
            px-4 py-3
            text-sm text-text-primary placeholder:text-text-muted
            min-h-[48px] max-h-32
            overflow-y-auto scroll-touch
            transition-[border-color,box-shadow] duration-200
            focus:outline-none focus:border-[rgba(252,209,22,0.4)]
            focus:shadow-[0_0_0_2px_rgba(252,209,22,0.12)]
            disabled:opacity-50 disabled:cursor-not-allowed
          "
        />

        {/* Send button */}
        <button
          type="submit"
          disabled={!canSend}
          aria-label="Send message"
          className="
            min-w-[48px] min-h-[48px]
            flex items-center justify-center
            rounded-xl shrink-0
            transition-all duration-200
            active:scale-95
            focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/60
            disabled:opacity-30 disabled:cursor-not-allowed disabled:active:scale-100
            bg-gradient-to-br from-[#D4A017] to-[#FCD116]
            text-[#0B0F1A]
          "
        >
          <Send size={18} />
        </button>
      </form>

      <p className="hidden lg:block text-[10px] text-text-muted mt-1.5 text-right">
        Enter to send · Shift+Enter for new line
      </p>
    </div>
  );
}
