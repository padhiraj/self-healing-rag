from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf(pdf_path: str):
    loader = PyMuPDFLoader(pdf_path)
    return loader.load()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]
    pdf_path = project_root / "data" / "Velar-whitepaper.pdf"

    docs = load_pdf(str(pdf_path))

    print("=" * 80)
    print(docs[9].page_content)
    print("=" * 80)