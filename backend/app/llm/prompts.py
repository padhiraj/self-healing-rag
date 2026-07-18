from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Use the previous conversation when answering follow-up questions.

If the answer is not available in the retrieved context, clearly say you don't know.

==============================
Conversation History
==============================

{history}

==============================
Retrieved Context
==============================

{context}

==============================
Current Question
==============================

{question}

Answer:
"""
)