from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".png",
    ".jpg",
    ".jpeg"
}


class DocumentService:

    def validate_file(self, file: UploadFile):
        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise ValueError("Unsupported file type")

    def generate_filename(self, filename: str):
        unique_id = uuid4().hex
        return f"{unique_id}_{filename}"

    async def save_file(self, file: UploadFile):
        self.validate_file(file)

        filename = self.generate_filename(file.filename)
        filepath = UPLOAD_DIR / filename

        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())

        return {
            "original_filename": file.filename,
            "stored_filename": filename,
            "path": str(filepath)
        }


document_service = DocumentService()