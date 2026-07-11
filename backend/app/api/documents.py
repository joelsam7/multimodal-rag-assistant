from fastapi import APIRouter, File, HTTPException, UploadFile
from backend.app.services.document_service import document_service

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        return await document_service.save_file(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))