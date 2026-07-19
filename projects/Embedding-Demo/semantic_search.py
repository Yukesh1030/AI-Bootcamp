from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
"Python Developer",
"Java Developer",
"Machine Learning Engineer",
"React Developer",
"Football Player",
"Doctor",
"Software Engineer",
"AI Engineer"
] #load the documents to be searched

document_embeddings = model.encode(documents) #Generate embeddings

query = input("Enter your search : ") #Take user input

query_embedding = model.encode(query) #Generate the query embedding

similarities = cosine_similarity([query_embedding], document_embeddings)

print(similarities) #Print the scores

best_index = similarities.argmax() #Get the index of the best match

print(best_index) #Print the index of the best match