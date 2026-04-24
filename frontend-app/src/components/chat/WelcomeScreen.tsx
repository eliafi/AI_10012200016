interface Props {
  onSuggestion: (text: string) => void;
}

const SUGGESTIONS = [
  "What were the results of the 2020 Ghana presidential election?",
  "Summarise Ghana's 2023 national budget highlights.",
  "Who won the parliamentary seat in Ablekuma North?",
  "What is Ghana's fiscal deficit target for 2024?",
];

/**
 * Hero welcome screen shown when the chat history is empty.
 * Features the Ghana tricolour gradient headline and suggested queries.
 */
export default function WelcomeScreen({ onSuggestion }: Props) {
  return (
    <div className="flex flex-col items-center justify-center flex-1 px-6 py-12 text-center">
      {/* Star + title */}
      <div className="mb-6 flex flex-col items-center gap-4">
        {/* Mini Black Star */}
        <svg
          viewBox="0 0 200 200"
          className="w-16 h-16 opacity-80"
          aria-hidden="true"
        >
          <defs>
            <linearGradient id="star-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%"   stopColor="#CE1126" />
              <stop offset="50%"  stopColor="#FCD116" />
              <stop offset="100%" stopColor="#006B3F" />
            </linearGradient>
          </defs>
          <polygon
            fill="url(#star-grad)"
            points="100,10 120.6,73.5 186.6,73.5 134.4,110.3 155,173.8 100,137 45,173.8 65.6,110.3 13.4,73.5 79.4,73.5"
          />
        </svg>

        <h1
          className="text-2xl sm:text-3xl font-extrabold uppercase tracking-widest"
          style={{ background: "var(--gradient-brand)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}
        >
          Ghana Civic RAG
        </h1>

        <p className="max-w-sm text-sm sm:text-base text-text-secondary leading-relaxed">
          Ask anything about Ghana&apos;s electoral results or national budget.
          Answers are grounded in retrieved documents with full source citations.
        </p>
      </div>

      {/* Suggested queries */}
      <div className="w-full max-w-lg flex flex-col gap-2.5">
        <p className="text-xs font-semibold uppercase tracking-wider text-text-muted mb-1">
          Try asking
        </p>
        {SUGGESTIONS.map((s) => (
          <button
            key={s}
            type="button"
            onClick={() => onSuggestion(s)}
            className="
              w-full text-left text-sm text-text-secondary
              ballot-glass px-4 py-3 rounded-xl
              hover:text-ghana-gold hover:border-[rgba(252,209,22,0.18)]
              active:scale-[0.98]
              transition-all duration-200
              focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FCD116]/50
            "
          >
            {s}
          </button>
        ))}
      </div>
    </div>
  );
}
