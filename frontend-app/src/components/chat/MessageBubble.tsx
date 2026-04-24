import { ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { ChatMessage } from "@/lib/types";

interface Props {
  message: ChatMessage;
  /**
   * Rendered below the bot bubble on mobile only (hidden on lg+).
   * Phase 5 passes the SourceAccordion + PipelineTimeline here.
   */
  mobileInspection?: ReactNode;
}

function Timestamp({ date }: { date: Date }) {
  return (
    <span className="text-[10px] text-text-muted mt-1 block">
      {date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
    </span>
  );
}

export default function MessageBubble({ message, mobileInspection }: Props) {
  const isUser = message.role === "user";

  if (isUser) {
    return (
      /* User message — right-aligned, gold gradient */
      <div className="flex flex-col items-end px-4 py-1 animate-slide-in">
        <div
          className="
            bg-gradient-to-br from-[#D4A017] to-[#FCD116]
            text-[#0B0F1A] font-medium
            px-4 py-3
            rounded-[20px_20px_4px_20px]
            max-w-[75%] sm:max-w-[65%]
            text-sm sm:text-[15px] leading-relaxed
            shadow-sm
          "
        >
          {message.content}
        </div>
        <Timestamp date={message.timestamp} />
      </div>
    );
  }

  /* Bot message — left-aligned, Ballot Box Glass */
  return (
    <div className="flex flex-col items-start px-4 py-1 animate-slide-in">
      <div
        className="
          ballot-glass
          px-4 py-3
          rounded-[20px_20px_20px_4px]
          max-w-[85%] sm:max-w-[75%]
          text-sm sm:text-[15px] leading-relaxed text-text-primary
        "
      >
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            /* Inline code — monospace gold tint */
            code: ({ children, ...rest }) => (
              <code
                className="font-mono text-ghana-gold bg-[rgba(252,209,22,0.08)] px-1.5 py-0.5 rounded text-[0.85em]"
                {...rest}
              >
                {children}
              </code>
            ),
            /* Code blocks */
            pre: ({ children }) => (
              <pre className="bg-[var(--bg-elevated)] rounded-xl p-3 my-2 overflow-x-auto text-[0.8em] font-mono text-text-secondary">
                {children}
              </pre>
            ),
            /* Links */
            a: ({ children, href }) => (
              <a
                href={href}
                target="_blank"
                rel="noopener noreferrer"
                className="text-ghana-gold underline underline-offset-2 hover:text-[#D4A017]"
              >
                {children}
              </a>
            ),
            /* Bold */
            strong: ({ children }) => (
              <strong className="font-semibold text-text-primary">{children}</strong>
            ),
            /* List items */
            li: ({ children }) => (
              <li className="ml-4 list-disc marker:text-ghana-gold">{children}</li>
            ),
          }}
        >
          {message.content}
        </ReactMarkdown>
      </div>

      <Timestamp date={message.timestamp} />

      {/* Mobile inspection slot — only shown below lg breakpoint */}
      {mobileInspection && (
        <div className="lg:hidden w-full max-w-[85%] mt-1">
          {mobileInspection}
        </div>
      )}
    </div>
  );
}
