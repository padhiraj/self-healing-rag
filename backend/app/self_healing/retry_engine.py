from backend.app.self_healing.query_rewritter import rewrite_query
from backend.app.self_healing.retreival_grader import grade_retrieval
from backend.app.vectorstore.retriever import get_retriever
from backend.app.self_healing.reranker import rerank_documents


def retrieve_with_retry(question: str, max_retries: int = 2):
    """
    Retrieve documents with automatic retry.

    Returns:
        docs
        retrieval_grade
        rewritten_query
        retry_count
        retrieved_docs
    """

    retriever = get_retriever()

    current_query = rewrite_query(question)

    for attempt in range(max_retries + 1):

        print("\n" + "=" * 70)
        print(f"Attempt {attempt + 1}")
        print("=" * 70)

        print("Search Query:")
        print(current_query)

        # -----------------------------
        # Retrieve Documents
        # -----------------------------
        raw_docs = retriever.invoke(current_query)

        retrieved_docs = len(raw_docs)

        # -----------------------------
        # Rerank
        # -----------------------------
        docs = rerank_documents(
            question=question,
            docs=raw_docs,
            top_k=3,
        )

        # -----------------------------
        # Grade Retrieval
        # -----------------------------
        context = "\n\n".join(doc.page_content for doc in docs)

        grade = grade_retrieval(question, context)

        print(f"Retrieval Grade: {grade}")

        if grade in ["HIGH", "MEDIUM"]:

            print("Retrieval Accepted")

            return (
                docs,
                grade,
                current_query,
                attempt,
                retrieved_docs,
            )

        print("Retrieval Rejected")

        current_query = rewrite_query(
            f"""
The previous retrieval was not good.

Rewrite the search query to improve retrieval.

Original Question:
{question}

Previous Search Query:
{current_query}
"""
        )

    return (
        docs,
        grade,
        current_query,
        max_retries,
        retrieved_docs,
    )