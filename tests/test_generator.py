from src.rag.generator import generate_answer


def test_generate_answer():
    query = "¿Cómo es el clima en Bogotá?"
    context = ["El clima en Bogotá es frío."]

    answer = generate_answer(query, context)

    assert "Bogotá" in answer
