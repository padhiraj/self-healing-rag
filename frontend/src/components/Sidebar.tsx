function Sidebar() {
  return (
    <aside className="w-80 h-screen bg-[#0F172A] text-white flex flex-col">

      {/* ---------------- Logo ---------------- */}
      <div className="flex flex-col items-center pt-10 pb-8">

        <div className="h-20 w-20 rounded-3xl bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-2xl">
          <span className="text-4xl font-bold">AI</span>
        </div>

        <h1 className="mt-8 text-5xl font-bold tracking-tight text-center leading-tight">
          Self-Healing
        </h1>

        <h2 className="text-3xl font-bold text-blue-400 mt-2">
          RAG
        </h2>

        <p className="text-gray-400 mt-3 text-lg">
          Velar AI Assistant
        </p>
      </div>

      <div className="border-t border-slate-700"></div>

      {/* ---------------- Cards ---------------- */}

      <div className="flex-1 overflow-y-auto px-6 py-8 space-y-6">

        {/* MODEL */}

        <div className="bg-[#1E293B] rounded-3xl p-6 shadow-lg border border-slate-700">

          <p className="uppercase text-xs tracking-widest text-gray-400">
            MODEL
          </p>

          <h3 className="text-3xl font-bold mt-2">
            Llama 3
          </h3>

          <p className="text-gray-400 mt-2">
            Powered by Groq
          </p>

        </div>

        {/* KNOWLEDGE */}

        <div className="bg-[#1E293B] rounded-3xl p-6 shadow-lg border border-slate-700">

          <p className="uppercase text-xs tracking-widest text-gray-400">
            KNOWLEDGE BASE
          </p>

          <h3 className="text-2xl font-bold mt-2">
            Velar Whitepaper
          </h3>

          <p className="text-gray-400 mt-2">
            Fully Indexed
          </p>

        </div>

        {/* FEATURES */}

        <div className="bg-[#1E293B] rounded-3xl p-6 shadow-lg border border-slate-700">

          <p className="uppercase text-xs tracking-widest text-gray-400 mb-5">
            FEATURES
          </p>

          <div className="space-y-4">

            <div className="flex items-center gap-3">
              <div className="h-2.5 w-2.5 rounded-full bg-emerald-400"></div>
              <span>Query Rewriting</span>
            </div>

            <div className="flex items-center gap-3">
              <div className="h-2.5 w-2.5 rounded-full bg-emerald-400"></div>
              <span>Retry Engine</span>
            </div>

            <div className="flex items-center gap-3">
              <div className="h-2.5 w-2.5 rounded-full bg-emerald-400"></div>
              <span>Semantic Reranking</span>
            </div>

            <div className="flex items-center gap-3">
              <div className="h-2.5 w-2.5 rounded-full bg-emerald-400"></div>
              <span>Knowledge Gap Detection</span>
            </div>

            <div className="flex items-center gap-3">
              <div className="h-2.5 w-2.5 rounded-full bg-emerald-400"></div>
              <span>Confidence Scoring</span>
            </div>

            <div className="flex items-center gap-3">
              <div className="h-2.5 w-2.5 rounded-full bg-emerald-400"></div>
              <span>Conversation Memory</span>
            </div>

          </div>

        </div>

      </div>

      {/* ---------------- Footer ---------------- */}

      <div className="border-t border-slate-700 p-6">

        <div className="flex items-center">

          <div className="h-3.5 w-3.5 rounded-full bg-emerald-500 animate-pulse mr-3"></div>

          <div>

            <p className="font-semibold text-lg">
              Backend Connected
            </p>

            <p className="text-sm text-gray-400">
              Ready for chatting
            </p>

          </div>

        </div>

      </div>

    </aside>
  );
}

export default Sidebar;