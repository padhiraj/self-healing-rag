from backend.app.analytics.logger import log_query

record = log_query(
    question="Explain Dharma",
    rewritten_query="Explain Velar V1 Dharma",
    retrieval_grade="HIGH",
    knowledge_gap=False,
    confidence=96,
    retry_count=0,
    retrieved_docs=8,
    reranked_docs=3,
    response_time=1.42,
)

print("\nAnalytics Record\n")
print(record)