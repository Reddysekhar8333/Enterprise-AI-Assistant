from fastapi import APIRouter

from app.models.chat_schema import (
    ChatRequest
)

from app.rag.rag_pipeline import (
    ask_question
)

router = APIRouter()


@router.post("/")
def chat(request: ChatRequest):
    
    return ask_question(
        request.question
    )