from backend.app.self_healing.retreival_grader import grade_retrieval

question = "Explain Dharma"

context = """
Bitcoin was introduced in 2009.

Ethereum supports smart contracts.
"""

grade = grade_retrieval(question, context)

print()
print("Final Grade:", grade)