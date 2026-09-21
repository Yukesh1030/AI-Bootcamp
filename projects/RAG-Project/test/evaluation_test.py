from src.retriever import retrieve_documents


test_cases = [
    {
        "query": "What technologies does Yukesh know?",
        "expected_keywords": [
            "React",
            "Python",
            "Java"
        ]
    },
    {
        "query": "What projects has Yukesh worked on?",
        "expected_keywords": [
            "Real-Time Chat Application",
            "Ration Shop Management System"
        ]
    },
    {
        "query": "What is Yukesh's educational background?",
        "expected_keywords": [
            "Bachelor of Engineering",
            "Computer Science"
        ]
    },
    {
        "query": "Where does Yukesh currently work?",
        "expected_keywords": [
            "Stackly",
            "React Frontend Developer"
        ]
    }
]


for test in test_cases:

    query = test["query"]

    expected_keywords = test["expected_keywords"]

    results = retrieve_documents(
        query,
        n_results=3
    )

    combined_results = " ".join(results)

    found_keywords = []

    for keyword in expected_keywords:

        if keyword.lower() in combined_results.lower():

            found_keywords.append(keyword)

    score = len(found_keywords) / len(expected_keywords)

    print("\n" + "=" * 60)

    print("QUERY:")
    print(query)

    print("\nEXPECTED:")
    print(expected_keywords)

    print("\nFOUND:")
    print(found_keywords)

    print(f"\nRETRIEVAL SCORE: {score * 100:.2f}%")