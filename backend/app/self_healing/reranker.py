from backend.app.llm.client import get_llm


def rerank_documents(question: str, docs, top_k: int = 3):
    """
    Rerank retrieved documents using the LLM.

    Returns:
        Top-k most relevant documents.
    """

    llm = get_llm()

    scored_docs = []

    for doc in docs:

        prompt = f"""
You are evaluating retrieved documents for a Velar RAG system.

Question:
{question}

Document:
{doc.page_content}

Rate how relevant this document is.

Return ONLY one integer from 1 to 10.

10 = Perfect
8 = Very Relevant
5 = Somewhat Relevant
1 = Irrelevant
"""

        response = llm.invoke(prompt)

        try:
            score = int(response.content.strip())
        except:
            score = 1

        scored_docs.append((score, doc))

        print(f"Score: {score}")

    scored_docs.sort(key=lambda x: x[0], reverse=True)

    return [doc for score, doc in scored_docs[:top_k]]