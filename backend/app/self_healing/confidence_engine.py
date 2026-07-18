def calculate_confidence(
    retrieval_grade: str,
    knowledge_gap: bool,
    retry_count: int,
    retrieved_docs: int,
    reranked_docs: int,
) -> dict:
    """
    Calculate confidence score for the generated answer.

    Returns:
    {
        "score": 91,
        "level": "HIGH"
    }
    """

    score = 0

    # ---------------------------------------
    # Retrieval Grade
    # ---------------------------------------

    if retrieval_grade == "HIGH":
        score += 40

    elif retrieval_grade == "MEDIUM":
        score += 25

    else:
        score += 10

    # ---------------------------------------
    # Knowledge Gap
    # ---------------------------------------

    if not knowledge_gap:
        score += 25

    # ---------------------------------------
    # Retry Count
    # ---------------------------------------

    if retry_count == 0:
        score += 15

    elif retry_count == 1:
        score += 10

    else:
        score += 5

    # ---------------------------------------
    # Retrieved Documents
    # ---------------------------------------

    if retrieved_docs >= 8:
        score += 10

    elif retrieved_docs >= 5:
        score += 7

    else:
        score += 5

    # ---------------------------------------
    # Reranked Documents
    # ---------------------------------------

    if reranked_docs == 3:
        score += 10

    elif reranked_docs == 2:
        score += 7

    else:
        score += 5

    # ---------------------------------------
    # Clamp Score
    # ---------------------------------------

    score = max(0, min(score, 100))

    # ---------------------------------------
    # Confidence Level
    # ---------------------------------------

    if score >= 85:
        level = "HIGH"

    elif score >= 60:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
    }