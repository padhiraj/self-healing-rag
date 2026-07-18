from backend.app.vectorstore.retriever import get_retriever


def main():

    retriever = get_retriever()

    query = "What is Velar?"

    docs = retriever.invoke(query)

    print("\nRetrieved Chunks\n")

    for i, doc in enumerate(docs, start=1):
        print("=" * 70)
        print(f"Chunk {i}")
        print("=" * 70)

        print(doc.page_content[:500])

        print()


if __name__ == "__main__":
    main()