from app.services.pdf_service import pdf_service

pdf_path = "sample.pdf"

text = pdf_service.extract_text(pdf_path)

print(text)