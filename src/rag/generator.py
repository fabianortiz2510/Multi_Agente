def generate_answer(query: str, context_chunks: list[str]) -> str:
    """
    Genera una respuesta simple basada en el contexto recuperado
    """
    if not context_chunks:
        return "No se encontró información relevante."

    context = " ".join(context_chunks[:2])

    return f"Pregunta: {query}\n\nRespuesta: {context}"
