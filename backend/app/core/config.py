from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = "Self-Healing-RAG"
    API_VERSION: str = "v1"

    # LLM Settings
    GROQ_API_KEY: str
    MODEL_NAME: str = "llama-3.3-70b-versatile"

    # Vector DB
    CHROMA_DB_DIR: str = "chroma_db"

    # Embeddings
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore any extra variables in .env
    )


settings = Settings()