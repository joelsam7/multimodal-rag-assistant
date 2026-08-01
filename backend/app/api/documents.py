from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.services.chroma_service import chroma_service


router = APIRouter()


UPLOAD_DIR = Path("uploads")


@router.get("/documents")
async def list_documents():

    documents = chroma_service.list_documents()

    return {

        "documents": documents,

        "count": len(documents)

    }


@router.delete("/documents/{filename}")
async def delete_document(filename: str):

    file_path = UPLOAD_DIR / filename


    if file_path.exists():

        file_path.unlink()


    chroma_service.delete_document(filename)


    return {

        "message": "Document deleted successfully"

    }