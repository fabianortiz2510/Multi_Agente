from src.rag.loader import load_documents
from src.rag.chunker import chunk_text


def build_chunks(data_path: str = "data") -> list[str]:
    """
    Carga documentos y los divide en chunks
    """
    documents = load_documents(data_path)
    all_chunks = []

    for doc in documents:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    return all_chunks
