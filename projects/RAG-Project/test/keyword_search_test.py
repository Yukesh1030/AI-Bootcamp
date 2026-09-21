from src.keyword_search import BM25Retriever


documents = [
    "Yukesh knows Java, JavaScript, Python and ReactJS.",
    "Yukesh has experience with MySQL and PostgreSQL databases.",
    "Yukesh has built a Real-Time Chat Application using Java Sockets.",
    "Yukesh has worked with RAG, LangChain, LangGraph and ChromaDB.",
    "Yukesh completed a Bachelor of Engineering in Computer Science."
]


retriever = BM25Retriever(documents)


query = "What AI technologies does Yukesh know?"

results = retriever.search(query, top_k=3)


for result in results:

    print("\nScore:", result["score"])

    print("Document:")
    print(result["document"])