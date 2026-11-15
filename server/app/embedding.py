from sentence_transformers import SentenceTransformer
from app.document_loader import load_documents
from app.chunker import process_documents_into_chunks

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def generate_embeddings(chunks):
    texts = [chunk["content"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    embedded_chunks = []

    for chunk, embedding in zip(chunks, embeddings):
        embedded_chunks.append({
            **chunk,
            "embedding": embedding.tolist()
        })

    return embedded_chunks

if __name__ == "__main__":
    documents = load_documents()

    chunks = process_documents_into_chunks(documents)

    embedded_chunks = generate_embeddings(chunks)

    print(f"\nTotal documents: {len(documents)}")
    print(f"Total chunks: {len(chunks)}")
    print(f"Total embedded chunks: {len(embedded_chunks)}")

    print("\nFirst embedded chunk:")
    print(embedded_chunks[0]["source"])
    print(embedded_chunks[0]["chunk_index"])
    print(embedded_chunks[0]["content"])

    print("\nEmbedding dimensions:")
    print(len(embedded_chunks[0]["embedding"]))