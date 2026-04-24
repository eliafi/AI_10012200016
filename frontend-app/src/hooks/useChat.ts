"use client";

import { useCallback, useRef, useState } from "react";
import { postQuery } from "@/lib/api";
import type {
  ChatMessage,
  ChatSettings,
  QueryResponse,
} from "@/lib/types";

interface UseChatResult {
  messages: ChatMessage[];
  isLoading: boolean;
  latestRagData: QueryResponse | null;
  error: string | null;
  sendMessage: (text: string, settings: ChatSettings) => Promise<void>;
}

function createId(prefix: string): string {
  if (typeof crypto !== "undefined" && typeof crypto.randomUUID === "function") {
    return `${prefix}-${crypto.randomUUID()}`;
  }

  return `${prefix}-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

export default function useChat(): UseChatResult {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [latestRagData, setLatestRagData] = useState<QueryResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const requestInFlightRef = useRef(false);

  const sendMessage = useCallback(
    async (text: string, settings: ChatSettings) => {
      const query = text.trim();
      if (!query || requestInFlightRef.current) {
        return;
      }

      const userMessage: ChatMessage = {
        id: createId("user"),
        role: "user",
        content: query,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, userMessage]);
      setError(null);
      setIsLoading(true);
      requestInFlightRef.current = true;

      try {
        const ragData = await postQuery({
          query,
          top_k: settings.top_k,
          hybrid_alpha: settings.hybrid_alpha,
          llm_model: settings.llm_model,
          max_context_tokens: settings.max_context_tokens,
        });

        const assistantMessage: ChatMessage = {
          id: createId("assistant"),
          role: "assistant",
          content: ragData.response?.trim() || "No response returned.",
          ragData,
          timestamp: new Date(),
        };

        setMessages((prev) => [...prev, assistantMessage]);
        setLatestRagData(ragData);
      } catch (unknownError) {
        const detail =
          unknownError instanceof Error ? unknownError.message : "Unknown error";

        setError(detail);

        const errorMessage: ChatMessage = {
          id: createId("assistant-error"),
          role: "assistant",
          content: `Request failed: ${detail}`,
          timestamp: new Date(),
        };

        setMessages((prev) => [...prev, errorMessage]);
      } finally {
        requestInFlightRef.current = false;
        setIsLoading(false);
      }
    },
    []
  );

  return {
    messages,
    isLoading,
    latestRagData,
    error,
    sendMessage,
  };
}
