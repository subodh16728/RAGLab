from pathlib import Path

# Locate the Naruto documents directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DOCUMENTS_DIR = (
    PROJECT_ROOT / "data" / "documents" / "naruto"
)


def load_documents() -> list[dict[str, str]]:

    if not DOCUMENTS_DIR.exists():
        raise FileNotFoundError(
            f"Documents directory not found: {DOCUMENTS_DIR}"
        )

    document_files = sorted(DOCUMENTS_DIR.glob("*.txt"))

    if not document_files:
        raise FileNotFoundError(
            "No TXT files found in the documents directory."
        )

    documents = []

    for file_path in document_files:

        content = file_path.read_text(
            encoding="utf-8"
        ).strip()

        if not content:
            continue

        documents.append({
            "source": file_path.name,
            "content": content
        })

    return documents


if __name__ == "__main__":

    loaded_documents = load_documents()

    print(f"Total documents loaded: {len(loaded_documents)}")

    for document in loaded_documents:
        print(
            f"{document['source']} "
            f"-> {len(document['content'])} characters"
        )
