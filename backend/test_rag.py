from backend.app.llm.rag_chain import ask


if __name__ == "__main__":

    question = input("Ask a question: ")

    answer = ask(question)

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(answer)