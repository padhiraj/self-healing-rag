from groq import Groq
from langchain_groq import ChatGroq

from backend.app.core.config import settings


def get_llm(streaming: bool = False):
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.MODEL_NAME,
        temperature=0,
        streaming=streaming,
    )


def get_groq_client():
    return Groq(
        api_key=settings.GROQ_API_KEY,
    )