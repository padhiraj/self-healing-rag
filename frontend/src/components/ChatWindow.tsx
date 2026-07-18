import { useEffect, useRef, useState } from "react";
import ChatInput from "./ChatInput";
import ChatMessage from "./ChatMessage";
import { streamMessage, sendMessage } from "../api/chat";

interface Source {
  page: number;
  source: string;
}

interface Confidence {
  score: number;
  level: string;
}

interface Analytics {
  rewritten_query: string;
  retrieval_grade: string;
  knowledge_gap: boolean;
  retry_count: number;
  response_time: number;
}

interface Message {
  role: "user" | "assistant";
  content: string;
  confidence?: Confidence;
  analytics?: Analytics;
  sources?: Source[];
}

function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "👋 Hello! I'm your Self-Healing RAG Assistant. Ask me anything about the Velar Whitepaper.",
    },
  ]);

  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  const handleSend = async (question: string) => {
    // Add user + empty assistant message
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: question,
      },
      {
        role: "assistant",
        content: "",
      },
    ]);

    let fullResponse = "";

    try {
      // Stream answer
      await streamMessage(question, (chunk) => {
        fullResponse += chunk;

        setMessages((prev) => {
          const updated = [...prev];

          updated[updated.length - 1] = {
            ...updated[updated.length - 1],
            role: "assistant",
            content: fullResponse,
          };

          return updated;
        });
      });

      // Fetch metadata
      const result = await sendMessage(question);

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          content: fullResponse,
          confidence: result.confidence,
          analytics: result.analytics,
          sources: result.sources,
        };

        return updated;
      });
    } catch (err) {
      console.error(err);

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          content: "❌ Failed to connect to backend.",
        };

        return updated;
      });
    }
  };

  return (
    <div className="flex-1 flex justify-center items-center bg-slate-100 p-8">
      <div className="w-full max-w-6xl h-[92vh] bg-white rounded-[32px] shadow-2xl overflow-hidden flex flex-col">

        {/* Header */}
        <div className="border-b bg-white px-8 py-6">
          <h2 className="text-3xl font-bold text-slate-800 text-center">
            Self-Healing RAG Assistant
          </h2>

          <p className="text-center text-slate-500 mt-2">
            Intelligent AI powered by the Velar Whitepaper
          </p>
        </div>

        {/* Messages */}
        <div
          className="
            flex-1
            overflow-y-auto
            px-10
            py-8
            space-y-6
            bg-gradient-to-b
            from-slate-50
            via-white
            to-slate-100
          "
        >
          {messages.map((message, index) => (
            <ChatMessage
              key={index}
              role={message.role}
              content={message.content}
              confidence={message.confidence}
              analytics={message.analytics}
              sources={message.sources}
            />
          ))}

          <div ref={bottomRef} />
        </div>

        {/* Input */}
        <div className="border-t bg-white px-8 py-6 shadow-inner">
          <ChatInput onSend={handleSend} />
        </div>

      </div>
    </div>
  );
}

export default ChatWindow;