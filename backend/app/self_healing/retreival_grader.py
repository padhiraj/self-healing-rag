from backend.app.llm.client import get_llm


def grade_retrieval(question: str, context: str) -> str:
    """
    Grades retrieval quality.

    Returns:
        HIGH
        MEDIUM
        LOW
    """

    llm = get_llm()

    prompt = f"""
You are an evaluator for a Self-Healing RAG system built ONLY for Velar documentation.

Evaluate how relevant the retrieved context is for answering the user's question.

Return ONLY one word.

Possible outputs:

HIGH
MEDIUM
LOW

Meaning:

HIGH
- Context completely answers the question.
- Retrieval is excellent.

MEDIUM
- Context is partially relevant.
- Some useful information exists.
- Answer can still be generated.

LOW
- Context is unrelated.
- Wrong topic.
- Missing required information.
- Retrieval should be retried.

Question:
{question}

Retrieved Context:
{context}
"""

    response = llm.invoke(prompt)

    score = response.content.strip().upper()

    if score not in ["HIGH", "MEDIUM", "LOW"]:
        score = "LOW"

    print("\n==============================")
    print("Retrieval Grade:", score)
    print("==============================\n")

    return score