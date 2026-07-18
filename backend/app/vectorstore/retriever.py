from pathlib import Path

from langchain_chroma import Chroma
from backend.app.core.config import settings

from backend.app.embeddings.embedder import get_embedding_model


def get_retriever():

    project_root = Path(__file__).resolve().parents[3]

    persist_directory = project_root / settings.CHROMA_DB_DIR

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=str(persist_directory),
        embedding_function=embedding_model,
    )

    retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 8
    }
)

    return retriever