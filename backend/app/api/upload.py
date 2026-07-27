from pathlib import Path
from app.services.pdf_service import pdf_service
from app.services.docx_service import docx_service
from fastapi import APIRouter, File, UploadFile
from app.services.embedding_service import embedding_service
from app.services.chunk_service import chunk_service
from app.services.chroma_service import chroma_service
from app.services.txt_service import txt_service
from app.services.image_service import image_service








router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    chunks = []
    embeddings = []

    filename = file.filename.lower()

    if filename.endswith(".pdf"):

        pages = pdf_service.extract_pages(str(file_path))

        chunks = chunk_service.chunk_pages(pages)


    elif filename.endswith(".docx"):

        text = docx_service.extract_text(str(file_path))

        pages = [
            {
                "page": 1,
                "text": text
            }
        ]

        chunks = chunk_service.chunk_pages(pages)
    elif filename.endswith(".txt"):

        text = txt_service.extract_text(str(file_path))

        pages = [
            {
                "page": 1,
                "text": text
            }
        ]

        chunks = chunk_service.chunk_pages(pages)

    elif filename.endswith((".png", ".jpg", ".jpeg")):

        text = image_service.extract_text(str(file_path))

        pages = [
            {
                "page": 1,
                "text": text
            }
        ]

        chunks = chunk_service.chunk_pages(pages)


    if chunks:

        chunk_texts = [
            chunk["text"]
            for chunk in chunks
        ]

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
        "embedding_dimension": len(embeddings[0]) if embeddings else 0,
        "status": "Stored in ChromaDB"
    }