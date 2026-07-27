import pytesseract
from PIL import Image


class ImageService:

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

    def extract_text(self, image_path: str):

        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        return text


image_service = ImageService()