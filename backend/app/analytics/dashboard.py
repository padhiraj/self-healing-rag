import json
from pathlib import Path

LOG_FILE = Path("logs/analytics.jsonl")


def generate_dashboard():
    """
    Read analytics logs and calculate project statistics.
    """

    if not LOG_FILE.exists():
        print("No analytics logs found.")
        return

    logs = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                logs.append(json.loads(line))

    if len(logs) == 0:
        print("No analytics data available.")
        return

    total_queries = len(logs)

    avg_confidence = sum(
        log["confidence"] for log in logs
    ) / total_queries

    avg_response_time = sum(
        log["response_time"] for log in logs
    ) / total_queries

    knowledge_gaps = sum(
        1 for log in logs if log["knowledge_gap"]
    )

    retries = sum(
        log["retry_count"] for log in logs
    )

    retrieval_success = sum(
        1
        for log in logs
        if log["retrieval_grade"] != "LOW"
    )

    retrieval_success_rate = (
        retrieval_success / total_queries
    ) * 100

    print("\n" + "=" * 50)
    print("      SELF-HEALING DASHBOARD")
    print("=" * 50)

    print(f"Total Queries          : {total_queries}")

    print(f"Average Confidence     : {avg_confidence:.2f}%")

    print(f"Average Response Time  : {avg_response_time:.2f} sec")

    print(f"Knowledge Gaps         : {knowledge_gaps}")

    print(f"Total Retries          : {retries}")

    print(f"Retrieval Success Rate : {retrieval_success_rate:.2f}%")

    print("=" * 50)