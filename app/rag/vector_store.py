import faiss
import numpy as np


def create_faiss_index(embeddings):
    dimension = len(
        embeddings[0]
    )
    index = faiss.IndexFlatL2(
        dimension
    )
    vectors = np.array(
        embeddings,
        dtype="float32"
    )
    index.add(vectors)

    return index


def save_index(index):
    faiss.write_index(
        index,
        "vector_store/index.faiss"
    )


def load_index():
    return faiss.read_index(
        "vector_store/index.faiss"
    )