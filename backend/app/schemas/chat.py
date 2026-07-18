from pydantic import BaseModel


# -------------------------------
# Request
# -------------------------------

class ChatRequest(BaseModel):
    session_id: str
    question: str


# -------------------------------
# Source
# -------------------------------

class Source(BaseModel):
    page: int
    source: str


# -------------------------------
# Confidence
# -------------------------------

class Confidence(BaseModel):
    score: int
    level: str


# -------------------------------
# Analytics
# -------------------------------

class Analytics(BaseModel):
    rewritten_query: str
    retrieval_grade: str
    knowledge_gap: bool
    retry_count: int
    response_time: float


# -------------------------------
# Response
# -------------------------------

class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]

    confidence: Confidence

    analytics: Analytics