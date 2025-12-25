from src.rag.embeddings import EmbeddingModel


def test_tfidf_embeddings():
    docs = ["clima en Bogotá", "temperatura en Medellín"]

    model = EmbeddingModel()
    matrix = model.fit(docs)
    query_vec = model.embed_query("clima")

    assert matrix.shape[0] == 2
    assert query_vec.shape[0] == 1
