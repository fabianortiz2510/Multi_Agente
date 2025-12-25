from src.graph import assistant_graph

def main():
    print("Multi-agent assistant (LangGraph) 🚀")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "salir"]:
            break

        result = assistant_graph.invoke({"input": user_input})
        print("\nAssistant:")
        print(result["output"])


if __name__ == "__main__":
    main()
