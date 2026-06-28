from app.rag.llm import generate_answer

response = generate_answer(
    "What is MongoDB?",
    """
    MongoDB is a NoSQL database.
    MongoDB stores BSON documents.
    MongoDB is scalable.
    """
)

print(response)