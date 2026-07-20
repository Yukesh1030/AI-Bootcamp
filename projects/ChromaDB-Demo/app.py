import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection("knowledge_base")
except:
    pass

collection = client.get_or_create_collection(
    name="knowledge_base"
)

ids = [
    "1",
    "2",
    "3",
    "4",
    "5"
]

documents = [
    """Python is a high-level programming language used for web development, automation, artificial intelligence, data science and scripting.""",

    """Java is an object-oriented programming language widely used for enterprise applications and Android development.""",

    """Artificial Intelligence is the simulation of human intelligence in machines.""",

    """Machine Learning is a subset of Artificial Intelligence where systems learn patterns from data.""",

    """Docker is a containerization platform used to package applications together with their dependencies."""
]

metadatas = [
    {"topic": "Python"},
    {"topic": "Java"},
    {"topic": "Artificial Intelligence"},
    {"topic": "Machine Learning"},
    {"topic": "Docker"}
]

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("Documents in Collection:", collection.count())

results = collection.query(
    query_texts=["What is Python used for?"],
    n_results=2
)

print("\nTop Results:")
print(results["documents"])




# import chromadb

# #2.Create a Client : creates a connection to ChromaDB , The client is your gateway.
# client=chromadb.PersistentClient(
#     path="./chroma_db"  # path to the database folder (for permanent storage)
# )
# #3.Create a Collection : A collection is a group of related documents. You can think of it as a table in a database.
# collection = client.get_or_create_collection(
#     name = "employee"
# )   # like CREATE TABLE employees in SQL
# collection.add(
#     ids=["1","2","3"],
#     documents=[
#         "python developer",
#         "java developer",
#         "AI Engineer"
#     ],
#     metadatas=[
#         {"department": "IT"},
#         {"department": "Backend"},
#         {"department": "Artificial Intelligence"}
#     ]
# )
# print("Collection created successfully!")
# print(collection.count()) #Print the number of documents in the collection
# print(collection) # print(collection.peek())
# data = collection.get()
# print(data["ids"])
# results = collection.query(
#     query_texts=["engineer"],
#     where={"department": "Artificial Intelligence"},
#     n_results=2
# )

# print(results["documents"])