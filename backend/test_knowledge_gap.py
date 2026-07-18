from backend.app.self_healing.knowledge_gap_detector import detect_knowledge_gap

question = "Explain Velar Governance"

context = """
Velar Dharma is an Automated Market Maker built on Stacks.
It supports liquidity pools and token swaps.
"""

gap = detect_knowledge_gap(question, context)

print("Knowledge Gap:", gap)