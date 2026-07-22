#Step 2 — Import Libraries
import chromadb
from sentence_transformers import SentenceTransformer

#Step 3 — Load the Embedding Model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

#Step 4 — Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")


#Step 5 — Create a Fresh Collection
try:
    client.delete_collection("manual_embeddings")
except:
    pass
collection = client.get_or_create_collection(name="manual_embeddings")

#create an documents
documents=[
    "Python is used for AI.",
    "Java is used for enterprise applications.",
    "Docker packages applications into containers."
]

#Step 7 — Generate Embeddings Yourself
embeddings = model.encode(documents)

print(type(embeddings))
print(len(embeddings))
print(len(embeddings[0]))