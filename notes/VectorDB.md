Module 6 – Vector Databases (ChromaDB)
Module Roadmap
Lesson 1  Why SQL Databases Are Not Enough
Lesson 2  Introduction to Vector Databases
Lesson 3  Installing ChromaDB
Lesson 4  Creating Your First Collection
Lesson 5  Adding Documents
Lesson 6  Metadata
Lesson 7  Embeddings + ChromaDB
Lesson 8  Similarity Search
Lesson 9  Filters
Lesson 10 Persistence
Lesson 11 Build a Mini Knowledge Base
Lesson 12 Connect Everything (Mini RAG)
📍 Lesson 1 – Why Normal Databases Are Not Enough

Before learning ChromaDB, you must answer one interview question:

"If we already have MySQL and PostgreSQL, why do we need ChromaDB?"

If you can answer this, you've understood vector databases.

Imagine This Scenario

Suppose you're building a Resume Search Portal.

Database:

Resume 1
Python Developer

Resume 2
Java Backend Engineer

Resume 3
Machine Learning Engineer

Resume 4
Doctor

A recruiter searches:

AI Engineer
Using MySQL

Your table might look like:

id	name	role
1	John	Python Developer
2	Alice	Java Backend Engineer
3	Bob	Machine Learning Engineer

Now imagine you run:

SELECT * FROM resumes
WHERE role = 'AI Engineer';

Output:

0 Results

Why?

Because "AI Engineer" doesn't exactly exist.

Another Query
Software Engineer

Database contains:

Python Developer

Should it match?

As humans,

✅ Yes.

But SQL says

❌ No.

Why?

Traditional databases compare:

Characters

Example:

Python Developer

AI Engineer

SQL internally checks:

P == A ?

No

It doesn't understand meaning.

SQL Understands Exact Values

SQL is excellent at questions like:

SELECT * FROM employees
WHERE age > 25;

or

WHERE salary > 100000;

or

WHERE city = 'Salem';

These are structured data queries.

But AI Uses Unstructured Data

Examples:

PDFs

Emails

Books

Resumes

Websites

Research Papers

Chat History

These don't have fixed columns.

Instead, we care about meaning.

We Already Solved This!

Remember Module 5?

We learned:

Sentence

↓

Embedding Model

↓

Vector

Example:

Python Developer

↓

[0.12, -0.45, 0.81, ...]
Then We Learned
Cosine Similarity

So instead of comparing:

Text

vs

Text

We compare:

Vector

vs

Vector

That's the breakthrough.

The Problem with MySQL

Suppose your company has:

20 Million PDF Chunks

Can you store vectors in MySQL?

Technically...

Yes.

Example:

id	embedding
1	[0.12,0.44,...]

But now imagine searching:

Compare this vector against

20 Million vectors.

SQL was not designed for this.

It becomes very slow.

Why?

SQL indexes are built for:

Numbers
Dates
Strings

Not for:

384-dimensional vectors

768-dimensional vectors

1536-dimensional vectors

Searching high-dimensional vectors efficiently is a completely different problem.

This Is Why Vector Databases Exist

Instead of:

MySQL

↓

Exact Match

We use:

ChromaDB

↓

Similarity Search
Comparison
MySQL	ChromaDB
Structured data	Embeddings
SQL Queries	Similarity Search
Exact matching	Semantic matching
Numbers & Strings	Dense vectors
Customer Records	AI Knowledge
Real-World Example

Suppose ChatGPT has stored millions of document chunks.

You ask:

How does Python inheritance work?

System:

Question

↓

Embedding

↓

ChromaDB

↓

Top 5 Similar Chunks

↓

LLM

↓

Answer

Notice something important:

❌ The LLM did not search all documents.

✅ ChromaDB did.

The LLM only reads the retrieved chunks.

This is why RAG is efficient.

Where Does ChromaDB Fit?
PDF

↓

Chunking

↓

Embeddings

↓

ChromaDB ⭐

↓

Retriever

↓

LLM

↓

Answer

This is the exact architecture used in your friend's project.

Interview Question ⭐⭐⭐⭐⭐
Q1. Why can't we use MySQL for RAG?

Professional Answer:

MySQL is designed for structured data and exact-value queries. It does not efficiently support high-dimensional vector similarity search. RAG applications require semantic retrieval based on embeddings, which is why vector databases such as ChromaDB, Pinecone, and FAISS are used.

Q2. What is a Vector Database?

Professional Answer:

A vector database stores embedding vectors and enables efficient similarity search using algorithms optimized for high-dimensional data. It is a core component of Retrieval-Augmented Generation (RAG) systems.

🏗️ Project Architecture (What We'll Build)

By the end of Module 6, your project structure will evolve into:

AI-BOOTCAMP/
│
├── projects/
│   ├── AI-Chatbot/
│   ├── Embedding-Demo/
│   └── ChromaDB-Demo/
│       ├── app.py
│       ├── documents/
│       ├── chroma_db/
│       ├── requirements.txt
│       └── README.md
│
└── notes/

We'll build this project from scratch together.

🎯 Today's Assignment

There is no coding for this lesson.

Instead, answer these three questions in your own words:

Why is MySQL not suitable for semantic search?
Why do we convert text into vectors before storing it?
Where does ChromaDB fit in the RAG pipeline?

If you can answer those confidently, you've understood the reason behind vector databases—not just how to use them.

🚀 Next Lesson

We'll start coding.

You'll create a new project called ChromaDB-Demo, install ChromaDB, understand what a Collection is (the equivalent of a table in SQL), and insert your very first AI documents into a vector database. This is where your theoretical knowledge begins turning into a real RAG application.

Lesson 2 – Installing ChromaDB & Creating Your First Collection
🎯 Lesson Goal

By the end of this lesson, you'll understand:

✅ What ChromaDB is
✅ What a Collection is
✅ How to install ChromaDB
✅ How ChromaDB stores data
✅ Folder structure
✅ Your first ChromaDB program
Before We Code

Let's compare SQL and ChromaDB.

SQL Database	ChromaDB
Database	Chroma Client
Table	Collection
Row	Document
Column	Metadata
Primary Key	Document ID
SQL Query	Similarity Search

If you already know MySQL, then:

MySQL Table

↓

employees

becomes

ChromaDB Collection

↓

employees

A Collection is simply a group of documents.

Project Structure

Inside your AI Bootcamp create a new project.

AI-BOOTCAMP

│

├── projects

│     │

│     ├── AI-Chatbot

│     │

│     ├── Embedding-Demo

│     │

│     └── ChromaDB-Demo ⭐

│            app.py

│            README.md

│            requirements.txt
Step 1

Open your terminal.

Go to

AI-BOOTCAMP

Your terminal should look like

(venv)

E:\learn\GenAI\AI-BOOTCAMP>
Step 2

Install ChromaDB.

pip install chromadb

Wait until installation completes.

Step 3

Freeze the packages.

pip freeze > requirements.txt

Exactly like previous modules.

Step 4

Open

projects/

↓

ChromaDB-Demo/

↓

app.py
Step 5

Import ChromaDB

Write

import chromadb
What is chromadb?

Exactly like

import numpy

import requests

import pandas

It is simply a Python package.

Step 6

Create a Client

Write

client = chromadb.Client()

Don't run yet.

Let's understand this.

What is a Client?

Think about MySQL.

When connecting:

mysql.connect(...)

You get a connection object.

Similarly,

client = chromadb.Client()

creates a connection to ChromaDB.

Visualize it:

Python

↓

Client

↓

ChromaDB

The client is your gateway.

Step 7

Create a Collection

Now write

collection = client.create_collection(
    name="employees"
)
What just happened?

Imagine SQL.

CREATE TABLE employees

In ChromaDB

client.create_collection(
    name="employees"
)

They're conceptually similar.

Visual
ChromaDB

│

├── employees

├── resumes

├── books

├── products

Each one is a collection.

Step 8

Print it

print(collection)

Run the program.

Expected output (similar to):

Collection(name=employees)

🎉 Congratulations!

You just created your first vector database collection.

Complete Program
import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="employees"
)

print(collection)
What Actually Happens?

When you execute:

client = chromadb.Client()

A ChromaDB instance starts in memory.

Then

create_collection()

creates an empty container.

At this point:

employees

↓

Documents : 0

Vectors : 0

Metadata : 0

The collection exists, but it's empty.

Important Concept

Think of a collection as a folder.

employees/

↓

(empty)

Soon we'll add documents.

Interview Question ⭐⭐⭐⭐⭐
What is a Collection?

Professional Answer:

A collection in ChromaDB is a logical container that stores documents, their embeddings, metadata, and unique IDs. It is conceptually similar to a table in a relational database but is designed for vector search.

Mini Assignment

Complete these tasks:

1.

Create

projects/

↓

ChromaDB-Demo
2.

Install

pip install chromadb
3.

Run

pip freeze > requirements.txt
4.

Create

import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="employees"
)

print(collection)
⚠️ One Important Note

The client we used today:

client = chromadb.Client()

creates an in-memory database.

That means:

Run Program

↓

Create Collection

↓

Stop Program

↓

Everything is Lost

This is useful for learning but not for real applications.

In the next lesson, you'll learn how to create a persistent ChromaDB database that saves everything to disk.

📍 Next Lesson (Lesson 3)

You'll learn:

Why your data disappears after the program ends
What PersistentClient is
How ChromaDB creates a local database folder
Where embeddings are physically stored
How to reopen the same database after restarting your application

This is the point where your ChromaDB setup starts behaving like a real database rather than a temporary in-memory store.