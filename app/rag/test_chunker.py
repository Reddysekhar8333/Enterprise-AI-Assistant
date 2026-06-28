from app.rag.pdf_loader import extract_text_from_pdf
from app.rag.chunker import create_chunks

text = extract_text_from_pdf(
    "documents/sample.pdf"
)

chunks = create_chunks(text)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print("\n")
    print(f"Chunk {i+1}")
    print(chunk[:300])