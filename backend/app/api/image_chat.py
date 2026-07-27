from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.services.qwen_service import qwen_service

router = APIRouter()

IMAGE_DIR = Path("image_uploads")
IMAGE_DIR.mkdir(exist_ok=True)


@router.post("/image-chat")
async def image_chat(
    file: UploadFile = File(...),
    question: str = "Describe this image."
):

    image_path = IMAGE_DIR / file.filename

    with open(image_path, "wb") as buffer:
        buffer.write(await file.read())

    answer = qwen_service.analyze_image(
        str(image_path),
        question
    )

    return {
        "filename": file.filename,
        "question": question,
        "answer": answer
    }