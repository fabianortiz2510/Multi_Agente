from src.rag.pipeline import build_chunks


def test_build_chunks():
    chunks = build_chunks()
    assert isinstance(chunks, list)
