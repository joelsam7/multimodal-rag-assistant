# Ent"""erprise Multi-Modal RAG Assistant

An AI-powered multimodal Retrieval-Augmented Generation (RAG) assistant that allows users to upload documents and images, retrieve relevant information, and generate accurate responses using Large Language Models and Vision Language Models.

## Features

### Document Processing
- Supports multiple file formats:
  - PDF
  - DOCX
  - TXT
  - PNG
  - JPG
  - JPEG

- Extracts text from documents
- Performs OCR on images using Tesseract
- Splits documents into meaningful chunks
- Generates vector embeddings

### Retrieval Pipeline
- Semantic search using ChromaDB
- Keyword search using BM25
- Hybrid search combining semantic and keyword retrieval
- Cross-encoder reranking for improved relevance

### AI Capabilities
- Question answering using Qwen2.5 LLM
- Image understanding using Qwen2.5-VL
- Context-based responses using RAG pipeline

## System Architecture

```
User
 |
 | Upload Document / Ask Question
 |
FastAPI Backend
 |
 ├── Document Processing
 |      |
 |      ├── PDF Extraction
 |      ├── DOCX Extraction
 |      ├── TXT Extraction
 |      └── Image OCR
 |
 ├── Text Chunking
 |
 ├── Embedding Generation
 |
 ├── ChromaDB Vector Database
 |
 ├── Hybrid Retrieval
 |      |
 |      ├── Semantic Search
 |      └── BM25 Keyword Search
 |
 ├── Cross Encoder Reranking
 |
 └── Qwen LLM / Qwen-VL Response Generation
```

## Tech Stack

### Backend
- Python
- FastAPI

### AI / ML
- Sentence Transformers
- Qwen2.5
- Qwen2.5-VL
- Cross Encoder Reranker

### Database
- ChromaDB

### Document Processing
- PyMuPDF
- python-docx
- Pytesseract
- Pillow

## Project Structure

```
multimodal-rag-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── chroma_db/
│   ├── uploads/
│   ├── requirements.txt
│   └── venv/
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Backend

```bash
cd backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The server will run at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Upload Documents

```
POST /upload
```

Uploads and indexes documents into ChromaDB.

Supported formats:
- PDF
- DOCX
- TXT
- Images

---

### Ask Questions

```
POST /ask
```

Uses:
- Semantic retrieval
- BM25 keyword retrieval
- Reranking
- RAG generation

---

### Chat

```
POST /chat
```

Provides conversational document-based responses.

---

### Image Chat

```
POST /image-chat
```

Allows users to ask questions about images using Qwen2.5-VL.

---

### List Documents

```
GET /documents
```

Returns uploaded and indexed documents.

## Workflow

1. User uploads a document or image.
2. Text is extracted from the file.
3. Documents are divided into chunks.
4. Embeddings are generated using Sentence Transformers.
5. Embeddings are stored in ChromaDB.
6. User submits a question.
7. Relevant chunks are retrieved using hybrid search.
8. Cross encoder reranks the results.
9. Qwen generates an answer using retrieved context.

## Future Improvements

- User authentication
- Conversation memory
- Cloud deployment
- More document format support
- Advanced multimodal embeddings
- Web-based frontend interface

## License

This project is developed for educational and portfolio purposes."""