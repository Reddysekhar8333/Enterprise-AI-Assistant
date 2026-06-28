
from fastapi import FastAPI

from app.api.document_routes import router as document_router
from app.api.chat_routes import router as chat_router

app = FastAPI(
    title="Enterprise AI Assistant"
)

app.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"]
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)

@app.get("/")
def root():
    return {
        "message": "Enterprise AI Assistant Running"
    }
