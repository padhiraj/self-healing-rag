def calculate_confidence(
    retrieval_grade: str,
    knowledge_gap: bool,
    retry_count: int,
    retrieved_docs: int,
    reranked_docs: int,
):

    score = 50  # Base confidence

    # -----------------------------
    # Retrieval Grade
    # -----------------------------

    if retrieval_grade == "HIGH":
        score += 30
    elif retrieval_grade == "MEDIUM":
        score += 15
    else:
        score -= 20

    # -----------------------------
    # Knowledge Gap
    # -----------------------------

    if knowledge_gap:
        score -= 30
    else:
        score += 10

    # -----------------------------
    # Retry Count
    # -----------------------------

    score -= retry_count * 8

    # -----------------------------
    # Retrieved Documents
    # -----------------------------

    if retrieved_docs >= 8:
        score += 10
    elif retrieved_docs >= 5:
        score += 5
    elif retrieved_docs >= 3:
        score += 2
    else:
        score -= 10

    # -----------------------------
    # Reranked Documents
    # -----------------------------

    if reranked_docs >= 5:
        score += 8
    elif reranked_docs >= 3:
        score += 5
    elif reranked_docs == 0:
        score -= 10

    # -----------------------------
    # Clamp
    # -----------------------------

    score = max(0, min(score, 98))

    # -----------------------------
    # Confidence Level
    # -----------------------------

    if score >= 90:
        level = "VERY HIGH"
    elif score >= 75:
        level = "HIGH"
    elif score >= 55:
        level = "MEDIUM"
    elif score >= 30:
        level = "LOW"
    else:
        level = "VERY LOW"

    return {
        "score": score,
        "level": level,
    }