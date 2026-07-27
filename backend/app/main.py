from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.documents import router as documents_router
from app.api.image_chat import router as image_chat_router
from app.api.ask import router as ask_router
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


app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(documents_router)
app.include_router(image_chat_router)
app.include_router(ask_router)