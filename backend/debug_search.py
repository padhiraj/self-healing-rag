from pathlib import Path

from backend.app.embeddings.embedder import get_embedding_model
from langchain_chroma import Chroma

project_root = Path(__file__).resolve().parents[1]

db = Chroma(
    persist_directory=str(project_root / "chroma_db"),
    embedding_function=get_embedding_model(),
)

results = db.similarity_search_with_score(
    "What is Velar?",
    k=5,
)

for i, (doc, score) in enumerate(results, 1):
    print("=" * 80)
    print(f"Result {i}")
    print(f"Score: {score}")
    print(doc.page_content[:500])