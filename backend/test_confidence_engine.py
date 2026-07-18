from backend.app.self_healing.confidence_engine import calculate_confidence

result = calculate_confidence(
    retrieval_grade="MEDIUM",
    knowledge_gap=False,
    retry_count=1,
    retrieved_docs=8,
    reranked_docs=3,
)

print(result)