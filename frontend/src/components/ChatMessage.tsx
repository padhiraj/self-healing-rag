import {
  Bot,
  User,
  Copy,
  FileText,
  Sparkles,
  Gauge,
} from "lucide-react";

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

interface ChatMessageProps {
  role: "user" | "assistant";
  content: string;
  confidence?: Confidence;
  analytics?: Analytics;
  sources?: Source[];
}

function ChatMessage({
  role,
  content,
  confidence,
  analytics,
  sources,
}: ChatMessageProps) {
  const isUser = role === "user";

  const copy = () => {
    navigator.clipboard.writeText(content);
  };

  return (
    <div
      className={`flex mb-6 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div className="flex gap-3 max-w-3xl">

        {/* Assistant Avatar */}

        {!isUser && (
          <div className="h-9 w-9 rounded-lg bg-gradient-to-r from-indigo-500 to-blue-600 flex items-center justify-center text-white shadow">
            <Bot size={18} />
          </div>
        )}

        <div>

          {/* Bubble */}

          <div
            className={`rounded-2xl shadow-md p-5 ${
              isUser
                ? "bg-gradient-to-r from-blue-600 to-indigo-600 text-white"
                : "bg-white border border-slate-200"
            }`}
          >

            {/* Header */}

            <div className="flex justify-between items-center mb-3">

              <h3 className="font-semibold text-base flex items-center gap-2">

                {isUser ? (
                  <>
                    <User size={16} />
                    You
                  </>
                ) : (
                  <>
                    <Bot size={16} />
                    Self-Healing Assistant
                  </>
                )}

              </h3>

              {!isUser && (
                <button
                  onClick={copy}
                  className="text-slate-400 hover:text-blue-600 transition"
                >
                  <Copy size={16} />
                </button>
              )}

            </div>

            {/* Answer */}

            <p className="text-sm leading-7 whitespace-pre-wrap text-slate-700">
              {content}
            </p>

            {/* Confidence */}

            {!isUser && confidence && (

              <div className="mt-5">

                <div className="flex justify-between items-center mb-2">

                  <span className="text-sm font-medium flex items-center gap-2">
                    <Gauge size={16} />
                    Confidence
                  </span>

                  <span className="text-sm font-semibold text-green-600">
                    {confidence.score}% • {confidence.level}
                  </span>

                </div>

                <div className="h-1.5 rounded-full bg-slate-200">

                  <div
                    className="h-1.5 rounded-full bg-gradient-to-r from-green-500 to-emerald-400"
                    style={{
                      width: `${confidence.score}%`,
                    }}
                  />

                </div>

              </div>

            )}

            {/* Analytics */}

            {!isUser && analytics && (

              <details className="mt-5">

                <summary className="cursor-pointer rounded-xl bg-slate-50 hover:bg-slate-100 px-4 py-3 font-medium flex justify-between">

                  <div className="flex items-center gap-2">

                    <Sparkles size={16} />

                    Self-Healing Analytics

                  </div>

                  ▼

                </summary>

                <div className="grid grid-cols-2 gap-3 mt-3">

                  <div className="bg-slate-50 rounded-lg p-3">
                    <p className="text-xs text-slate-500">
                      Rewritten Query
                    </p>

                    <p className="text-sm mt-1 font-medium break-words">
                      {analytics.rewritten_query}
                    </p>
                  </div>

                  <div className="bg-slate-50 rounded-lg p-3">
                    <p className="text-xs text-slate-500">
                      Retrieval Grade
                    </p>

                    <p className="text-sm font-medium">
                      {analytics.retrieval_grade}
                    </p>
                  </div>

                  <div className="bg-slate-50 rounded-lg p-3">
                    <p className="text-xs text-slate-500">
                      Knowledge Gap
                    </p>

                    <p className="text-sm font-medium">
                      {analytics.knowledge_gap ? "Yes" : "No"}
                    </p>
                  </div>

                  <div className="bg-slate-50 rounded-lg p-3">
                    <p className="text-xs text-slate-500">
                      Retries
                    </p>

                    <p className="text-sm font-medium">
                      {analytics.retry_count}
                    </p>
                  </div>

                  <div className="bg-slate-50 rounded-lg p-3 col-span-2">
                    <p className="text-xs text-slate-500">
                      Response Time
                    </p>

                    <p className="text-sm font-medium">
                      {analytics.response_time.toFixed(2)} sec
                    </p>
                  </div>

                </div>

              </details>

            )}

            {/* Sources */}

            {!isUser && sources && sources.length > 0 && (

              <details className="mt-5">

                <summary className="cursor-pointer rounded-xl bg-slate-50 hover:bg-slate-100 px-4 py-3 font-medium flex justify-between">

                  <div className="flex items-center gap-2">

                    <FileText size={16} />

                    Sources ({sources.length})

                  </div>

                  ▼

                </summary>

                <div className="space-y-2 mt-3">

                  {sources.map((source, index) => (

                    <div
                      key={index}
                      className="rounded-lg border border-slate-200 bg-slate-50 px-3 py-2 flex items-center gap-3"
                    >

                      <FileText
                        size={16}
                        className="text-indigo-600"
                      />

                      <div>

                        <p className="text-sm font-medium">
                          {source.source}
                        </p>

                        <p className="text-xs text-slate-500">
                          Page {source.page}
                        </p>

                      </div>

                    </div>

                  ))}

                </div>

              </details>

            )}

          </div>

        </div>

        {/* User Avatar */}

        {isUser && (
          <div className="h-9 w-9 rounded-lg bg-blue-600 flex items-center justify-center text-white shadow">
            <User size={17} />
          </div>
        )}

      </div>
    </div>
  );
}

export default ChatMessage;