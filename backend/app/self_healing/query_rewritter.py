from backend.app.llm.client import get_llm


def rewrite_query(question: str) -> str:

    llm = get_llm()

    prompt = f"""
You are a query rewriting assistant for the Velar documentation.

Velar is a Bitcoin DeFi platform.

Important domain knowledge:
- Dharma = Velar v1
- Artha = Velar v2
- Kama = Velar v3
- Moksha = Velar v4

Your job is to rewrite user questions so they retrieve the correct Velar documents.

Rules:
- NEVER interpret words outside the Velar domain.
- If the user says "Dharma", assume they mean "Velar v1 Dharma".
- If the user says "Artha", assume "Velar v2 Artha".
- Keep the same meaning.
- Return ONLY the rewritten search query.

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()