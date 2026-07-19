from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2") #variable = Object("identifier")

sentences = "Python is the programming language"

embedding= model.encode(sentences)

print("Sentence:")
print(sentences)

print("\nLength:")
print(len(embedding))

print("\nType:")
print(type(embedding))

print("\nFirst 10 Values:")
print(embedding[:10])