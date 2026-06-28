from app.rag.retriever import retrieve_chunks

results = retrieve_chunks(
    "What is MongoDB?"
)

for i, chunk in enumerate(results):
    print("\n")
    print("=" * 50)

    print(
        f"Chunk {i+1}"
    )
    print(chunk[:500])