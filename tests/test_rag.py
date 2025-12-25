from src.rag.loader import load_documents


def test_load_documents():
    docs = load_documents()
    assert isinstance(docs, list)
