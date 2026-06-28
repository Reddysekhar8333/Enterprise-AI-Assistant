import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.document import Document

from app.rag.ingestion import ingest_document

router = APIRouter()

UPLOAD_DIR = "documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
    ): 
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    document = Document(
        filename=file.filename,
        file_path=file_path
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "document_id": document.id,
        "filename": document.filename,
        "file_path": document.file_path,
        "uploaded_at": document.uploaded_at
    }

@router.get("/")
def get_documents(
    db: Session = Depends(get_db)
    ):
    documents = db.query(Document).all()
    return documents


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db)
    ):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )
    if not document:
        return {
            "message": "Document not found"
        }
    return document


@router.post("/{document_id}/ingest")
def ingest_pdf(
    document_id: int,
    db: Session = Depends(get_db)
    ):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )
    if not document:
        return {
            "message": "Document not found"
        }
    total_chunks = ingest_document(
        document.id,
        document.file_path,
        db
    )
    return {
        "document_id": document.id,
        "chunks_created": total_chunks
    }