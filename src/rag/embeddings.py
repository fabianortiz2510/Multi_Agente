from sklearn.feature_extraction.text import TfidfVectorizer


class EmbeddingModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.matrix = None

    def fit(self, documents: list[str]):
        self.matrix = self.vectorizer.fit_transform(documents)
        return self.matrix

    def embed_query(self, query: str):
        return self.vectorizer.transform([query])
