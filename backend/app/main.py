from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes import router

app = FastAPI(
    title="Self-Healing RAG API",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://self-healing-kg2q6psnr-padhirajs-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "Self-Healing RAG Backend is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }