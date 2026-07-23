from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retriever import retrieve
from app.services.llm import llm

router = APIRouter()


class Query(BaseModel):
    document_id: str
    question: str


@router.post("/query")
async def query(data: Query):

    docs = retrieve(
        data.question,
        f"vector_db/{data.document_id}"
    )

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{data.question}
"""

    answer = llm.invoke(prompt)

    return {
        "answer": answer.content,
        "context": context
    }