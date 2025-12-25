from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity
from src.rag.loader import load_documents
from src.rag.chunker import chunk_text
from src.rag.embeddings import EmbeddingModel


class RagAgent:
    def run(self, query: str) -> str:
        project_root = Path.cwd()
        docs_path = project_root / "data" / "documents"

        if not docs_path.exists():
            return "⚠️ No se encontraron documentos para RAG"

        documents = load_documents(docs_path)
        if not documents:
            return "⚠️ Los documentos están vacíos"

        # Chunking
        chunks = []
        for doc in documents:
            chunks.extend(chunk_text(doc))

        if not chunks:
            return "⚠️ No se pudieron generar fragmentos"

        # Embeddings
        model = EmbeddingModel()
        model.fit(chunks)

        query_vector = model.embed_query(query)
        similarities = cosine_similarity(query_vector, model.matrix)

        best_index = similarities.argmax()
        best_chunk = chunks[best_index]

        return (
            "Respuesta basada en documentos locales:\n"
            f"{best_chunk}"
        )
