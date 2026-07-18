import axios from "axios";

// Reads backend URL from environment
const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const API = axios.create({
  baseURL: API_URL,
});

// New session every browser refresh
const SESSION_ID = crypto.randomUUID();

export async function sendMessage(question: string) {
  const response = await API.post("/chat", {
    session_id: SESSION_ID,
    question,
  });

  return response.data;
}

export async function streamMessage(
  question: string,
  onChunk: (chunk: string) => void
) {
  const response = await fetch(`${API_URL}/chat/stream`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      session_id: SESSION_ID,
      question,
    }),
  });

  if (!response.body) {
    throw new Error("Streaming not supported.");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { value, done } = await reader.read();

    if (done) break;

    onChunk(decoder.decode(value));
  }
}