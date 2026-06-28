from sqlalchemy.orm import Session

from app.models.chunk import Chunk

from app.rag.pdf_loader import extract_text_from_pdf
from app.rag.chunker import create_chunks


def ingest_document(
    document_id: int,
    file_path: str,
    db: Session
    ):
    text = extract_text_from_pdf(file_path)
    chunks = create_chunks(text)
    for chunk_text in chunks:
        chunk = Chunk(
            document_id=document_id,
            chunk_text=chunk_text
        )
        db.add(chunk)
    db.commit()
    return len(chunks)