import fitz


class PDFService:

    @staticmethod
    def extract_text(pdf_path: str) -> str:

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    @staticmethod
    def extract_pages(pdf_path: str):

        document = fitz.open(pdf_path)

        pages = []

        for page_num, page in enumerate(document):

            pages.append({
                "page": page_num + 1,
                "text": page.get_text()
            })

        document.close()

        return pages


pdf_service = PDFService()