import time
from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

from backend.app.core.logger import get_logger
from backend.app.llm.client import get_llm, get_groq_client
from backend.app.llm.prompts import RAG_PROMPT
from backend.app.memory.chat_history import get_chat_history
from backend.app.core.config import settings
from backend.app.vectorstore.retriever import get_retriever

from backend.app.self_healing.retry_engine import retrieve_with_retry
from backend.app.self_healing.knowledge_gap_detector import detect_knowledge_gap
from backend.app.self_healing.confidence_engine import calculate_confidence
from backend.app.self_healing.query_rewritter import rewrite_query
from backend.app.analytics.logger import log_query

logger = get_logger(__name__)


def ask(question: str, session_id: str):

    start_time = time.time()

    logger.info("=" * 80)
    logger.info(f"Original Question: {question}")

    # -------------------------------------------------
    # Self-Healing Retrieval Pipeline
    # -------------------------------------------------

    docs, retrieval_grade, rewritten_query, retry_count, retrieved_docs = (
        retrieve_with_retry(question)
    )

    logger.info(f"Rewritten Query : {rewritten_query}")
    logger.info(f"Retrieval Grade : {retrieval_grade}")

    # -------------------------------------------------
    # Chat History
    # -------------------------------------------------

    history = get_chat_history(session_id)

    history_text = ""

    for message in history.messages:

        if isinstance(message, HumanMessage):
            history_text += f"User: {message.content}\n"

        elif isinstance(message, AIMessage):
            history_text += f"Assistant: {message.content}\n"

    # -------------------------------------------------
    # Context
    # -------------------------------------------------

    context = "\n\n".join(doc.page_content for doc in docs)

    # -------------------------------------------------
    # Knowledge Gap
    # -------------------------------------------------

    knowledge_gap = detect_knowledge_gap(
        question=question,
        context=context,
    )

    logger.info(f"Knowledge Gap : {knowledge_gap}")

    # -------------------------------------------------
    # Prompt
    # -------------------------------------------------

    prompt = RAG_PROMPT.invoke(
        {
            "history": history_text,
            "context": context,
            "question": question,
        }
    )

    # -------------------------------------------------
    # LLM
    # -------------------------------------------------

    llm = get_llm()

    response = llm.invoke(prompt)

    answer = response.content

    # -------------------------------------------------
    # Save History
    # -------------------------------------------------

    history.add_user_message(question)
    history.add_ai_message(answer)

    # -------------------------------------------------
    # Confidence
    # -------------------------------------------------

    confidence = calculate_confidence(
        retrieval_grade=retrieval_grade,
        knowledge_gap=knowledge_gap,
        retry_count=retry_count,
        retrieved_docs=retrieved_docs,
        reranked_docs=len(docs),
    )

    # -------------------------------------------------
    # Sources
    # -------------------------------------------------

    sources = []

    for doc in docs:

        sources.append(
            {
                "page": doc.metadata.get("page", 0) + 1,
                "source": Path(doc.metadata.get("source")).name,
            }
        )

    # -------------------------------------------------
    # Response Time
    # -------------------------------------------------

    response_time = round(time.time() - start_time, 2)

    # -------------------------------------------------
    # Analytics
    # -------------------------------------------------

    log_query(
        question=question,
        rewritten_query=rewritten_query,
        retrieval_grade=retrieval_grade,
        knowledge_gap=knowledge_gap,
        confidence=confidence["score"],
        retry_count=retry_count,
        retrieved_docs=retrieved_docs,
        reranked_docs=len(docs),
        response_time=response_time,
    )

    return {
        "answer": answer,
        "sources": sources,
        "confidence": confidence,
        "analytics": {
            "rewritten_query": rewritten_query,
            "retrieval_grade": retrieval_grade,
            "knowledge_gap": knowledge_gap,
            "retry_count": retry_count,
            "response_time": response_time,
        },
    }

def stream_answer(question: str, session_id: str):

    logger.info("=" * 80)
    logger.info(f"Original Question: {question}")

    # -----------------------------
    # Self-Healing Pipeline
    # -----------------------------

    rewritten_question = rewrite_query(question)

    logger.info(f"Rewritten Query: {rewritten_question}")

    retriever = get_retriever()

    docs = retriever.invoke(rewritten_question)

    history = get_chat_history(session_id)

    history_text = ""

    for message in history.messages:

        if isinstance(message, HumanMessage):
            history_text += f"User: {message.content}\n"

        elif isinstance(message, AIMessage):
            history_text += f"Assistant: {message.content}\n"

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful AI assistant.

Use the previous conversation when answering follow-up questions.

If the answer is not available in the retrieved context,
clearly say you don't know.

Conversation History:

{history_text}

Retrieved Context:

{context}

Question:

{question}

Answer:
"""

    # -----------------------------
    # Native Groq Streaming
    # -----------------------------

    client = get_groq_client()

    stream = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
        stream=True,
    )

    full_answer = ""

    for chunk in stream:

        delta = chunk.choices[0].delta.content

        if delta:

            full_answer += delta

            yield delta

    history.add_user_message(question)
    history.add_ai_message(full_answer)