"use client";

import BallotGlassCard from "@/components/ui/BallotGlassCard";
import GoldButton from "@/components/ui/GoldButton";
import {
  DEFAULT_SETTINGS,
  LLM_MODELS,
  type ChatSettings,
} from "@/lib/types";
import ModelSelector from "./ModelSelector";
import SliderInput from "./SliderInput";

interface Props {
  settings: ChatSettings;
  onChange: (next: ChatSettings) => void;
  onReset?: () => void;
}

export default function SettingsPanel({ settings, onChange, onReset }: Props) {
  function update<K extends keyof ChatSettings>(key: K, value: ChatSettings[K]) {
    onChange({ ...settings, [key]: value });
  }

  function handleReset() {
    if (onReset) {
      onReset();
      return;
    }

    onChange({ ...DEFAULT_SETTINGS });
  }

  return (
    <BallotGlassCard noHover className="p-4 sm:p-5 flex flex-col gap-5">
      <div className="flex flex-col gap-1">
        <h2 className="text-base font-semibold text-text-primary">Query Settings</h2>
        <p className="text-xs text-text-muted leading-relaxed">
          Tune retrieval and model parameters before sending a query.
        </p>
      </div>

      <SliderInput
        label="top_k"
        value={settings.top_k}
        min={1}
        max={20}
        step={1}
        description="Number of retrieved chunks considered for ranking."
        valueFormatter={(value) => `${Math.round(value)}`}
        onChange={(value) => update("top_k", Math.round(value))}
      />

      <SliderInput
        label="hybrid_alpha"
        value={settings.hybrid_alpha}
        min={0}
        max={1}
        step={0.01}
        description="Blend weight between vector and keyword similarity."
        valueFormatter={(value) => value.toFixed(2)}
        onChange={(value) => update("hybrid_alpha", value)}
      />

      <ModelSelector
        value={settings.llm_model}
        options={LLM_MODELS}
        description="Model used for final answer generation."
        onChange={(value) => update("llm_model", value)}
      />

      <div className="border-t border-[var(--border-subtle)] pt-4 flex items-center justify-between gap-3">
        <p className="text-[11px] text-text-muted leading-relaxed">
          Defaults: top_k 5, hybrid_alpha 0.55, llm_model gpt-4o-mini.
        </p>

        <GoldButton
          type="button"
          className="min-h-[44px] px-4 py-2 text-sm"
          onClick={handleReset}
        >
          Reset
        </GoldButton>
      </div>
    </BallotGlassCard>
  );
}
