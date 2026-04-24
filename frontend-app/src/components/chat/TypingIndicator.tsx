/**
 * Animated "thinking" indicator — three gold dots bouncing sequentially.
 * Staggered delays (0s / 0.2s / 0.4s) defined in globals.css via
 * .dot-bounce:nth-child() selectors.
 */
export default function TypingIndicator() {
  return (
    <div className="flex items-start gap-2 px-4 py-2 animate-slide-in">
      {/* Bot bubble shape */}
      <div
        className="
          flex items-center gap-1.5
          ballot-glass px-4 py-3
          rounded-[20px_20px_20px_4px]
          max-w-[80px]
        "
        aria-label="Assistant is typing"
        role="status"
      >
        <span className="dot-bounce w-2 h-2 rounded-full bg-ghana-gold block" />
        <span className="dot-bounce w-2 h-2 rounded-full bg-ghana-gold block" />
        <span className="dot-bounce w-2 h-2 rounded-full bg-ghana-gold block" />
      </div>
    </div>
  );
}
