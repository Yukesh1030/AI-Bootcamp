from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = ["Python Developer",
              "Java developer",
              "fire"]

embeddings = model.encode(sentences)

similarity_matrix = cosine_similarity(embeddings)

print(similarity_matrix)