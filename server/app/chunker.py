
from app.document_loader import load_documents

def process_documents_into_chunks(
    documents: list[dict[str, str]],
    chunk_size: int = 500,
    overlap: int = 100
) -> list[dict[str, str | int]]:

    all_chunks = []

    for document in documents:

        document_chunks = split_text_into_chunks(
            document["content"],
            chunk_size,
            overlap
        )

        for index, content in enumerate(document_chunks):

            all_chunks.append({
                "source": document["source"],
                "chunk_index": index,
                "content": content
            })

    return all_chunks


def split_text_into_chunks(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
) -> list[str]:

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    if overlap < 0:
        raise ValueError("Overlap cannot be negative.")

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks   

if __name__ == "__main__":

    documents = load_documents()

    chunks = process_documents_into_chunks(documents)

    print(f"Total documents loaded: {len(documents)}")
    print(f"Total chunks generated: {len(chunks)}")
    print("\nFirst 3 chunks:")

    for chunk in chunks[:3]:
        print(chunk)
        print("-" * 50)

    print("\nChunks per document:")

    for document in documents:

        document_chunk_count = sum(
            1 for chunk in chunks
            if chunk["source"] == document["source"]
        )

        print(
            f"{document['source']} "
            f"-> {document_chunk_count} chunks"
        )