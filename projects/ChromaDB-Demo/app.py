import chromadb

#2.Create a Client : creates a connection to ChromaDB , The client is your gateway.
client=chromadb.PersistentClient(
    path="./chroma_db"  # path to the database folder (for permanent storage)
)

#3.Create a Collection : A collection is a group of related documents. You can think of it as a table in a database.
collection = client.get_or_create_collection(
    name = "employee"
)   # like CREATE TABLE employees in SQL

collection.add(
    ids=["1","2","3"],
    documents=[
        "python developer",
        "java developer",
        "AI Engineer"
    ],
    metadatas=[
        {"department": "IT"},
        {"department": "Backend"},
        {"department": "Artificial Intelligence"}
    ]
)
print("Collection created successfully!")
print(collection.count()) #Print the number of documents in the collection
print(collection)
# print(collection.peek())
data = collection.get()

print(data["ids"])

results = collection.query(
    query_texts=["engineer"],
    where={"department": "Artificial Intelligence"},
    n_results=2
)

print(results["documents"])