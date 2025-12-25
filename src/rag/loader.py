from pathlib import Path


def load_documents(path: Path) -> list[str]:
    documents = []
    for file in path.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            documents.append(f.read())
    return documents
