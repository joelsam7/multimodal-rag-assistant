from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="Enterprise Multi-Modal RAG Assistant",
    description="An AI-powered assistant for enterprise document search and analysis.",
    version="1.0.0",
)

app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "project": "Enterprise Multi-Modal RAG Assistant",
        "version": "1.0.0",
        "status": "Running",
        "docs": "/docs"
    }