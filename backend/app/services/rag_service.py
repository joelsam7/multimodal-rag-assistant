class RAGService:

    def build_prompt(self, question, context):

        return f"""
You are an Enterprise Multi-Modal RAG Assistant.

Answer the question using ONLY the context below.

Rules:
- Do NOT use outside knowledge.
- Do NOT guess.
- Do NOT omit relevant facts that appear in the context.
- If the answer contains a list, include ALL items found in the context.
- Copy names, numbers, and values exactly as they appear.
- If the answer is not in the context, reply exactly:
"I could not find that information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""


rag_service = RAGService()