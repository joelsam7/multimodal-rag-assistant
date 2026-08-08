# Enterprise Multi-Modal RAG Assistant

An enterprise-oriented Retrieval-Augmented Generation (RAG) system designed to interact with uploaded documents and images using semantic retrieval, keyword search, hybrid retrieval, reranking, and multimodal language models.

The system allows users to upload documents, ask questions based on their content, and analyze images through a unified conversational interface.

## Overview

Traditional LLM applications can generate responses using information learned during model training, which can lead to outdated or unsupported answers.

This project addresses that problem by implementing a Retrieval-Augmented Generation pipeline that retrieves relevant information from user-provided documents before generating a response.

The system also extends traditional RAG with multimodal capabilities, allowing image-based queries through a Vision-Language Model.

## Key Features

* PDF and DOCX document processing
* Text extraction and document chunking
* Semantic search using vector embeddings
* Keyword-based retrieval using BM25
* Hybrid retrieval combining semantic and keyword search
* Cross-Encoder based reranking
* Context-grounded response generation
* Multimodal image understanding
* Persistent vector storage using ChromaDB
* REST APIs built with FastAPI
* Interactive web interface built with React
* Local LLM inference using Ollama

## Architecture

```text
                    User
                     |
                     v
              React Frontend
                     |
                     v
              FastAPI Backend
                /          \
               /            \
        Document Flow     Query Flow
             |                |
             v                v
      Document Processing   Query Processing
             |                |
             v                v
       Text Extraction    Hybrid Retrieval
             |                |
             v                |
        Text Chunking          |
             |                |
             v                v
       Embeddings       Semantic + BM25
             |                |
             v                v
          ChromaDB      Candidate Documents
                              |
                              v
                     Cross-Encoder Reranker
                              |
                              v
                      Relevant Context
                              |
                              v
                         Qwen2.5
                              |
                              v
                         Response


Image Query
     |
     v
React Frontend
     |
     v
FastAPI /image-chat
     |
     v
Qwen2.5-VL
     |
     v
Image Understanding
     |
     v
Response
```

## RAG Pipeline

### 1. Document Ingestion

Uploaded documents are processed through the document processing pipeline.

```text
Document
   |
   v
Text Extraction
   |
   v
Text Chunking
   |
   v
Embedding Generation
   |
   v
ChromaDB
```

The system currently supports PDF and DOCX document processing.

### 2. Embedding Generation

Text chunks are converted into vector representations using SentenceTransformers.

Model:

```text
all-MiniLM-L6-v2
```

These embeddings allow the system to retrieve documents based on semantic similarity rather than relying only on exact keyword matches.

### 3. Hybrid Retrieval

The retrieval pipeline combines two complementary approaches:

**Semantic Search**

Uses vector embeddings to identify content that is conceptually similar to the user's query.

**BM25**

Performs keyword-based retrieval and is particularly useful when exact terms, names, identifiers, or technical keywords are important.

The results from both retrieval methods are combined to improve recall.

### 4. Cross-Encoder Reranking

Retrieved candidates are passed through a Cross-Encoder reranker.

Instead of independently comparing the query and document embeddings, the Cross-Encoder evaluates the query-document pair directly to estimate relevance.

```text
User Query
    |
    v
Hybrid Retrieval
    |
    v
Candidate Documents
    |
    v
Cross-Encoder
    |
    v
Ranked Documents
    |
    v
Top Relevant Context
```

### 5. Grounded Generation

The highest-ranked context is provided to the Qwen2.5 language model.

The generation pipeline is designed to keep responses grounded in the retrieved document context rather than relying on unsupported external information.

## Multimodal Processing

The system also supports image-based interaction through Qwen2.5-VL.

The Vision-Language Model can process visual information and respond to queries involving images.

```text
Image
  |
  v
Qwen2.5-VL
  |
  v
Visual Understanding
  |
  v
Generated Response
```

This enables use cases such as:

* Image question answering
* Document image understanding
* OCR-related analysis
* Visual content interpretation
* Image-based queries

## Technology Stack

### Frontend

* React
* Vite
* Tailwind CSS
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### Retrieval

* ChromaDB
* SentenceTransformers
* BM25
* Cross-Encoder

### AI Models

* Qwen2.5
* Qwen2.5-VL
* Ollama

### Document Processing

* PyMuPDF
* python-docx

## Project Structure

```text
multimodal-rag-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── upload.py
│   │   │   ├── ask.py
│   │   │   ├── chat.py
│   │   │   ├── image_chat.py
│   │   │   └── documents.py
│   │   │
│   │   ├── services/
│   │   │   ├── pdf_service.py
│   │   │   ├── docx_service.py
│   │   │   ├── chunk_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── chroma_service.py
│   │   │   ├── hybrid_search_service.py
│   │   │   ├── reranker_service.py
│   │   │   ├── rag_service.py
│   │   │   ├── qwen_service.py
│   │   │   └── image_service.py
│   │   │
│   │   └── main.py
│   │
│   ├── uploads/
│   └── chroma_db/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Desktop.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   └── ChatMessage.jsx
│   │   │
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

## API Endpoints

| Method | Endpoint      | Description                            |
| ------ | ------------- | -------------------------------------- |
| POST   | `/upload`     | Upload and process documents           |
| POST   | `/ask`        | Ask questions about uploaded documents |
| POST   | `/chat`       | Conversational document interaction    |
| POST   | `/image-chat` | Process image-based queries            |
| GET    | `/documents`  | Retrieve uploaded document information |

FastAPI also provides interactive API documentation through Swagger UI.

## Installation

### Prerequisites

Make sure the following are installed:

* Python 3.10+
* Node.js
* npm
* Ollama
* Git

### Clone the Repository

```bash
git clone <repository-url>

cd multimodal-rag-assistant
```

## Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## Ollama Setup

Install the required models through Ollama:

```bash
ollama pull qwen2.5:3b
```

```bash
ollama pull qwen2.5-vl:3b
```

Make sure Ollama is running before starting the application.

## Frontend Setup

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at the local URL provided by Vite.

## How It Works

### Document Question Answering

```text
1. User uploads a document
2. Backend extracts the text
3. Text is divided into chunks
4. Chunks are converted into embeddings
5. Embeddings are stored in ChromaDB
6. User submits a question
7. Semantic and BM25 retrieval are performed
8. Retrieved candidates are reranked
9. Relevant context is selected
10. Context is passed to Qwen2.5
11. Grounded response is returned to the user
```

### Image Question Answering

```text
1. User uploads an image
2. Image is sent to the multimodal endpoint
3. Qwen2.5-VL processes the image
4. Visual information is interpreted
5. The model generates the response
6. Response is returned to the frontend
```

## Why Hybrid Retrieval?

Semantic search is effective at understanding the meaning of a query, while keyword retrieval performs well when exact terminology matters.

Combining both approaches helps the system handle queries where either semantic similarity or exact keyword matching is important.

The Cross-Encoder reranker then improves the ordering of the retrieved candidates by evaluating query-document relevance more precisely.

## Design Goals

The project focuses on:

* Grounded responses
* Improved retrieval accuracy
* Multimodal document interaction
* Modular backend architecture
* Local model inference
* Persistent document storage
* Separation between retrieval and generation

## Future Improvements

* Support for additional document formats
* Metadata-aware retrieval
* Conversation-aware retrieval
* Retrieval evaluation metrics
* Streaming responses
* Authentication and authorization
* Document-level access control
* Advanced multimodal RAG
* Production deployment
* Distributed vector storage

## Project Status

The core RAG pipeline, hybrid retrieval, reranking, document processing, multimodal interaction, REST APIs, and frontend interface are implemented.

The project is currently being refined toward a more production-oriented enterprise architecture.

## Author

**Joel Sam**

B.E. Computer Science and Engineering
Artificial Intelligence & Machine Learning
