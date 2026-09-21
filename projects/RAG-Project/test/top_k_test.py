import chromadb
from src.embeddings import model


# -----------------------------
# ChromaDB
# -----------------------------

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="documents")


# -----------------------------
# Test questions
# -----------------------------

test_cases = [
    {
        "query": "What technologies does Yukesh know?",
        "keywords": [
            "React",
            "Java",
            "Python",
            "MySQL"
        ]
    },
    {
        "query": "What projects has Yukesh worked on?",
        "keywords": [
            "Real-Time Chat",
            "Ration Shop"
        ]
    },
    {
        "query": "What is Yukesh's educational background?",
        "keywords": [
            "Bachelor",
            "Computer Science",
            "Salem College",
            "8.01"
        ]
    }
]


# -----------------------------
# Retrieval
# -----------------------------

def retrieve(query, k):

    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=k
    )

    return results["documents"][0]


# -----------------------------
# Evaluation
# -----------------------------

def evaluate(query, keywords, k):

    documents = retrieve(query, k)

    combined_text = " ".join(documents).lower()

    matched_keywords = []

    for keyword in keywords:

        if keyword.lower() in combined_text:
            matched_keywords.append(keyword)

    precision = len(matched_keywords) / k

    recall = len(matched_keywords) / len(keywords)

    hit_rate = 1 if len(matched_keywords) > 0 else 0

    return precision, recall, hit_rate, matched_keywords


# -----------------------------
# Run evaluation
# -----------------------------

k_values = [1, 3, 5, 7]

for k in k_values:

    print("\n" + "=" * 60)
    print(f"TOP-K = {k}")
    print("=" * 60)

    total_precision = 0
    total_recall = 0
    total_hit_rate = 0

    for test in test_cases:

        precision, recall, hit_rate, matched = evaluate(
            test["query"],
            test["keywords"],
            k
        )

        total_precision += precision
        total_recall += recall
        total_hit_rate += hit_rate

        print(f"\nQuery: {test['query']}")

        print(f"Matched: {matched}")

        print(f"Precision: {precision:.2f}")

        print(f"Recall: {recall:.2f}")

        print(f"Hit Rate: {hit_rate:.2f}")

    count = len(test_cases)

    print("\n--- Average ---")

    print(f"Precision: {total_precision / count:.2f}")

    print(f"Recall: {total_recall / count:.2f}")

    print(f"Hit Rate: {total_hit_rate / count:.2f}")