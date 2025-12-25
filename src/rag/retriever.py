import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_top_k(query_vector, document_matrix, documents, k: int = 3):
    """
    Retorna los k documentos más similares a la consulta
    """
    similarities = cosine_similarity(query_vector, document_matrix)[0]

    top_indices = np.argsort(similarities)[::-1][:k]

    return [documents[i] for i in top_indices]
