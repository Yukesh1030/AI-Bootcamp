from src.retriever import retrieve_documents


test_queries = [
    "What technologies does Yukesh know?",
    "What projects has Yukesh worked on?",
    "What is Yukesh's educational background?",
    "Where does Yukesh currently work?",
    "What is Yukesh's favorite food?",
]


for query in test_queries:

    print("\n" + "=" * 60)
    print("QUERY:")
    print(query)
    print("=" * 60)

    results = retrieve_documents(
        query,
        n_results=3
    )

    print("\nRETRIEVED DOCUMENTS")
    print("-" * 60)

    for i, document in enumerate(results):

        print(f"\nResult {i + 1}")
        print("-" * 40)

        print(document)