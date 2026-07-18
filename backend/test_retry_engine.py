from backend.app.self_healing.retry_engine import retrieve_with_retry

docs, grade, query, retry_count, retrieved_docs = retrieve_with_retry(
    "Explain Dharma"
)

print("\n" + "=" * 70)
print("Final Query")
print("=" * 70)
print(query)

print("\n" + "=" * 70)
print("Final Grade")
print("=" * 70)
print(grade)

print("\n" + "=" * 70)
print("Retry Count")
print("=" * 70)
print(retry_count)

print("\n" + "=" * 70)
print("Retrieved Documents")
print("=" * 70)
print(retrieved_docs)

print("\n" + "=" * 70)
print("Top Documents")
print("=" * 70)

for i, doc in enumerate(docs, start=1):
    print(f"\nDocument {i}\n")
    print(doc.page_content[:500])