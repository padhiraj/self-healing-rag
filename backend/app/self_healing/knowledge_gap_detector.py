from backend.app.llm.client import get_llm


def detect_knowledge_gap(question: str, context: str) -> bool:
    """
    Returns True if the retrieved context
    is insufficient to answer the question.
    """

    llm = get_llm()

    prompt = f"""
You are evaluating retrieved documents for a Velar-only RAG system.

Question:
{question}

Retrieved Context:
{context}

Rules:

Return ENOUGH if:
- The retrieved context contains enough information to answer most or all of the user's question.
- Minor missing details are acceptable.
- The answer can be generated with reasonable confidence.

Return INSUFFICIENT only if:
- The retrieved context is mostly unrelated.
- The answer cannot be generated.
- Critical information is missing.

Return ONLY one word.

ENOUGH

or

INSUFFICIENT
"""

    response = llm.invoke(prompt)

    result = response.content.strip().upper()

    print("\n==============================")
    print("Knowledge Gap:", result)
    print("==============================\n")

    return result == "INSUFFICIENT"