import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
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
  const response = await fetch("http://127.0.0.1:8000/chat/stream", {
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