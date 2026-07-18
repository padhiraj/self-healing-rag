from pathlib import Path

from backend.app.ingestion.loader import load_pdf
from backend.app.ingestion.chunker import split_documents

project_root = Path(__file__).resolve().parents[1]
pdf_path = project_root / "data" / "Velar-whitepaper.pdf"

docs = load_pdf(str(pdf_path))
chunks = split_documents(docs)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    if "What is Velar" in chunk.page_content or "Velar is" in chunk.page_content:
        print("=" * 80)
        print(f"Chunk {i}")
        print(chunk.page_content[:1000])