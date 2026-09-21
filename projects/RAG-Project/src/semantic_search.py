import chromadb

from src.embeddings import model


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="documents"
)


def semantic_search(query, top_k=5):

    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    output = []

    for rank, (document, distance) in enumerate(
        zip(documents, distances),
        start=1
    ):

        output.append({
            "document": document,
            "distance": float(distance),
            "rank": rank
        })

    return output