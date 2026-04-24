"use client";

import { ChangeEvent } from "react";

interface Props {
  label: string;
  value: number;
  min: number;
  max: number;
  step: number;
  onChange: (value: number) => void;
  description?: string;
  valueFormatter?: (value: number) => string;
}

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value));
}

export default function SliderInput({
  label,
  value,
  min,
  max,
  step,
  onChange,
  description,
  valueFormatter,
}: Props) {
  const safeValue = clamp(value, min, max);
  const pct = ((safeValue - min) / (max - min)) * 100;

  function handleChange(event: ChangeEvent<HTMLInputElement>) {
    onChange(Number(event.target.value));
  }

  return (
    <div className="flex flex-col gap-2">
      <div className="flex items-center justify-between gap-3">
        <label className="text-sm font-semibold text-text-primary">{label}</label>
        <span className="font-mono text-xs text-ghana-gold">
          {valueFormatter ? valueFormatter(safeValue) : safeValue}
        </span>
      </div>

      {description && (
        <p className="text-xs text-text-muted leading-relaxed">{description}</p>
      )}

      <div className="flex flex-col gap-2">
        <div className="h-1.5 rounded-full bg-[var(--bg-elevated)] overflow-hidden">
          <div
            className="h-full rounded-full"
            style={{
              width: `${pct}%`,
              background: "var(--gradient-gold-shimmer)",
              transition: "width 250ms cubic-bezier(0.4, 0, 0.2, 1)",
            }}
          />
        </div>

        <input
          type="range"
          min={min}
          max={max}
          step={step}
          value={safeValue}
          onChange={handleChange}
          className="w-full accent-[#FCD116] min-h-[44px] cursor-pointer"
          aria-label={label}
        />
      </div>
    </div>
  );
}
