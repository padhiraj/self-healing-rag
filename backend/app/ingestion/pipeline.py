from pathlib import Path

from backend.app.ingestion.loader import load_pdf
from backend.app.ingestion.chunker import split_documents
from backend.app.vectorstore.chroma_store import create_vector_store


class IngestionPipeline:
    """
    Complete document ingestion pipeline.
    """

    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[3]
        self.pdf_path = self.project_root / "data" / "Velar-whitepaper.pdf"

    def run(self):
        print("\n🚀 Starting Ingestion Pipeline...\n")

        # Step 1: Load PDF
        documents = load_pdf(str(self.pdf_path))
        print(f"✅ Loaded {len(documents)} pages")

        # Step 2: Split Documents
        chunks = split_documents(documents)
        print(f"✅ Created {len(chunks)} chunks")

        # Step 3: Store in ChromaDB
        create_vector_store(chunks)
        print("✅ Stored embeddings in ChromaDB")

        print("\n🎉 Ingestion Completed Successfully!\n")