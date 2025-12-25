def chunk_text(
    text: str,
    chunk_size: int = 300,
    overlap: int = 50
) -> list[str]:
    """
    Divide un texto en chunks solapados
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks
