from src.semantic_search import semantic_search


query = "What AI technologies does Yukesh know?"


results = semantic_search(
    query,
    top_k=5
)


for result in results:

    print("\nRank:", result["rank"])

    print("Distance:", result["distance"])

    print("Document:")
    print(result["document"])