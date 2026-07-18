import { useState } from "react";

interface Props {
  onSend: (question: string) => void;
}

function ChatInput({ onSend }: Props) {
  const [question, setQuestion] = useState("");

  const handleSend = () => {
    if (!question.trim()) return;

    onSend(question);
    setQuestion("");
  };

  return (
    <div className="flex items-center gap-4">
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleSend();
        }}
        placeholder="Ask anything about the Velar Whitepaper..."
        className="
          flex-1
          rounded-2xl
          border
          border-slate-300
          bg-slate-50
          px-6
          py-4
          text-base
          outline-none
          transition-all
          focus:border-blue-500
          focus:ring-4
          focus:ring-blue-100
        "
      />

      <button
        onClick={handleSend}
        className="
          rounded-2xl
          bg-gradient-to-r
          from-blue-600
          to-indigo-600
          px-8
          py-4
          font-semibold
          text-white
          shadow-lg
          transition
          hover:scale-105
          hover:shadow-xl
        "
      >
        Send
      </button>
    </div>
  );
}

export default ChatInput;