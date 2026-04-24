"use client";

interface Option {
  value: string;
  label: string;
}

interface Props {
  label?: string;
  value: string;
  options: Option[];
  onChange: (value: string) => void;
  description?: string;
}

export default function ModelSelector({
  label = "llm_model",
  value,
  options,
  onChange,
  description,
}: Props) {
  return (
    <div className="flex flex-col gap-2">
      <label className="text-sm font-semibold text-text-primary">{label}</label>

      {description && (
        <p className="text-xs text-text-muted leading-relaxed">{description}</p>
      )}

      <div className="relative">
        <select
          value={value}
          onChange={(event) => onChange(event.target.value)}
          className="
            w-full min-h-[44px]
            rounded-xl
            border border-[var(--border-subtle)]
            bg-[var(--bg-elevated)]/75
            px-3 py-2.5 pr-10
            text-sm text-text-primary
            focus:outline-none focus:border-[rgba(252,209,22,0.45)]
            focus:shadow-[0_0_0_2px_rgba(252,209,22,0.12)]
          "
          aria-label={label}
        >
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>

        <span
          className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-text-muted"
          aria-hidden="true"
        >
          v
        </span>
      </div>
    </div>
  );
}
