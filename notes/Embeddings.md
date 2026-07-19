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