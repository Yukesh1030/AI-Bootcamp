from sentence_transformers import SentenceTransformer

#2.load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

text = "Python is the programming language"

embedding = model.encode(text)
print(len(embedding))