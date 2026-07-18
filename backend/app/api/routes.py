from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.app.llm.rag_chain import ask, stream_answer
from backend.app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


# ---------------------------------
# Normal Chat Endpoint
# ---------------------------------
@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = ask(
        question=request.question,
        session_id=request.session_id,
    )

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"],
        analytics=result["analytics"],
    )


# ---------------------------------
# Streaming Chat Endpoint
# ---------------------------------
@router.post("/chat/stream")
def stream_chat(request: ChatRequest):

    return StreamingResponse(
    stream_answer(
        question=request.question,
        session_id=request.session_id,
    ),
    media_type="text/event-stream",
)