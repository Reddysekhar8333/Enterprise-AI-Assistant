
from app.database.db import SessionLocal

from app.models.chunk import Chunk
from app.models.vector_mapping import VectorMapping

from app.rag.embeddings import generate_embedding
from app.rag.vector_store import (
    create_faiss_index,
    save_index
)


def build_index():

    db = SessionLocal()

    chunks = db.query(
        Chunk
    ).all()

    embeddings = []

    position = 0

    for chunk in chunks:

        print(
            f"Embedding chunk {chunk.id}"
        )

        embedding = generate_embedding(
            chunk.chunk_text
        )

        embeddings.append(
            embedding
        )

        mapping = VectorMapping(
            chunk_id=chunk.id,
            vector_position=position
        )

        db.add(mapping)

        position += 1

    db.commit()

    index = create_faiss_index(
        embeddings
    )

    save_index(index)

    print(
        f"Indexed {len(chunks)} chunks"
    )


if __name__ == "__main__":
    build_index()