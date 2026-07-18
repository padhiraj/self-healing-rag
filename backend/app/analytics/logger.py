import json
from pathlib import Path
from datetime import datetime


# Create logs folder automatically
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Analytics log file
LOG_FILE = LOG_DIR / "analytics.jsonl"


def log_query(
    question: str,
    rewritten_query: str,
    retrieval_grade: str,
    knowledge_gap: bool,
    confidence: int,
    retry_count: int,
    retrieved_docs: int,
    reranked_docs: int,
    response_time: float,
):
    """
    Save one analytics record.
    """

    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "question": question,
        "rewritten_query": rewritten_query,
        "retrieval_grade": retrieval_grade,
        "knowledge_gap": knowledge_gap,
        "confidence": confidence,
        "retry_count": retry_count,
        "retrieved_docs": retrieved_docs,
        "reranked_docs": reranked_docs,
        "response_time": round(response_time, 2),
    }

    with open(LOG_FILE, "a") as file:
        file.write(json.dumps(record))
        file.write("\n")

    return record