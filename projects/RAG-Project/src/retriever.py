import chromadb

from src.embeddings import model


client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="documents")


def retrieve_documents(
    query,
    n_results=5,
    distance_threshold=1.7,
    section=None
):

    query_embedding = model.encode([query])

    query_params = {
        "query_embeddings": query_embedding.tolist(),
        "n_results": n_results
    }

    if section is not None:

        query_params["where"] = {
            "section": section
        }

    results = collection.query(**query_params)

    documents = results["documents"][0]
    distances = results["distances"][0]

    filtered_documents = []

    for document, distance in zip(
        documents,
        distances
    ):

        print(f"Distance: {distance:.4f}")

        if distance <= distance_threshold:

            filtered_documents.append(document)

    return filtered_documents