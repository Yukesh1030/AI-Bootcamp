import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="documents"
)


def get_all_documents():

    results = collection.get(
        include=["documents", "metadatas"]
    )

    return {
        "documents": results["documents"],
        "metadatas": results["metadatas"],
        "ids": results["ids"]
    }