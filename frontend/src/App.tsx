import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";

function App() {
  return (
    <div className="h-screen w-screen bg-slate-100 overflow-hidden">
      <div className="flex h-full">

        {/* Sidebar */}
        <Sidebar />

        {/* Main Area */}
        <main className="flex-1 p-8 overflow-hidden">

          <div className="h-full rounded-3xl bg-white shadow-2xl border border-slate-200 overflow-hidden">

            <ChatWindow />

          </div>

        </main>

      </div>
    </div>
  );
}

export default App;