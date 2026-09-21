from src.hybrid_search import HybridRetriever


retriever = HybridRetriever()


queries = [
    "What technologies does Yukesh know?",
    "What projects has Yukesh worked on?",
    "What is Yukesh's educational background?",
    "Does Yukesh know ChromaDB?"
]


for query in queries:

    print("\n")
    print("=" * 70)
    print("QUERY:", query)
    print("=" * 70)


    results = retriever.search(
        query,
        top_k=5
    )


    for result in results:

        print("\nRank:", result["rank"])

        print(
            "RRF Score:",
            round(result["score"], 6)
        )

        print("Document:")

        print(
            result["document"][:500]
        )