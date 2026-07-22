from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm import llm

router = APIRouter()

class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    response = llm.invoke(request.question)

    return {
        "answer": response.content
    }