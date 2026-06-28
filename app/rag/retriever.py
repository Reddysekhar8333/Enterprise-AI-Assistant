import numpy as np

from app.database.db import SessionLocal

from app.models.chunk import Chunk
from app.models.vector_mapping import VectorMapping

from app.rag.embeddings import generate_embedding
from app.rag.vector_store import load_index


def retrieve_chunks(
    query: str,
    k: int = 3
    ):
    query_embedding = generate_embedding(
        query
    )
    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )
    index = load_index()

    distances, positions = index.search(
        query_vector,
        k
    )
    db = SessionLocal()
    results = []
    for pos in positions[0]:
        mapping = (
            db.query(VectorMapping)
            .filter(
                VectorMapping.vector_position == int(pos)
            )
            .first()
        )
        if mapping:
            chunk = (
                db.query(Chunk)
                .filter(
                    Chunk.id == mapping.chunk_id
                )
                .first()
            )
            if chunk:
                results.append(
                    chunk.chunk_text
                )
    return results