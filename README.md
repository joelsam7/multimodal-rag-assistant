# Multi-Modal RAG Assistant

An AI-powered multimodal Retrieval-Augmented Generation (RAG) assistant that allows users to upload documents and images, retrieve relevant information, and generate context-aware responses using Large Language Models (LLMs) and Vision Language Models (VLMs).

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
- Stores document embeddings persistently using ChromaDB

### Retrieval Pipeline
- Semantic search using Sentence Transformers + ChromaDB
- Keyword search using BM25
- Hybrid retrieval combining semantic and keyword search
- CrossEncoder reranking for improved relevance

### AI Capabilities
- Document question answering using Qwen2.5 LLM
- Image understanding using Qwen2.5-VL
- Context-grounded responses using RAG pipeline
- Source attribution for generated answers

### Document Management
- Upload documents
- View indexed documents
- Delete documents from the knowledge base
- Handles empty knowledge bases gracefully

## System Architecture

```
User
 |
 | Upload Document / Ask Question
 |
React Frontend
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
 ├── CrossEncoder Reranking
 |
 └── Qwen2.5 / Qwen2.5-VL Response Generation
```

## Tech Stack

### Frontend
- React
- Tailwind CSS

### Backend
- Python
- FastAPI

### AI / ML
- Sentence Transformers
- BM25
- CrossEncoder Reranker
- Qwen2.5
- Qwen2.5-VL

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

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── chroma_db/
│   ├── uploads/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Backend Setup

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start backend server:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

Start frontend:

```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

### Upload Document

```
POST /upload
```

Uploads and indexes documents into ChromaDB.

Supported:
- PDF
- DOCX
- TXT
- Images

---

### Ask Questions

```
POST /ask
```

Pipeline:
- Semantic retrieval
- BM25 keyword retrieval
- CrossEncoder reranking
- RAG response generation

---

### Image Chat

```
POST /image-chat
```

Uses Qwen2.5-VL for image-based question answering.

---

### List Documents

```
GET /documents
```

Returns indexed documents.

---

### Delete Document

```
DELETE /documents/{filename}
```

Removes a document from the knowledge base.

## Workflow

1. User uploads a document or image.
2. Content is extracted from the file.
3. Documents are split into chunks.
4. Sentence Transformer generates embeddings.
5. Embeddings are stored in ChromaDB.
6. User submits a question.
7. Relevant information is retrieved using hybrid search.
8. CrossEncoder reranks retrieved chunks.
9. Qwen generates an answer using retrieved context.

## Future Improvements

- User authentication and authorization
- Persistent conversation history
- Cloud deployment
- Advanced multimodal embeddings
- Enterprise access control

## License

This project is developed for educational and portfolio purposes.