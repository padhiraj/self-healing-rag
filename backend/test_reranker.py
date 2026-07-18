from backend.app.self_healing.query_rewritter import rewrite_query
from backend.app.self_healing.reranker import rerank_documents
from backend.app.vectorstore.retriever import get_retriever

question = "Explain Dharma"

query = rewrite_query(question)

retriever = get_retriever()

docs = retriever.invoke(query)

print("\nRetrieved:", len(docs), "documents")

docs = rerank_documents(question, docs)

print("\nTop Documents\n")

for i, doc in enumerate(docs):

    print("=" * 70)

    print(f"Document {i+1}")

    print(doc.page_content[:350])