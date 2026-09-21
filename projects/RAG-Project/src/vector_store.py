import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(chunks, embeddings):

    metadatas = []

    for i, chunk in enumerate(chunks):

        metadata = {
            "source": "Yukesh_G_ATS_Resume.pdf",
            "chunk_id": i,
            "section": "general"
        }

        metadatas.append(metadata)

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids,
        metadatas=metadatas
    )

    print(
        f"Stored {len(chunks)} documents in ChromaDB"
    )