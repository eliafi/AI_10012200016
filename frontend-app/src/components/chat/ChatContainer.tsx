"use client";

import { useEffect, useRef, useState, ReactNode } from "react";
import type { ChatMessage } from "@/lib/types";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";
import WelcomeScreen from "./WelcomeScreen";
import ChatInput from "./ChatInput";

interface Props {
  messages: ChatMessage[];
  isLoading: boolean;
  onSend: (text: string) => void;
  /**
   * Given a bot message, return the mobile inspection node
   * (SourceAccordion + PipelineTimeline). Supplied by Phase 5.
   * Falls back to null until then.
   */
  renderMobileInspection?: (message: ChatMessage) => ReactNode;
}

/**
 * Scrollable message list.
 *
 * - Auto-scrolls to the bottom whenever messages or loading state change.
 * - Shows WelcomeScreen when empty.
 * - Suggestion clicks pre-fill ChatInput via local state.
 * - On mobile the list has bottom padding so the fixed input bar never
 *   obscures the last message.
 */
export default function ChatContainer({
  messages,
  isLoading,
  onSend,
  renderMobileInspection,
}: Props) {
  const bottomRef = useRef<HTMLDivElement>(null);
  const [prefill, setPrefill] = useState<string | undefined>();

  /* Auto-scroll to the latest message */
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  function handleSuggestion(text: string) {
    setPrefill(text);
  }

  const isEmpty = messages.length === 0;

  return (
    <div className="flex flex-col flex-1 min-h-0">
      {/* Scrollable area */}
      <div
        className="
          flex-1 overflow-y-auto scroll-touch
          py-4
          /* Bottom padding ensures last message clears the fixed input bar on mobile */
          pb-[80px] lg:pb-4
        "
      >
        {isEmpty ? (
          <WelcomeScreen onSuggestion={handleSuggestion} />
        ) : (
          <div className="flex flex-col gap-1">
            {messages.map((msg) => (
              <MessageBubble
                key={msg.id}
                message={msg}
                mobileInspection={
                  msg.role === "assistant" && renderMobileInspection
                    ? renderMobileInspection(msg)
                    : undefined
                }
              />
            ))}

            {/* Typing indicator while waiting for response */}
            {isLoading && <TypingIndicator />}

            {/* Scroll anchor */}
            <div ref={bottomRef} />
          </div>
        )}
      </div>

      {/* Input bar — fixed on mobile, inline on desktop */}
      <ChatInput
        onSend={onSend}
        disabled={isLoading}
        prefill={prefill}
        onPrefillConsumed={() => setPrefill(undefined)}
      />
    </div>
  );
}
