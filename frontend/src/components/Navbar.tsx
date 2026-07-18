function Navbar() {
  return (
    <nav className="bg-blue-600 shadow-md">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1 className="text-white text-2xl font-bold">
          Self-Healing RAG
        </h1>

        <span className="text-white text-sm">
          Powered by FastAPI + Groq
        </span>
      </div>
    </nav>
  );
}

export default Navbar;