"use client";

import { useCallback, useState } from "react";
import ChatContainer from "@/components/chat/ChatContainer";
import AppShell from "@/components/layout/AppShell";
import InspectionPanel from "@/components/rag/InspectionPanel";
import SourceAccordion from "@/components/rag/SourceAccordion";
import SettingsPanel from "@/components/settings/SettingsPanel";
import useChat from "@/hooks/useChat";
import useMediaQuery from "@/hooks/useMediaQuery";
import {
  DEFAULT_SETTINGS,
  type ChatMessage,
  type ChatSettings,
} from "@/lib/types";

export default function Home() {
  const [settings, setSettings] = useState<ChatSettings>({ ...DEFAULT_SETTINGS });
  const { messages, isLoading, latestRagData, sendMessage } = useChat();
  const isDesktop = useMediaQuery("(min-width: 1024px)");

  const handleSend = useCallback(
    (text: string) => {
      void sendMessage(text, settings);
    },
    [sendMessage, settings]
  );

  const renderMobileInspection = useCallback(
    (message: ChatMessage) => {
      if (isDesktop || !message.ragData) {
        return null;
      }

      return <SourceAccordion ragData={message.ragData} />;
    },
    [isDesktop]
  );

  return (
    <AppShell
      chatPanel={
        <ChatContainer
          messages={messages}
          isLoading={isLoading}
          onSend={handleSend}
          renderMobileInspection={renderMobileInspection}
        />
      }
      inspectionPanel={
        isDesktop ? (
          <InspectionPanel ragData={latestRagData} isLoading={isLoading} />
        ) : null
      }
      settingsContent={
        <SettingsPanel
          settings={settings}
          onChange={setSettings}
          onReset={() => setSettings({ ...DEFAULT_SETTINGS })}
        />
      }
    />
  );
}
