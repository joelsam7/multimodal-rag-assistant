from pathlib import Path
from app.services.pdf_service import pdf_service
from fastapi import APIRouter, File, UploadFile
from app.services.embedding_service import embedding_service
from app.services.chunk_service import chunk_service
from app.services.chroma_service import chroma_service
router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = ""
    chunks = []
    
    if file.filename.lower().endswith(".pdf"):

        pages = pdf_service.extract_pages(str(file_path))

        chunks = chunk_service.chunk_pages(pages)

        chunk_texts = [chunk["text"] for chunk in chunks]

        embeddings = embedding_service.create_embeddings(chunk_texts)

        chroma_service.add_document(
            file.filename,
            chunks,
            embeddings
        )
    return {
    "filename": file.filename,
    "message": "Document indexed successfully",
    "chunks": len(chunks),
    "embedding_dimension": len(embeddings[0]),
    "status": "Stored in ChromaDB"
}