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



Lesson 2 – Generate Your First Embedding
🎯 Today's Goal

By the end of this lesson, you'll understand this complete pipeline:

Sentence
    │
    ▼
Embedding Model
    │
    ▼
384-Dimensional Vector
    │
    ▼
Python List / NumPy Array
    │
    ▼
Cosine Similarity
Step 0 – Create a New Project

Inside your AI-Bootcamp folder, create:

AI-Bootcamp/
│
├── embeddings/
│      ├── app.py
│      ├── requirements.txt
│      └── venv
│
├── chatbot/
│
└── ...

Why a separate folder?

Because every AI topic should be its own mini-project.

This keeps your code clean and professional.

Step 1 – Create a Virtual Environment

Open the terminal:

cd embeddings

Then:

python -m venv venv

Activate it:

Windows
venv\Scripts\activate
Step 2 – Install the Required Packages

Run:

pip install sentence-transformers
🤔 Question

Why didn't we install OpenAI?

Because today we're not calling an API.

Everything runs locally.

What Happens Internally?

When you run

pip install sentence-transformers

Python downloads the sentence-transformers library.

But that library depends on another library.

PyTorch

The installation also pulls in:

PyTorch

Question:

Why?

Because the embedding model is a deep neural network.

Neural networks need a framework to perform tensor operations.

The most popular frameworks are:

PyTorch
TensorFlow

sentence-transformers uses PyTorch.

Architecture
Your Code

↓

sentence-transformers

↓

PyTorch

↓

Neural Network

↓

Embedding Vector
Step 3 – Create app.py

Don't write everything.

We'll build it slowly.

First Import
from sentence_transformers import SentenceTransformer
Question

What is SentenceTransformer?

Think of it as a Python class.

Remember OOP?

When we create an object:

model = SentenceTransformer(...)

We're creating an object capable of generating embeddings.

Visual
SentenceTransformer

↓

Object

↓

encode()

↓

Vector
Step 4 – Load the Model

Write:

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

Let's stop here.

Don't write anything else yet.

What Happens Internally?

This single line does a lot of work.

First Run

Since your computer doesn't have the model yet:

Python

↓

Hugging Face

↓

Download Model

↓

Store Locally

The model is downloaded and cached.

Second Run

Next time:

Python

↓

Local Cache

↓

Load Model

No download.

Much faster.

🤔 Why "sentence-transformers/all-MiniLM-L6-v2"?

Let's break the name down.

sentence-transformers

Organization.

all

General-purpose embedding model.

MiniLM

A lightweight Transformer architecture.

L6

6 Transformer layers.

Remember Transformers?

GPT has many layers.

MiniLM is much smaller and faster.

v2

Second version.

Why Is It Popular?

Because it's:

✅ Small
✅ Fast
✅ Free
✅ Good quality
✅ Widely used for RAG

That's why you saw it in your friend's project.

Interview Question ⭐⭐⭐⭐⭐

Why is all-MiniLM-L6-v2 widely used?

Professional Answer:

It provides a good balance between embedding quality, speed, and model size. It generates 384-dimensional embeddings, making it efficient for semantic search and RAG applications while requiring relatively low computational resources.

Step 5 – Run It

Your app.py should contain only:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Model Loaded Successfully!")
What You Should See

The first run may take a little time because the model downloads.

Typical output:

Downloading model...
Loading...
Model Loaded Successfully!

On future runs:

Model Loaded Successfully!

Almost instantly.

🧠 What's Really Happening?

Think of the model like a dictionary.

Not a normal dictionary.

A mathematical dictionary.

Instead of:

Python

↓

Programming Language

It learns:

Python

↓

384 Numbers

Those numbers capture semantic meaning.

🎯 Your Task

Complete these steps:

Create the embeddings folder.
Create and activate a virtual environment.
Install sentence-transformers.
Create app.py.
Paste the two lines and the print.
Run:
python app.py
📩 Send Me
A screenshot of your terminal (especially the first run).
Any errors, if they occur.
🚀 Next Part of This Lesson

Once you've successfully loaded the model, we'll continue with Lesson 2 – Part 2:

You'll write your first call to:

embedding = model.encode("Python is a programming language.")

Then we'll inspect:

Why the result has 384 values
Why they're floating-point numbers
What each dimension represents (and what it doesn't)
How to compare two sentence embeddings using cosine similarity

This is where embeddings become real instead of theoretical.


Module 5 — Embedding Models
Lesson 2 — Generate Your First Embedding
🎯 Today's Objective

Today we are NOT building a chatbot.

We are learning one small AI component called an Embedding Model.

So we should not write this inside

projects/
    AI-Chatbot/

because it has nothing to do with the chatbot.

Professional developers always separate experiments from projects.

Step 1
Create a New Project

Inside

projects/

Create a new folder.

projects/
│
├── AI-Chatbot/
│
└── Embedding-Demo/

Inside

Embedding-Demo

create

Embedding-Demo
│
├── embedding.py
│
├── README.md
│
└── requirements.txt

So your folder becomes

AI-BOOTCAMP

│

├── projects

│      │

│      ├── AI-Chatbot

│      │      app.py

│      │

│      └── Embedding-Demo

│             embedding.py
│             README.md
│             requirements.txt

Why?

Because every concept becomes its own mini-project.

Later you'll have

projects/

AI-Chatbot

Embedding-Demo

ChromaDB-Demo

RAG-Demo

LangChain-Demo

CrewAI-Demo

Resume-Analyzer

Medical-AI

...

This is exactly how professionals organize learning repositories.

Step 2

Open Terminal

Go to

AI-BOOTCAMP

NOT

Embedding-Demo

because your virtual environment is already here.

Your terminal should show

(venv)

E:\learn\GenAI\AI-BOOTCAMP>
Step 3

Install the library

pip install sentence-transformers
Question

Why here?

Because

your

venv

belongs to

AI-BOOTCAMP

Every project inside

projects/

shares the same virtual environment.

This is completely fine while learning.

Step 4

Freeze the dependencies

Again

pip freeze > requirements.txt

Notice

this updates only

AI-BOOTCAMP/

requirements.txt

NOT

Embedding-Demo/

For now that's okay.

Later I'll teach you project-specific virtual environments.

Step 5

Open

Embedding-Demo

↓

embedding.py

This file will contain today's code.

Step 6

Write only ONE line

from sentence_transformers import SentenceTransformer

Don't write anything else.

Stop.

Let's understand this line.

Question 1

What is

sentence_transformers

Is it a model?

No.

It is a Python package.

Think

sentence_transformers

↓

Library

Exactly like

numpy

pandas

requests
Question 2

What is

SentenceTransformer

Notice

Capital S

Capital T

That means

it's a

Class

Remember OOP?

Student()

Employee()

SentenceTransformer()

Exactly the same concept.

Internal Structure

Imagine

sentence_transformers

│

├── SentenceTransformer

├── losses

├── datasets

├── models

├── evaluation

├── util

We are importing only

SentenceTransformer
Why is it a Class?

Because

every model

is an object.

Example

MiniLM

↓

Object
MPNet

↓

Object
BGE

↓

Object

The class creates these objects.

Visual
SentenceTransformer

(Class)

        │

        ▼

model

(Object)

        │

        ▼

encode()

save()

tokenize()

...
Interview Question ⭐⭐⭐⭐⭐
What is SentenceTransformer?

Professional Answer:

SentenceTransformer is the primary class provided by the sentence-transformers library. It loads pre-trained transformer-based embedding models and provides methods such as encode() to convert text into dense vector representations.

🎯 Today's Mini Assignment

Complete only these tasks:

✅ Create the Embedding-Demo folder under projects/.
✅ Create embedding.py, README.md, and requirements.txt inside it.
✅ Install sentence-transformers in your existing venv.
✅ Add only this import to embedding.py:
from sentence_transformers import SentenceTransformer
🚀 Our New Teaching Style

From this point onward, we are not going to jump straight to complete programs.

We'll build every project exactly like a real software team:

Step 1: Folder structure
Step 2: Why the folder exists
Step 3: Create one file
Step 4: Write one line of code
Step 5: Understand what that line does internally
Step 6: Move to the next line only after you understand the previous one

This is how you'll develop a deep understanding instead of just copying code. Once you finish today's mini assignment, we'll continue with the next single line, where you'll instantiate the SentenceTransformer class and see what happens internally when a pre-trained model is loaded.

Lesson 2 (Part 2)
Loading Your First Embedding Model

Currently your file contains only:

from sentence_transformers import SentenceTransformer

Nothing else.

Step 7

Now write only this line.

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

Don't run it yet.

Let's understand every single character.

Break the line into pieces
model

Question:

What is model?

It is simply a Python variable.

Exactly like

name = "Yukesh"

age = 22

Here,

model = ...

means

Store the embedding model inside the variable named model.

Next Part
SentenceTransformer(...)

Remember our OOP lessons?

This is Object Creation.

Exactly like

student = Student()

or

car = Car()

Here

model = SentenceTransformer(...)

means

Create an object of the SentenceTransformer class.

Question

What object?

Not a student.

Not a car.

An Embedding Model.

Visualize it like this:

SentenceTransformer (Class)

        │

        ▼

MiniLM Model (Object)

        │

        ▼

encode()

save()

tokenize()

...
The String

Now look carefully.

"sentence-transformers/all-MiniLM-L6-v2"

Most beginners think

"This is just a string."

No.

This string is actually an identifier.

Think of it like a GitHub repository.

owner/repository

Example

Yukesh1030/E-Commerce

Similarly

sentence-transformers/all-MiniLM-L6-v2

means

Organization

↓

sentence-transformers

↓

Model Name

↓

all-MiniLM-L6-v2

This tells the library exactly which pre-trained model to download.

Internal Working

When Python reaches

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

it does NOT magically understand English.

Instead, this happens.

Python

↓

SentenceTransformer Library

↓

Check Local Cache

↓

Model Exists?
First Time
No

↓

Connect to Hugging Face

↓

Download Model

↓

Store in Cache

↓

Load into RAM

↓

Return model object
Second Time
Yes

↓

Load From Local Cache

↓

Done

No internet required after the first download.

What is Hugging Face?

You'll hear this name every day in AI.

Think of it as

GitHub

↓

for AI Models

Developers upload

LLMs
Embedding Models
Vision Models
Speech Models

to Hugging Face.

When we specify

SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

the library knows exactly where to fetch it from.

Later in this bootcamp we'll explore Hugging Face in depth.

Why MiniLM?

Question:

Why don't we use GPT-4 or Llama-3 for embeddings?

Because MiniLM is specifically trained to generate embeddings.

It is:

✅ Small

✅ Fast

✅ Lightweight

✅ High Quality

Perfect for RAG.

What Does L6 Mean?
MiniLM

↓

L6

↓

6 Transformer Layers

Remember the Transformer lesson?

Each layer gradually builds a richer understanding of the sentence.

More layers usually mean:

Better understanding
More computation
Slower inference

MiniLM chooses a balance.

What Happens in RAM?

After executing

model = SentenceTransformer(...)

your computer's memory roughly looks like:

RAM

↓

model

↓

MiniLM

↓

Vocabulary

↓

Weights

↓

Neural Network

↓

Tokenizer

Nothing has been embedded yet.

We've only loaded the model into memory.

Question

Has the sentence been converted into vectors?

❌ No.

We haven't provided any sentence.

The model is just waiting.

Think of it like opening Microsoft Word.

Opening Word doesn't mean you've written a document.

Interview Question ⭐⭐⭐⭐⭐
What happens internally when you instantiate SentenceTransformer?

Professional Answer:

When a SentenceTransformer object is created, the library loads the specified pre-trained embedding model. On the first execution, the model is downloaded from Hugging Face and cached locally. On subsequent executions, it is loaded directly from the local cache into memory, making it ready to generate embeddings.

🧠 Small Challenge

Without looking at the next lesson, answer these two questions:

Q1

Why do we need to load the model before calling encode()?

Q2

After running:

model = SentenceTransformer(...)

has any embedding been generated?

Why or why not?

🚀 Next Lesson (Part 3)

Once you answer these two questions, we'll write just one more line:

sentence = "Python is a programming language."

Then you'll learn how that simple sentence travels through:

Sentence

↓

Tokenizer

↓

Token IDs

↓

Transformer

↓

Pooling

↓

384-Dimensional Vector

This is the exact internal pipeline used by modern embedding models, and understanding it will make RAG and vector databases much easier to grasp.



Lesson 2 (Part 3)
Generating Your First Embedding

You already have:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

Now add:

sentence = "Python is a programming language."

and

embedding = model.encode(sentence)

This is the most important line.

What happens inside encode()?

It is not a simple function.

Internally:

Sentence
      │
      ▼
Tokenizer
      │
      ▼
Token IDs
      │
      ▼
Transformer (6 Layers)
      │
      ▼
Contextual Token Embeddings
      │
      ▼
Pooling
      │
      ▼
384-Dimensional Sentence Vector

This entire pipeline executes with just one line:

embedding = model.encode(sentence)
Step 1 — Tokenization

Input:

Python is a programming language.

The tokenizer converts it into pieces:

["Python", "is", "a", "programming", "language", "."]

Then each token gets an ID.

Example (illustrative only):

[2034, 2003, 1037, 4730, 2653, 1012]

These IDs are what the neural network actually processes.

Step 2 — Transformer Processing

Each token passes through the MiniLM transformer.

Instead of looking at words independently, the model considers the entire sentence.

For example:

Python

could mean:

Programming language ✅
Snake 🐍

The surrounding words:

is a programming language

help the model understand the correct meaning.

That's why transformers are called context-aware.

Step 3 — Pooling

After the transformer finishes, every token has its own embedding.

Example:

Python      → Vector A
is          → Vector B
a           → Vector C
programming → Vector D
language    → Vector E

But we don't want five vectors.

We want one vector representing the entire sentence.

The model performs pooling (commonly mean pooling) to combine them into a single sentence embedding.

Token Embeddings

↓

Pooling

↓

One Sentence Embedding
Step 4 — Final Output

Now print:

print(type(embedding))

Expected:

<class 'numpy.ndarray'>

Check the length:

print(len(embedding))

Output:

384

This means the sentence is now represented by a 384-dimensional vector.

Print a small portion:

print(embedding[:10])

Example:

[-0.021
 0.451
-0.112
...
]

Don't worry about the exact values.

The important point is:

The pattern of all 384 numbers together represents the sentence's meaning.

Why Floating-Point Numbers?

Why not integers?

Because neural networks learn continuous representations.

A value like:

0.523784

contains much more information than:

1

The model uses these continuous values to capture subtle semantic relationships.

Your Complete Code
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

sentence = "Python is a programming language."

embedding = model.encode(sentence)

print("Sentence:")
print(sentence)

print("\nLength:")
print(len(embedding))

print("\nType:")
print(type(embedding))

print("\nFirst 10 Values:")
print(embedding[:10])
Interview Questions
1. What does model.encode() do?

Answer:

It converts input text into a dense numerical vector (embedding) that captures the semantic meaning of the text.

2. Why does all-MiniLM-L6-v2 produce a 384-dimensional vector?

Answer:

The model architecture is designed to output a fixed-size sentence embedding of 384 dimensions, providing a balance between semantic quality, speed, and memory usage.

3. Why do we use pooling?

Answer:

The transformer produces embeddings for individual tokens. Pooling combines those token embeddings into a single fixed-length vector representing the entire sentence.

🎯 Mini Assignment

Run the following code:

sentences = [
    "Python is a programming language.",
    "Java is a programming language.",
    "Football is a popular sport."
]

for sentence in sentences:
    embedding = model.encode(sentence)

    print("=" * 60)
    print(sentence)
    print("Vector Length:", len(embedding))
    print("First 5 Values:", embedding[:5])
Observe:
Does every sentence produce 384 dimensions?
Are the vectors different?
Why do you think "Python" and "Java" should eventually be more similar than "Football"?
🚀 Next Lesson (One of the Best Practical Lessons)

We'll stop just generating vectors and start using them.

You'll build your first mini semantic search engine:

User Query
      │
      ▼
Embedding Model
      │
      ▼
Cosine Similarity
      │
      ▼
Rank Sentences
      │
      ▼
Most Similar Result

This is essentially the same retrieval logic used in RAG, ChromaDB, FAISS, and Pinecone, but you'll implement it yourself first so you understand what's happening behind the scenes instead of treating it as a black box.


Lesson 3 – Cosine Similarity (Practical)
🎯 Goal

By the end of this lesson, you'll understand:

✅ Why two similar sentences have similar vectors.
✅ What Cosine Similarity actually measures.
✅ How semantic search works.
✅ The mathematics behind every RAG system.
The Problem

Suppose we have these three sentences:

1. Python is a programming language.

2. Java is a programming language.

3. Football is a popular sport.

Question:

Which sentence is most similar to:

Python Developer

Humans immediately answer:

Python → Java ✅

Python → Football ❌

But how does the computer know this?

Step 1 – Create a New File

Inside:

Embedding-Demo/

Create:

similarity.py

Your structure becomes:

Embedding-Demo/

embedding.py

similarity.py   ⭐

README.md
Step 2 – Install One Library

Run:

pip install scikit-learn

Why?

Because it provides a ready-made Cosine Similarity function.

Later we'll implement it manually.

Freeze again:

pip freeze > requirements.txt
Step 3 – Import
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
Question

What is pairwise?

Imagine five vectors.

A

B

C

D

E

You want to compare every vector with every other vector.

That's called pairwise comparison.

Step 4 – Load Model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

Same as before.

Step 5 – Create Sentences
sentences = [

"Python Developer",

"Java Developer",

"Football Player"

]

Notice something.

These are short.

Why?

To make similarity easier to understand.

Step 6 – Generate Embeddings
embeddings = model.encode(sentences)

Question:

Yesterday we did

embedding = model.encode(sentence)

Today we wrote

embeddings = model.encode(sentences)

Why?

Because

sentence

↓

One vector

Whereas

sentences

↓

Many vectors

Think of it like this:

Sentence 1

↓

Vector 1

------------

Sentence 2

↓

Vector 2

------------

Sentence 3

↓

Vector 3
Step 7 – Compare

Now comes the magic.

similarity_matrix = cosine_similarity(embeddings)
What Happens?

Internally:

Vector 1

↓

Compare

↓

Vector 2

↓

Similarity Score

Repeat for every pair.

Result:

        P      J      F

P      1.0   0.83   0.21

J      0.83  1.0    0.18

F      0.21  0.18   1.0
Understanding the Matrix
Python → Python

1.0

Why?

Anything is 100% similar to itself.

Python → Java

0.83

Very similar.

Python → Football

0.21

Not similar.

Why Is It Called Cosine Similarity?

Imagine each embedding is an arrow in space.

Python  →

Java    →

Football ↑

The algorithm measures the angle between the arrows.

Small angle

↓

High similarity

Large angle

↓

Low similarity

Values

Cosine similarity ranges from:

-1

↓

0

↓

1
Score	Meaning
1.0	Identical meaning
0.8–0.99	Very similar
0.5–0.8	Related
0–0.5	Weakly related
-1	Opposite direction (rare with embeddings)
Step 8 – Print
print(similarity_matrix)

You'll see a 3×3 matrix.

Don't expect exactly my numbers.

Different library versions may produce slightly different scores.

The important observation is:

Python

↓

Java

Higher score

than

Python

↓

Football
Complete Program
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

sentences = [
    "Python Developer",
    "Java Developer",
    "Football Player"
]

embeddings = model.encode(sentences)

similarity_matrix = cosine_similarity(embeddings)

print(similarity_matrix)
Internal Flow
Sentence

↓

Embedding Model

↓

Vector

↓

Cosine Similarity

↓

Similarity Score

Notice:

The LLM is not involved.

Only:

Embedding Model ✅
Mathematics ✅

This is why semantic search is so fast.

Real RAG Connection

Suppose your vector database contains:

Chunk 1

Python Basics

------------

Chunk 2

Java OOP

------------

Chunk 3

Cricket History

User asks:

Explain Python.

The system:

Question

↓

Embedding

↓

Compare with all chunks

↓

Highest Similarity

↓

Return Python Chunk

This is exactly what RAG does before the LLM generates an answer.

Interview Questions ⭐⭐⭐⭐⭐
1. What is Cosine Similarity?

Answer:

Cosine Similarity measures the semantic similarity between two vector embeddings by calculating the cosine of the angle between them. Higher scores indicate greater semantic similarity.

2. Why is Cosine Similarity preferred over Euclidean Distance?

Answer:

Cosine Similarity compares the direction of vectors rather than their magnitude, making it more suitable for high-dimensional text embeddings where semantic meaning is represented by direction.

3. Where is Cosine Similarity used?
Semantic Search
RAG
Vector Databases
Recommendation Systems
Duplicate Detection
Resume Matching
Document Search
🎯 Assignment

Modify your program with these sentences:

sentences = [
    "Python Developer",
    "Software Engineer",
    "Machine Learning Engineer",
    "Cricket Player",
    "Football Coach"
]

Then answer:

Which two sentences had the highest similarity (excluding self-comparisons)?
Which sentence was least similar to "Python Developer"?
Did the similarity scores match your intuition?
🚀 Next Lesson (One of My Favorites)

We'll stop comparing fixed sentences and build your first Mini Semantic Search Engine.

You'll type:

User: Python backend developer

Your program will:

User Query
      │
      ▼
Embedding
      │
      ▼
Compare with 100 sentences
      │
      ▼
Rank by similarity
      │
      ▼
Top 3 Results

At that point, you'll have built the core retrieval mechanism behind production RAG systems—without using LangChain, ChromaDB, or any vector database. Once you understand this, learning those frameworks becomes much easier because you'll know exactly what they're doing under the hood.


Lesson 4 – Build Your Own Semantic Search Engine

This is one of my favorite lessons because you'll build a tiny search engine from scratch.

🎯 Goal

Instead of comparing every sentence manually, we want the computer to answer:

"Which sentence is most similar to my query?"

For example:

Database:

Python Developer

Java Developer

Machine Learning Engineer

Football Player

Doctor

Data Scientist

React Developer

User types:

Python Backend Engineer

Your program should return:

Top Results

1. Python Developer

2. Software Engineer

3. Machine Learning Engineer

This is Semantic Search.

How Does Semantic Search Work?
User Query
      │
      ▼
Embedding Model
      │
      ▼
Query Vector
      │
      ▼
Compare with all stored vectors
      │
      ▼
Similarity Scores
      │
      ▼
Sort (Highest → Lowest)
      │
      ▼
Top Results

Notice something...

❌ No LLM.

Only:

Embedding Model
Cosine Similarity

This is why retrieval is so fast.

Step 1

Create a new file:

Embedding-Demo/

semantic_search.py

Your structure becomes:

Embedding-Demo

embedding.py

similarity.py

semantic_search.py ⭐

README.md
Step 2

Import

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

Nothing new here.

Step 3

Load the model

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
Step 4

Create your "database"

documents = [

"Python Developer",

"Java Developer",

"Machine Learning Engineer",

"React Developer",

"Football Player",

"Doctor",

"Software Engineer",

"AI Engineer"

]

Question:

Why do I call this documents instead of sentences?

Because later these won't be single sentences.

They'll be:

PDF chunks
Resume sections
Website paragraphs
Documentation

This prepares you for RAG.

Step 5

Generate embeddings

document_embeddings = model.encode(documents)

Think of it as:

8 Documents

↓

8 Vectors

These vectors represent your searchable database.

Step 6

Take user input

query = input("Enter your search: ")

Example:

Python Backend Engineer
Step 7

Generate the query embedding

query_embedding = model.encode(query)

Now both the documents and the query are represented as vectors in the same semantic space.

Step 8 (Very Important)

Compare the query vector with all document vectors

similarity_scores = cosine_similarity(
    [query_embedding],
    document_embeddings
)

Why the square brackets?

Because cosine_similarity() expects a 2D array.

query_embedding is one vector.
[query_embedding] makes it a list containing one vector.
Step 9

Print the scores

print(similarity_scores)

Example:

[[0.91
  0.82
  0.78
  0.74
  0.15
  0.11
  0.86
  0.88]]

Each score corresponds to a document.

Step 10

Find the best match

best_index = similarity_scores.argmax()

argmax() returns the index of the highest value.

Example:

Scores

0.91

0.82

0.78

↓

Highest = 0.91

↓

Index = 0
Step 11

Print the result

print("\nBest Match:")
print(documents[best_index])

Output:

Enter your search:

Python Backend Engineer

Best Match:

Python Developer

🎉 You just built your first semantic search engine.

Complete Program
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Python Developer",
    "Java Developer",
    "Machine Learning Engineer",
    "React Developer",
    "Football Player",
    "Doctor",
    "Software Engineer",
    "AI Engineer"
]

document_embeddings = model.encode(documents)

query = input("Enter your search: ")

query_embedding = model.encode(query)

similarity_scores = cosine_similarity(
    [query_embedding],
    document_embeddings
)

best_index = similarity_scores.argmax()

print("\nBest Match:")
print(documents[best_index])
🧠 Interview Question ⭐⭐⭐⭐⭐
What is Semantic Search?

Professional Answer:

Semantic search retrieves information based on the meaning of the query rather than exact keyword matching. It converts both the query and documents into embeddings, computes similarity scores (commonly using cosine similarity), and returns the most semantically relevant results.

🎯 Assignment

Test your program with these queries:

Python Backend Engineer
AI Researcher
Frontend React
Soccer Coach

Observe which document is returned and ask yourself:

Does the result make semantic sense?
Is it matching meaning rather than exact words?
🚀 What Comes After This?

Once you complete this lesson, we'll move to Module 6 – Vector Databases.

You'll finally understand why tools like ChromaDB exist.

Instead of searching through 8 vectors, you'll learn how to search through 10 million vectors in milliseconds, which is exactly what production RAG systems do. This is the point where your AI applications start becoming scalable.


Lesson 5 – Batch Embeddings & Performance
🎯 Today's Goal

Learn:

Why model.encode() one sentence at a time is inefficient
What Batch Processing is
What batch_size means
Why GPUs make embedding generation much faster
Best practices for large datasets
The Problem

Suppose you have:

1 Sentence

Easy.

embedding = model.encode(sentence)

No issues.

Now imagine your company has:

1,000,000 resumes

Can you do this?

for resume in resumes:
    embedding = model.encode(resume)

Yes.

But...

It will be very slow.

Why?

Every call to model.encode() has overhead:

Python

↓

Function Call

↓

Tokenizer

↓

Transformer

↓

Pooling

↓

Return Vector

If you repeat this one million times, the overhead becomes huge.

Batch Processing

Instead of this:

Resume 1

↓

Embedding

↓

Resume 2

↓

Embedding

↓

Resume 3

↓

Embedding

We send all of them together.

Resume 1

Resume 2

Resume 3

Resume 4

↓

Embedding Model

↓

4 Embeddings

One forward pass processes multiple inputs efficiently.

Python Example

Instead of

documents = [
    "Python Developer",
    "Java Developer",
    "AI Engineer"
]

for doc in documents:
    embedding = model.encode(doc)

Do this:

embeddings = model.encode(documents)

The model processes all documents together.

What Happens Internally?

Without batching:

Sentence 1

↓

Transformer

↓

Done

------------

Sentence 2

↓

Transformer

↓

Done

With batching:

Sentence 1

Sentence 2

Sentence 3

↓

Transformer

↓

Sentence Embedding 1

Sentence Embedding 2

Sentence Embedding 3

The GPU/CPU can process multiple inputs in parallel.

Why is Batching Faster?

Imagine washing clothes.

Option 1

Wash one shirt.

Wait.

Wash another shirt.

Wait.

Wash another shirt.

Very slow.

Option 2

Put 20 shirts in the washing machine.

Wash once.

Much faster.

The transformer works similarly.

What is batch_size?

Many models allow:

embeddings = model.encode(
    documents,
    batch_size=32
)

Question:

What does 32 mean?

It means:

Take 32 documents

↓

Generate embeddings

↓

Take next 32

↓

Generate embeddings

Until everything is processed.

Visual

Suppose:

100 Documents

Batch size:

20

Processing:

Batch 1

20 Docs

------------

Batch 2

20 Docs

------------

Batch 3

20 Docs

------------

Batch 4

20 Docs

------------

Batch 5

20 Docs
Why Not Set
batch_size = 100000

Because memory is limited.

Every document consumes RAM or GPU memory.

Too large a batch causes:

Memory Overflow

↓

Out Of Memory (OOM)

↓

Program Crashes
Choosing Batch Size

Typical values:

Device	Batch Size
CPU	8–32
Small GPU	32–64
High-End GPU	128–512

There is no universal "best" batch size.

CPU vs GPU

Suppose:

1000 Sentences

CPU:

1 Worker

↓

Sentence

↓

Sentence

↓

Sentence

GPU:

Thousands of Cores

↓

Many Sentences Together

That's why GPUs are much faster for deep learning workloads.

Simple Benchmark

Let's compare two approaches.

Method 1
for sentence in documents:
    model.encode(sentence)
Method 2
model.encode(documents)

Method 2 is almost always faster.

Real Company Example

Suppose LinkedIn wants embeddings for:

50 Million Resumes

They don't do:

for resume in resumes:
    model.encode(resume)

Instead they:

Batch

↓

GPU

↓

Store in Vector DB

This pipeline runs continuously.

Practical Exercise

Create a new file:

Embedding-Demo/

batch_embedding.py

Paste:

from sentence_transformers import SentenceTransformer
import time

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Python Developer",
    "Java Developer",
    "Machine Learning Engineer",
    "React Developer",
    "AI Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Doctor",
    "Lawyer",
    "Football Player"
]

start = time.time()

embeddings = model.encode(documents)

end = time.time()

print("Generated", len(embeddings), "embeddings")
print("Time:", round(end - start, 4), "seconds")

Run it.

Observe:

Number of embeddings
Execution time
Interview Questions ⭐⭐⭐⭐⭐
1. What is batch processing?

Answer:

Batch processing is the technique of processing multiple inputs together in a single model execution, improving throughput and reducing computational overhead.

2. Why is batching faster?

Answer:

Batching allows the CPU or GPU to process multiple inputs simultaneously, reducing repeated function-call overhead and making better use of hardware resources.

3. What happens if the batch size is too large?

Answer:

If the batch size exceeds available memory, the application may run out of RAM or GPU memory, resulting in an Out Of Memory (OOM) error.

🧠 Industry Insight

When you upload a PDF to ChatGPT Enterprise or a company RAG application, the system doesn't process one paragraph at a time. The pipeline typically looks like this:

PDF

↓

Chunking

↓

1000 Chunks

↓

Batch Embeddings

↓

Vector Database

↓

Ready for Search

Batching is one of the reasons these systems can prepare large documents quickly.

📌 What's Next?

You've now learned:

✅ How embeddings are generated
✅ How similarity search works
✅ How semantic search works
✅ How to optimize embedding generation

The next module is where everything comes together.

🚀 Module 6 – Vector Databases (ChromaDB)

This is one of the biggest milestones in the bootcamp.

You'll finally understand why your friend's project contains files like:

vector_store.py
retriever.py
chunking.py
rag_chain.py

We'll build our own vector database pipeline step by step, starting with:

Lesson 1 – Why Normal Databases (MySQL/PostgreSQL) Are Not Enough for AI Applications?

Once you understand that, ChromaDB will make perfect sense instead of feeling like "just another library."
