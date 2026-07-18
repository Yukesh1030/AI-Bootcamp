Embedding Models
________________________________________
Lesson 1
Why Do We Need Embedding Models?
________________________________________
Before We Start...
I want to ask you a question.
Suppose you have this sentence
Python is a programming language.
Question:
Can the LLM understand this sentence?
Yes.
But...
Suppose I ask
Find another sentence similar to this.
Question:
How will the computer compare
Python is a programming language.
with
Java is a programming language.
Can it compare text directly?
No.
Computers only understand
0

1
Not English.
________________________________________
Question
How does the computer compare
Apple
with
Orange
Can it calculate
Apple

-

Orange
No.
________________________________________
So...
We convert
Text
↓
into
Numbers
This process is called
Embedding
________________________________________
Wait...
Didn't We Already Learn Embeddings?
Yes.
But only conceptually.
Today
we'll learn
how they are actually generated.
________________________________________
Think Like Google Maps
Suppose I ask
Where is Chennai?
Google Maps doesn't store
Chennai
It stores
Latitude

Longitude
Example
13.0827

80.2707
Now distance becomes easy.
Exactly the same idea.
________________________________________
Instead of storing
Python
We store
0.24

-0.81

0.62

...

384 Numbers
Now
computers can calculate
distance.
________________________________________
Visual
Sentence

↓

Embedding Model

↓

Vector

↓

Vector Database
________________________________________
What Is an Embedding Model?
Beginner Definition
An Embedding Model converts text into numerical vectors while preserving semantic meaning.
________________________________________
Interview Definition ⭐⭐⭐⭐⭐
An embedding model is a neural network trained to transform text into dense numerical vectors such that semantically similar texts are located close together in vector space.
________________________________________
Example
Sentence
Python Developer
↓
Embedding Model
↓
[0.24,0.71,-0.53,...]
Sentence
Java Developer
↓
Embedding Model
↓
[0.20,0.69,-0.50,...]
Notice something.
The vectors become
close.
________________________________________
Sentence
Football Match
↓
[-0.92,0.43,-0.15,...]
Far away.
________________________________________
Important Question
Why Not Use the LLM?
This is one of the most common interview questions.
Suppose
you already have
Llama

GPT

Gemini
Why not use them to generate vectors?
________________________________________
Answer
Because
LLMs are optimized for
Next Token Prediction
Not
Similarity Search
Embedding Models are trained specifically for
Semantic Similarity
Different objective.
Different training.
________________________________________
Real Example
Imagine
100 Million Documents.
Question
Find
Python Developer
Similar resumes.
Using LLM
Very Slow

Very Expensive
Using Embedding Model
Milliseconds
________________________________________
So the Pipeline Becomes
Resume

↓

Embedding Model

↓

Vector

↓

Vector DB

↓

Cosine Similarity

↓

Top Results
This is
RAG.
________________________________________
Popular Embedding Models
You'll hear these names a lot.
________________________________________
1
Sentence Transformers
all-MiniLM-L6-v2
The one you saw in your friend's project.
________________________________________
2
OpenAI
text-embedding-3-small

text-embedding-3-large
________________________________________
3
BGE
BAAI/bge-small

bge-base

bge-large
Very popular for RAG.
________________________________________
4
E5
intfloat/e5-small

e5-base

e5-large
Excellent retrieval performance.
________________________________________
5
Nomic
nomic-embed-text
Open source.
________________________________________
Question
How many numbers are inside a vector?
Depends on the model.
Example
MiniLM

↓

384 Dimensions
OpenAI
↓
1536 Dimensions
BGE Large
↓
1024 Dimensions
Dimension
means
Number of values inside the vector.
________________________________________
Real Project
Suppose
you upload
1000 PDFs
Pipeline
PDF

↓

Chunking

↓

Embedding Model

↓

Vectors

↓

ChromaDB
Question
When user asks
Explain Transformers
Pipeline
Question

↓

Embedding Model

↓

Question Vector

↓

Cosine Similarity

↓

Top Chunks

↓

LLM

↓

Answer
Notice
The LLM wasn't searching.
The
Embedding Model
did.
________________________________________
Interview Question ⭐⭐⭐⭐⭐
Why do we use Embedding Models instead of LLMs for retrieval?
Professional Answer:
Embedding models are specifically trained to generate semantic vector representations for efficient similarity search, whereas LLMs are optimized for next-token prediction. Using embedding models enables fast and scalable retrieval in vector databases, making them ideal for RAG systems.
________________________________________
Assignment (No Coding Yet)
I want you to answer these three questions in your own words:
Q1
Why can't a computer compare two English sentences directly?
________________________________________
Q2
Why do we convert text into vectors?
________________________________________
Q3
Why don't we use the LLM itself for similarity search?
________________________________________
🚀 Next Lesson (The First Hands-On Embedding Model)
Now we'll finally work with the model you've seen before:
sentence-transformers/all-MiniLM-L6-v2
You'll learn:
•	How to install sentence-transformers 
•	Why it depends on PyTorch 
•	What happens when you call model.encode() 
•	How a sentence becomes a 384-dimensional vector 
•	How to inspect the vector in Python 
•	Why every value is a floating-point number 
•	How this vector will later be stored in ChromaDB 
This is the lesson where you'll generate your first real embeddings instead of just talking about them. After that, RAG will start feeling much less mysterious.



