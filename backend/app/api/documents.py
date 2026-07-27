from fastapi import APIRouter

from app.services.chroma_service import chroma_service

router = APIRouter()


@router.get("/documents")
async def list_documents():

    documents = chroma_service.list_documents()

    return {
        "documents": documents,
        "count": len(documents)
    }