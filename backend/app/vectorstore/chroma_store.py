from pathlib import Path

from langchain_chroma import Chroma

from backend.app.embeddings.embedder import get_embedding_model


def create_vector_store(documents):
    """
    Create a Chroma vector database from document chunks.
    """

    project_root = Path(__file__).resolve().parents[3]

    persist_directory = project_root / "chroma_db"

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=str(persist_directory),
    )

    return vector_store