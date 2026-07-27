from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import embedding_service
from app.services.chroma_service import chroma_service
from app.services.rag_service import rag_service
from app.services.qwen_service import qwen_service
from app.services.reranker_service import reranker_service
from app.services.hybrid_search_service import hybrid_search_service
router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
async def ask(request: AskRequest):

    query_embedding = embedding_service.create_embeddings(
        [request.question]
    )[0]

    results = chroma_service.search_documents(query_embedding)

    all_chunks = chroma_service.get_all_chunks()

    keyword_results = hybrid_search_service.keyword_search(
        request.question,
        all_chunks["documents"]
    )
    

    semantic_results = results["documents"][0]

    combined_results = []

    for chunk in semantic_results + keyword_results:
        if chunk not in combined_results:
            combined_results.append(chunk)

    best_chunks = reranker_service.rerank(
        request.question,
        combined_results,
        top_k=3
    )

    context = "\n\n".join(best_chunks)

    prompt = rag_service.build_prompt(
        request.question,
        context
    )

    answer = qwen_service.generate_response(prompt)

    return {
    "question": request.question,
    "answer": answer,
    "sources": [
        {
            "source": metadata["source"],
            "page": metadata["page"]
        }
        for metadata in results["metadatas"][0]
    ]
}