from app.rag.embeddings import generate_embedding

embedding = generate_embedding(
    "What is MongoDB?"
)

print(type(embedding))
print(len(embedding))