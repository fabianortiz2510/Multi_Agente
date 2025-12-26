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
        similarities = cosine_similarity(query_vector, model.matrix)[0]

        # 🔹 Tomar los TOP K chunks
        TOP_K = 3
        top_indices = similarities.argsort()[-TOP_K:][::-1]

        # 🔹 Umbral mínimo de similitud
        SIMILARITY_THRESHOLD = 0.30

        filtered_chunks = [
            chunks[i]
            for i in top_indices
            if similarities[i] >= SIMILARITY_THRESHOLD
        ]

        if not filtered_chunks:
            return (
                " No tengo información suficiente en los documentos "
                "para responder esa pregunta."
            )

        context = "\n\n".join(filtered_chunks)

        return (
            " Respuesta basada exclusivamente en documentos locales:\n\n"
            f"{context}"
        )
