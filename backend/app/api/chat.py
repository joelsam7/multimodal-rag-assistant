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

    question = request.question.strip()

    lower_question = question.lower()


    casual_messages = {

        "hi": "Hello! How can I help you with your documents?",
        "hello": "Hello! How can I help you today?",
        "hey": "Hey! What would you like to know?",
        "thanks": "You're welcome!",
        "thank you": "You're welcome!",
        "bye": "Goodbye! Have a great day."

    }


    if lower_question in casual_messages:

        return {

            "question": question,
            "answer": casual_messages[lower_question],
            "sources": []

        }



    query_embedding = embedding_service.create_embeddings(
        [question]
    )[0]


    results = chroma_service.search_documents(
        query_embedding
    )


    if not results["documents"] or not results["documents"][0]:

        return {

            "question": question,
            "answer": "I could not find this information in the uploaded documents. Please upload a relevant document or try rephrasing your question.",
            "sources": []

        }


    context = "\n\n".join(
        results["documents"][0]
    )


    prompt = rag_service.build_prompt(
        question,
        context
    )


    answer = qwen_service.generate_response(
        prompt
    )


    return {

        "question": question,
        "answer": answer,
        "sources": results["metadatas"][0]

    }