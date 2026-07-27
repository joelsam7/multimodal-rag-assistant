from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import embedding_service
from app.services.chroma_service import chroma_service

from app.services.rag_service import rag_service
from app.services.qwen_service import qwen_service

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    query_embedding = embedding_service.create_embeddings(
        [request.question]
    )[0]

    results = chroma_service.search_documents(query_embedding)

    context = "\n\n".join(results["documents"][0]) 

    print(context)



    prompt = rag_service.build_prompt(
        request.question,
        context
    )

    answer = qwen_service.generate_response(prompt)

    return {
        "question": request.question,
        "answer": answer,
        "sources": results["metadatas"][0]
    }

