from backend.app.self_healing.query_rewritter import rewrite_query

question = "Explain Dharma"

new_query = rewrite_query(question)

print("\nOriginal Question:")
print(question)

print("\nRewritten Query:")
print(new_query)