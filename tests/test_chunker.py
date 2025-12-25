from src.rag.chunker import chunk_text


def test_chunk_text():
    text = "A" * 1000
    chunks = chunk_text(text)

    assert len(chunks) > 1
    assert all(isinstance(c, str) for c in chunks)
