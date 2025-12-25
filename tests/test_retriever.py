from src.rag.embeddings import EmbeddingModel
from src.rag.retriever import retrieve_top_k


def test_retriever():
    docs = [
        "El clima en Bogotá es frío",
        "Medellín tiene clima templado",
        "Cali es una ciudad cálida"
    ]

    model = EmbeddingModel()
    matrix = model.fit(docs)

    query_vec = model.embed_query("clima frío")

    results = retrieve_top_k(query_vec, matrix, docs, k=1)

    assert len(results) == 1
    assert "Bogotá" in results[0]
