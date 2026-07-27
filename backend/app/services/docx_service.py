from docx import Document


class DocxService:

    @staticmethod
    def extract_text(docx_path: str):

        document = Document(docx_path)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return text


docx_service = DocxService()