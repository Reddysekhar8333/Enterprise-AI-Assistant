from app.rag.retriever import retrieve_chunks
from app.rag.llm import generate_answer


def ask_question( question: str ):
    chunks = retrieve_chunks(
        question,
        k=3
    )
    context = "\n\n".join(chunks)
    answer = generate_answer(
        question,
        context
    )
    return {
        "answer": answer,
        "sources": chunks
    }
