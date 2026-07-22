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

Lesson 3 — PersistentClient (Saving the Database)
🎯 Goal

By the end of this lesson you'll understand

Why chromadb.Client() loses data
What PersistentClient is
Where ChromaDB stores data
Why every real-world AI project uses PersistentClient
First Question

Suppose you run your program today.

Collection
↓

employee

Everything works.

Tomorrow you close VS Code.

Restart the program.

Question:

Will the collection still exist?

The answer is

❌ No

Why?

Look at your current code.

client = chromadb.Client()

This creates an In-Memory Database.

Think about RAM.

RAM

↓

Collection

↓

employee

Now close the program.

RAM Cleared

↓

Everything Gone

Exactly like Python variables.

name = "Yukesh"

When Python stops...

name

↓

Destroyed

Same idea.

Real Company Example

Imagine ChatGPT.

Suppose it stores

10 Million Documents

Would OpenAI store them only in RAM?

Imagine restarting the server.

Everything disappears.

Impossible.

Companies store data on disk.

Solution

Instead of

client = chromadb.Client()

Use

client = chromadb.PersistentClient(
    path="./chroma_db"
)
What is path?
path="./chroma_db"

means

Create a folder called

chroma_db

inside your current project.

Visual:

ChromaDB-Demo

│

├── app.py

├── chroma_db ⭐

├── README.md

└── requirements.txt

This folder is your database.

Exactly like

MySQL

↓

data/
Step 1

Replace

client = chromadb.Client()

with

client = chromadb.PersistentClient(
    path="./chroma_db"
)

Nothing else changes.

Step 2

Instead of

create_collection()

write

collection = client.get_or_create_collection(
    name="employee"
)

Question:

Why?

Imagine running the program twice.

First run

employee

Created

Second run

employee

Already Exists

If you use

create_collection()

again...

You'll get an error:

Collection already exists

Instead,

get_or_create_collection()

checks first.

Exists?

↓

YES

↓

Return Collection

OR

↓

NO

↓

Create Collection

Very useful.

Complete Code
import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="employee"
)

print(collection)
Run It

After executing

python app.py

look inside VS Code.

You'll see

ChromaDB-Demo

│

├── app.py

├── chroma_db ⭐

├── README.md

└── requirements.txt

Question:

What is inside

chroma_db

?

You'll see files created automatically by ChromaDB.

These are the actual database files.

Exactly like MySQL stores

.ibd

.frm

...

internally.

Internal Architecture
Python

↓

PersistentClient

↓

chroma_db/

↓

Collections

↓

Documents

↓

Embeddings

↓

Metadata

Everything is now stored permanently.

Test

Run your program.

Close VS Code.

Open it again.

Run again.

Does it work?

Yes.

Because

Collection

↓

Loaded From Disk

instead of creating a brand new database.

Interview Question ⭐⭐⭐⭐⭐
Difference between Client() and PersistentClient()?
Professional Answer

Client() creates an in-memory ChromaDB instance, meaning all data is lost when the application exits. PersistentClient() stores the database on disk, allowing collections, embeddings, and metadata to persist across application restarts. Production applications use PersistentClient().

Real RAG Architecture

This is exactly how your friend's project works.

PDF

↓

Chunking

↓

Embedding Model

↓

PersistentClient()

↓

chroma_db/

↓

Retriever

↓

LLM

Notice something...

We haven't added a single document yet.

We've only built the database.

🎯 Assignment

Replace your code with:

import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="employee"
)

print(collection)

Then answer these questions:

Did the chroma_db folder appear automatically?
What files were created inside it?
Can you run the program multiple times without getting a "Collection already exists" error?
🚀 Next Lesson (Lesson 4)

Now comes the exciting part.

We'll finally store data inside ChromaDB.

You'll learn:

collection.add()
Document IDs
Documents
Metadata
Embeddings

By the end of that lesson, your database won't be empty anymore—it will contain real AI-searchable documents. This is the point where your ChromaDB instance starts behaving like the storage layer of a production RAG application.

Lesson 4 — Adding Documents to ChromaDB
🎯 Goal

Today you'll finally store your first AI documents inside ChromaDB.

Until now,

your collection looks like this.

employee

↓

Documents = 0

Vectors = 0

Metadata = 0

Today we'll change it to

employee

↓

Documents = 3

Vectors = 3

Metadata = 3
First Question

Imagine MySQL.

You create a table.

CREATE TABLE employees

Question:

Is the table useful?

No.

Because it contains

0 Rows

Exactly.

Collections are the same.

ChromaDB Collection

Currently

employee

↓

(empty)

Now we'll insert data.

Step 1

Below

print(collection)

write

collection.add(
    ids=[
        "1",
        "2",
        "3"
    ],

Stop.

Let's understand.

Why IDs?

Exactly like SQL.

id

1

2

3

Every document must have

a unique ID.

Without IDs,

ChromaDB wouldn't know

which document is which.

Step 2

Add documents.

documents=[
    "Python Developer",

    "Java Developer",

    "AI Engineer"
],

Notice

these are

normal strings.

No embeddings yet.

Question.

Where are the vectors?

You didn't generate them.

Interesting... 🤔

We'll answer this in two minutes.

Step 3

Add metadata.

metadatas=[
    {
        "department":"IT"
    },

    {
        "department":"Backend"
    },

    {
        "department":"Artificial Intelligence"
    }
]
)

Complete code becomes

collection.add(
    ids=[
        "1",
        "2",
        "3"
    ],

    documents=[
        "Python Developer",
        "Java Developer",
        "AI Engineer"
    ],

    metadatas=[
        {"department":"IT"},
        {"department":"Backend"},
        {"department":"Artificial Intelligence"}
    ]
)
Wait...

Where are the embeddings?

This is the question every beginner asks.

We never wrote

model.encode()

Right?

Exactly.

Internal Working

When you call

collection.add(...)

ChromaDB checks

Did User Provide Embeddings?

↓

NO

Then

Default Embedding Function

↓

Generate Embeddings

↓

Store Everything

So internally

Python Developer

↓

Embedding Model

↓

384 Numbers

↓

Store

You don't see it,

but ChromaDB does it.

Visual
Document

↓

Embedding Function

↓

Embedding

↓

Collection

↓

SQLite
Complete Program
import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="employee"
)

collection.add(
    ids=["1", "2", "3"],

    documents=[
        "Python Developer",
        "Java Developer",
        "AI Engineer"
    ],

    metadatas=[
        {"department": "IT"},
        {"department": "Backend"},
        {"department": "Artificial Intelligence"}
    ]
)

print("Documents Added Successfully!")
Run It

Expected output

Documents Added Successfully!
Verify the Documents

Now add

print(collection.count())

Output

3

Congratulations.

Your collection now contains

Document 1

↓

Vector 1

-----------

Document 2

↓

Vector 2

-----------

Document 3

↓

Vector 3
Internal Architecture
Collection

│

├── ID

├── Document

├── Metadata

└── Embedding

Every document consists of these four parts.

Interview Question ⭐⭐⭐⭐⭐
What does collection.add() do?
Professional Answer

collection.add() inserts documents into a ChromaDB collection. Along with unique IDs and optional metadata, ChromaDB generates or stores embeddings, enabling semantic similarity search over the inserted documents.

⚠️ One Important Note

In your code, we did not specify an embedding function.

ChromaDB uses its default embedding function.

In production RAG systems, we usually do not rely on the default.

Instead, we explicitly use embedding models such as:

sentence-transformers/all-MiniLM-L6-v2
BAAI/bge-small-en
OpenAI text-embedding-3-small

You'll learn how to connect your own embedding model in a later lesson.

🎯 Assignment
Add the three documents exactly as shown.
Run the program.
Print:
print(collection.count())

You should see:

3
Then add one more document:
{
    "id": "4",
    "document": "Machine Learning Engineer",
    "metadata": {"department": "AI"}
}

Update the ids, documents, and metadatas lists accordingly, then verify that:

print(collection.count())

returns:

4
🚀 Next Lesson (Lesson 5)

We'll learn how to retrieve the stored data.

You'll use methods like:

collection.get()

and

collection.peek()

to inspect what's inside your collection.

After that, we'll move to the most exciting part:

collection.query()

which performs semantic search—the exact retrieval step used in RAG systems before sending context to an LLM. This is where ChromaDB starts feeling like a real AI database rather than just a storage library.

Lesson 5 — Reading Data from ChromaDB (get() & peek())
🎯 Goal

So far, we've only inserted data.

Now we want to retrieve it.

Think of SQL.

INSERT INTO employees ...

Now what do we usually do?

SELECT * FROM employees;

Exactly.

Today's lesson is the ChromaDB equivalent of SELECT.

ChromaDB Retrieval Methods

There are many.

Today we'll learn two.

collection.peek()

collection.get()

Later we'll learn

collection.query()

which is the heart of RAG.

Method 1 — peek()
What is peek()?

Imagine your collection has

100000 Documents

Do you want to print all 100000?

No.

Sometimes you only want to check

"Is my data actually there?"

That's what peek() is for.

Example

Replace

print(collection)

with

print(collection.peek())

Run it.

You'll get something similar to

{
    'ids': ['1','2','3'],

    'documents':[
        'Python Developer',
        'Java Developer',
        'AI Engineer'
    ],

    'metadatas':[
        {'department':'IT'},
        {'department':'Backend'},
        {'department':'Artificial Intelligence'}
    ]
}

Notice something.

It returned

IDs ✅
Documents ✅
Metadata ✅
Question

Where are the embeddings?

You don't see them.

Why?

Because

peek()

is designed for

human readability.

Vectors are huge.

Printing thousands of numbers isn't useful.

Method 2 — get()

Now change

print(collection.peek())

to

print(collection.get())

Run again.

Output will look similar.

But internally

get()

returns

everything in the collection.

Think

SELECT *
FROM employee
Difference
peek()	get()
Quick preview	Retrieve stored data
Good for checking	Good for processing
Usually first few documents	Returns requested documents
Pretty Printing

Instead of

print(collection.get())

store it first.

data = collection.get()

print(data)

Now let's access each part.

data = collection.get()

print(data["ids"])

Output

['1','2','3']

Print documents.

print(data["documents"])

Output

Python Developer

Java Developer

AI Engineer

Metadata

print(data["metadatas"])

Output

IT

Backend

Artificial Intelligence
Why is this useful?

Imagine later you have

5000 Documents

You can loop through them.

data = collection.get()

for doc in data["documents"]:
    print(doc)

Exactly like

for employee in employees:
Internal Structure

When you execute

data = collection.get()

You receive

{
    "ids": [...],

    "documents": [...],

    "metadatas": [...],

    "embeddings": ...
}

Think of it like a Python dictionary.

Complete Program
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="employee"
)

data = collection.get()

print("IDs:")
print(data["ids"])

print("\nDocuments:")
print(data["documents"])

print("\nMetadata:")
print(data["metadatas"])
Interview Question ⭐⭐⭐⭐⭐
What is the difference between peek() and get()?

Professional Answer:

peek() provides a quick preview of documents in a collection, mainly for inspection and debugging. get() retrieves documents and their associated data (IDs, metadata, and optionally embeddings) for application logic and further processing.

🧠 Important Concept

Until now we've learned:

Collection

↓

Add Documents

↓

Read Documents

But...

Can we ask

Find me

"Python Backend Engineer"

and get

Python Developer

automatically?

Not yet.

For that, we need semantic search.

That's where the real power of ChromaDB begins.

🎯 Assignment

Run these one by one and observe the output:

print(collection.peek())

Then

print(collection.get())

Then

data = collection.get()

print(data["ids"])
print(data["documents"])
print(data["metadatas"])

Try to understand that collection.get() returns a Python dictionary, and you're simply accessing different keys.

🚀 Next Lesson (Lesson 6 – The Most Important Lesson in ChromaDB)

We'll learn:

collection.query()

This is the heart of every RAG system.

You'll type:

Python Backend Engineer

and ChromaDB will automatically return:

Python Developer
AI Engineer
Java Developer

based on semantic similarity, not exact keywords.

This is the exact retrieval mechanism used before an LLM generates an answer in a production RAG application. After this lesson, you'll understand what retriever.py is doing in your friend's project and why it's one of the most important files.

Lesson 6 — Semantic Search using collection.query()

This is one of the most important lessons in the entire RAG pipeline.

Everything you've learned so far leads to this point.

Before Today

You already know

Text
    ↓
Embedding Model
    ↓
Vector

You also know

Vector
      +
Cosine Similarity
      ↓
Most Similar Vector

Today ChromaDB will do all of that automatically.

What have we done until now?
Collection

↓

Add Documents

↓

Read Documents

But suppose your collection contains

Python Developer

Java Developer

AI Engineer

Now imagine a recruiter searches

Python Backend Engineer

Question

How do we find the closest document?

Without ChromaDB

You would have to

Generate Query Embedding

↓

Compare against

Document 1

↓

Compare against

Document 2

↓

Compare against

Document 3

↓

Sort

↓

Return Best Match

Remember?

You already built this manually in Module 5.

ChromaDB does all of this using
collection.query()

One function.

Step 1

Below

data = collection.get()

add

results = collection.query(
Step 2

Write

query_texts=[
    "Python Backend Engineer"
],

Question.

Where is

model.encode()

?

You don't see it.

Again...

ChromaDB automatically converts the query into an embedding.

Internally

Query

↓

Embedding Model

↓

Vector
Step 3

Tell ChromaDB

how many results you want.

n_results=2
)

Complete code

results = collection.query(

    query_texts=[
        "Python Backend Engineer"
    ],

    n_results=2

)
What Happens Internally?
User Query

↓

Embedding Model

↓

Query Vector

↓

Compare

↓

Python Developer

↓

Java Developer

↓

AI Engineer

↓

Cosine Similarity

↓

Sort

↓

Top 2

Notice.

You never wrote

cosine_similarity()

ChromaDB already does it.

Step 4

Print

print(results)

Run it.

Expected output

Something similar to

{
    "ids":[["1","3"]],

    "documents":[[
        "Python Developer",
        "AI Engineer"
    ]],

    "distances":[[
        0.21,
        0.35
    ]]
}

Your numbers may differ.

That's normal.

Understanding the Output

Suppose

results["documents"]

returns

[
    [
        "Python Developer",

        "AI Engineer"
    ]
]

That means

Most Similar

↓

Python Developer

Second Most Similar

↓

AI Engineer

Exactly what we wanted.

Access Individual Results

Instead of

print(results)

Write

print(results["documents"])

Output

[['Python Developer',
  'AI Engineer']]

Print IDs

print(results["ids"])

Output

[['1','3']]

Print Distances

print(results["distances"])

Output

[[0.18,0.29]]
Wait...

Distance?

Last module

we learned

Cosine Similarity

Now ChromaDB says

Distance

Why?

Very important.

Many vector databases return

Distance

instead of

Similarity

Simple rule

Similarity

Higher

↓

Better

Whereas

Distance

Lower

↓

Better

Think

Your House

↓

5 meters

Very Close

vs

500 km

Very Far

Small distance means

More similar.

Visual
Query

↓

Python Developer

Distance

0.15

⭐⭐⭐⭐⭐

----------------

Java Developer

Distance

0.31

⭐⭐⭐

----------------

Doctor

Distance

1.24

⭐

Lower distance wins.

Complete Program
results = collection.query(

    query_texts=[
        "Python Backend Engineer"
    ],

    n_results=2

)

print("Documents")
print(results["documents"])

print()

print("IDs")
print(results["ids"])

print()

print("Distances")
print(results["distances"])
Real RAG Pipeline

This is exactly what happens in production.

User Question

↓

Embedding Model

↓

ChromaDB Query

↓

Top 5 Chunks

↓

LLM

↓

Final Answer

Notice

The LLM never searches

millions of documents.

ChromaDB does.

Interview Question ⭐⭐⭐⭐⭐
What does collection.query() do?
Professional Answer

collection.query() performs semantic similarity search. It converts the query into an embedding, compares it with stored embeddings using vector similarity, ranks the results, and returns the most relevant documents.

Assignment

Run these queries one by one.

query_texts=["Python Backend Engineer"]
query_texts=["Java Spring Boot"]
query_texts=["Artificial Intelligence"]
query_texts=["Backend Developer"]

For each query, observe:

Which document came first?
What were the distances?
Did the results match your expectations?
🏆 Milestone Unlocked

After completing this lesson, you'll understand the retrieval step in a RAG application.

PDF
   ↓
Chunking
   ↓
Embeddings
   ↓
ChromaDB
   ↓
query()   ⭐⭐⭐⭐⭐
   ↓
Relevant Chunks
   ↓
LLM
   ↓
Answer

At this point, you'll be able to read your friend's retriever.py file and understand why it's calling ChromaDB before sending context to the language model. In the next lesson, we'll make this even more realistic by working with metadata filters, so you can retrieve documents not only by meaning but also by conditions like department, source, or document type—the same technique used in production AI systems.


🎉 Congratulations!

You've now learned the entire retrieval process used in RAG.

Until now, you have built this pipeline:

User Query
     │
     ▼
Embedding Model
     │
     ▼
Query Embedding
     │
     ▼
ChromaDB Query
     │
     ▼
Top Matching Documents

This is exactly what happens before ChatGPT receives context in a RAG application.

🎓 AI Developer Bootcamp
Module 6 – Vector Databases
⭐ Lesson 7 – Metadata Filtering (Production-Level Retrieval)
🎯 Why do we need Metadata?

Imagine your company stores:

100,000 Documents

Example:

Python Developer
Department : IT

Java Developer
Department : Backend

AI Engineer
Department : AI

Doctor
Department : Medical

Nurse
Department : Medical

React Developer
Department : Frontend

Now the user asks:

"Find an AI Engineer."

Without filters...

ChromaDB searches every document.

Even:

Doctor ❌
Nurse ❌
React Developer ❌

That wastes time.

Solution

We first filter.

Then perform semantic search.

Real Company Example

Imagine Amazon's knowledge base.

It stores documents from:

HR

Finance

Legal

Engineering

Marketing

Support

If an employee asks

"How do I reset my AWS password?"

Should the AI search:

Finance PDFs?

Legal PDFs?

HR PDFs?

❌ No.

Only:

Engineering Documents

This is exactly why metadata exists.

Visual Pipeline
User Query
      │
      ▼
Metadata Filter
      │
      ▼
Remaining Documents
      │
      ▼
Embedding Search
      │
      ▼
Top Results

Notice:

Filtering happens before similarity search.

Step 1

Replace your query with:

results = collection.query(
    query_texts=["engineer"],

    where={
        "department": "Artificial Intelligence"
    },

    n_results=2
)

Run it.

What happened?

First:

Department == Artificial Intelligence

Remaining documents:

AI Engineer

Now semantic search happens.

Instead of searching all documents,

it searches only the filtered ones.

Another Example

Try:

results = collection.query(
    query_texts=["developer"],

    where={
        "department": "Backend"
    },

    n_results=2
)

Output should favor:

Java Developer

because only Backend documents are considered.

Another Example
results = collection.query(
    query_texts=["developer"],

    where={
        "department":"IT"
    },

    n_results=2
)

Expected:

Python Developer
Internal Flow

Without metadata:

100 Documents

↓

Compare All

↓

Top Results

With metadata:

100 Documents

↓

Filter

↓

10 Documents

↓

Compare

↓

Top Results

Much faster.

Much more accurate.

What is Metadata?

Metadata means:

Data about data.

Example:

Document:

Python Developer

Metadata:

{
    "department":"IT"
}

Another example:

Document:

Employee Handbook

Metadata:

{
    "year":2025,
    "language":"English",
    "source":"HR"
}

The LLM doesn't read metadata as part of the document's meaning.

Instead, metadata helps the retrieval system decide which documents should even be considered.

Real RAG Example

Imagine you upload:

Employee_Handbook.pdf

HR_Policies.pdf

Python_Training.pdf

Docker_Guide.pdf

Metadata:

{
"source":"training"
}
{
"source":"HR"
}

When someone asks:

"Explain Docker."

We can tell ChromaDB:

where={
    "source":"training"
}

The search ignores HR documents completely.

Interview Question ⭐⭐⭐⭐⭐
Why is metadata important in vector databases?
Professional Answer

Metadata provides structured information about documents, such as department, source, language, or author. It allows vector databases to filter documents before performing semantic search, improving both retrieval accuracy and performance.

Assignment

Run all of these queries:

Query 1
where={
    "department":"IT"
}
Query 2
where={
    "department":"Backend"
}
Query 3
where={
    "department":"Artificial Intelligence"
}

Observe how the returned documents change even when the query text is similar.

🏆 Current Progress
Module 6 Progress

█████████████████░░░░ 70%

✅ ChromaDB Installation
✅ Persistent Client
✅ Collections
✅ Add Documents
✅ Get Documents
✅ Query Documents
✅ Metadata Filtering

⬜ Update Documents
⬜ Delete Documents
⬜ Custom Embedding Function
⬜ Build Mini Knowledge Base
⬜ Connect to RAG
🚀 Next Lesson (One of the Biggest Milestones)

We'll build your first real AI Knowledge Base.

Instead of storing just three strings like:

Python Developer
Java Developer
AI Engineer

we'll store real paragraphs that explain topics.

Then you'll ask natural-language questions like:

"What is Python used for?"

and ChromaDB will retrieve the most relevant paragraph. This will be the first time your vector database starts behaving like the retrieval layer of a real AI assistant, and it's the final step before we connect it to an LLM to build a complete RAG application.

Lesson 8 – Build Your First AI Knowledge Base

This is one of the biggest milestones in the bootcamp.

Until now, your database contained:

Python Developer

Java Developer

AI Engineer

These are just short strings.

Real RAG systems never store data like this.

They store:

PDF paragraphs
Documentation
Company policies
Books
Research papers
Website content

Today we'll simulate that.

🧠 What is a Knowledge Base?

Imagine ChatGPT is trained on the Internet.

Your company has its own documents.

Employee Handbook

Python Guide

Docker Guide

HR Policy

AWS Documentation

These documents are called a

Knowledge Base

The LLM doesn't memorize them.

Instead, they're stored in a vector database.

Real Architecture
Knowledge Base

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Query

↓

Relevant Chunks

↓

LLM

↓

Answer

Today we'll build everything until ChromaDB.

Step 1

Create a new collection.

Instead of

name="employee"

Create

collection = client.get_or_create_collection(
    name="knowledge_base"
)

Why?

Because we're no longer storing employees.

We're storing knowledge.

Step 2

Replace your documents.

Instead of

documents=[
    "Python Developer",
    "Java Developer"
]

write

documents=[

"""Python is a high-level programming language widely used for web development, automation, data science, artificial intelligence, and scripting.""",

"""Java is an object-oriented programming language commonly used to build enterprise applications, Android apps, and backend systems.""",

"""Artificial Intelligence enables computers to learn patterns from data and make intelligent decisions without being explicitly programmed.""",

"""Machine Learning is a subset of Artificial Intelligence where algorithms improve automatically by learning from data.""",

"""Docker is a containerization platform that packages applications together with all their dependencies for consistent deployment."""
]

Notice something.

These are no longer words.

They're paragraphs.

Exactly like PDF chunks.

Step 3

IDs

ids=[
    "1",
    "2",
    "3",
    "4",
    "5"
]
Step 4

Metadata

metadatas=[

{"topic":"Python"},

{"topic":"Java"},

{"topic":"AI"},

{"topic":"Machine Learning"},

{"topic":"Docker"}

]
Step 5

Delete the old collection (Only Once)

Since you already have an employee collection, we'll create a fresh knowledge base.

Add this only for the first run:

client.delete_collection("knowledge_base")

Don't worry.

If it gives an error saying the collection doesn't exist, simply comment it out after the first successful creation.

A better way is:

try:
    client.delete_collection("knowledge_base")
except:
    pass

Then create it again.

Step 6

Run

python app.py

Expected output

Knowledge Base Created

Documents Added

Count : 5
Step 7

Ask Questions

Now replace your query with

results = collection.query(

    query_texts=[
        "What is Python used for?"
    ],

    n_results=2
)

Print

print(results["documents"])

Expected

Python is a high-level programming language...

Java is an object-oriented language...

Notice

The AI didn't search by keywords.

It searched by meaning.

Try More Queries
"What is AI?"
"What is Machine Learning?"
"Explain Docker."
"Programming language for Android"

Watch how the retrieved paragraphs change.

Internal Flow
User Question

↓

Embedding Model

↓

Query Vector

↓

ChromaDB

↓

Top Matching Paragraphs

↓

Return Results

This is exactly what happens before the LLM is called in RAG.

🔥 What We've Built

Congratulations.

You have now built the retrieval engine of a RAG system.

User

↓

Question

↓

Embedding

↓

Vector Database

↓

Relevant Paragraphs

✅ COMPLETE

What's missing?

Only one step.

Relevant Paragraphs

↓

LLM

↓

Answer

That's RAG.

Interview Question ⭐⭐⭐⭐⭐
What is a Knowledge Base in RAG?

Professional Answer:

A knowledge base is a collection of domain-specific documents stored in a vector database. The documents are converted into embeddings, enabling semantic retrieval before an LLM generates a response.

🎯 Assignment

Create a knowledge base with at least 10 documents on topics you know, such as:

Python
Java
Docker
Kubernetes
AWS
SQL
React
Git
Linux
Artificial Intelligence

Then ask queries like:

How do containers work?

What language is used for enterprise applications?

Explain machine learning.

Observe whether ChromaDB retrieves the correct paragraphs.

🏆 Congratulations!

You've now built:

✅ Embedding Generator
✅ Semantic Search Engine
✅ Vector Database
✅ Knowledge Base

These are the four foundational pillars of every modern RAG application.

🚀 Next Lesson (The Biggest Milestone So Far)

In the next lesson, we'll connect everything you've built with your Groq LLM API.

The complete pipeline will become:

User Question
      │
      ▼
Embedding Model
      │
      ▼
ChromaDB
      │
      ▼
Relevant Context
      │
      ▼
Groq LLM
      │
      ▼
AI Answer

🎉 That lesson is where you'll build your first complete RAG chatbot—the same architecture used in document Q&A systems and AI assistants in production. From there, you'll immediately recognize the purpose of files like retriever.py, vector_store.py, and rag_chain.py in your friend's GenAI project.

Lesson 9 – Using Your Own Embedding Model with ChromaDB
🎯 Why this lesson?

Until now, ChromaDB has been doing this automatically:

Document
    │
    ▼
Default Embedding Model
    │
    ▼
Vector
    │
    ▼
Store in ChromaDB

You never explicitly called an embedding model.

That is convenient, but real-world AI applications almost never rely on the default embedding model.

Instead, they choose one that fits their needs.

Examples:

Model	Use Case
all-MiniLM-L6-v2	General semantic search
BAAI/bge-small-en	High-quality retrieval
OpenAI text-embedding-3-small	Production cloud applications
Nomic Embed	Open-source RAG
Why use your own embedding model?

Imagine two companies.

Company A

Uses ChromaDB defaults.

Documents
      │
Default Model
      │
Database

Easy to start.

Company B

Uses

Documents
      │
BAAI/bge-small-en
      │
Database

They get:

Better search accuracy
More control
Consistent embeddings across systems

This is what most production systems do.

Step 1 — Create a New Project

Inside your projects folder:

projects
│
├── AI-Chatbot
├── Embedding-Demo
├── ChromaDB-Demo
│
└── RAG-Retriever

Create:

RAG-Retriever
Step 2 — Install a New Package

Go into the project folder.

cd projects
mkdir RAG-Retriever
cd RAG-Retriever

Install:

pip install sentence-transformers

Then update:

pip freeze > requirements.txt
Step 3 — Create app.py

Start with:

from sentence_transformers import SentenceTransformer
Step 4 — Load the Embedding Model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

Does this look familiar?

It should.

You've already used exactly this model in Module 5.

Step 5 — Generate an Embedding
text = "Python is a programming language."

embedding = model.encode(text)

print(len(embedding))

Output:

384

This confirms the model generates a 384-dimensional vector.

🧠 Why are we doing this again?

In Module 5, we generated embeddings to understand how they work.

Now we're preparing to plug that embedding model into ChromaDB instead of relying on its default behavior.

This gives us:

Our Documents
      │
Our Embedding Model
      │
ChromaDB

instead of:

Our Documents
      │
Unknown Default Model
      │
ChromaDB
Visual Comparison
Before
Python Document
       │
       ▼
Default ChromaDB Model
       │
       ▼
Embedding
       │
       ▼
Vector Database
After
Python Document
       │
       ▼
SentenceTransformer
(all-MiniLM-L6-v2)
       │
       ▼
Embedding
       │
       ▼
ChromaDB

Now you control the embedding pipeline.

💡 Why does this matter for RAG?

Remember your friend's project?

pdf_loader.py
chunking.py
embeddings.py
vector_store.py
retriever.py
rag_chain.py

Notice something?

There's a separate file called:

embeddings.py

Why?

Because production projects don't let ChromaDB decide the embedding model.

They generate embeddings themselves and then store those vectors.

You're about to learn that exact architecture.

🎯 Mini Assignment

Create the new RAG-Retriever folder and complete these steps:

Install sentence-transformers.
Create app.py.
Load all-MiniLM-L6-v2.
Encode:
Python is a programming language.
Print:
print(len(embedding))

You should see:

384
🚀 Next Lesson (One of the Most Important in the Entire Bootcamp)

We'll connect:

SentenceTransformer
        │
        ▼
Generate Embeddings
        │
        ▼
Store Those Embeddings
        │
        ▼
ChromaDB

instead of letting ChromaDB generate them automatically.

🎯 A Small Change in Teaching Pace

From this point onward, I'm going to increase the pace slightly because you've demonstrated that you understand:

✅ Embeddings
✅ Cosine Similarity
✅ Vector Databases
✅ ChromaDB CRUD
✅ Semantic Search

These are the foundations. The next modules (RAG, LangChain, LangGraph, and AI Agents) build directly on them, and we'll spend more time on architecture and real-world implementation than on basic syntax. By the end of this bootcamp, you'll not only understand your friend's project—you'll be able to build an improved version of it yourself. 🚀

Module 6 – Lesson 10 (One of the Most Important in the Entire Bootcamp)

This lesson is where everything you've learned over the last several modules comes together.

Until today, ChromaDB was doing this:

Document
   │
   ▼
ChromaDB
(Default Embedding)
   │
   ▼
Vector Database

Today, you will generate the embeddings and store them yourself.

This is how almost every production RAG system works.

Goal

Instead of:

collection.add(
    documents=[...]
)

We'll do:

Document
     │
     ▼
SentenceTransformer
     │
     ▼
384-D Vector
     │
     ▼
collection.add(
    embeddings=[...]
)

This is the first time you'll understand why your friend's project separates:

embeddings.py
vector_store.py

They are two independent responsibilities.

Step 1 — Create a New File

Inside:

projects/RAG-Retriever/

Create:

manual_embeddings.py
Step 2 — Import Libraries
import chromadb
from sentence_transformers import SentenceTransformer
Step 3 — Load the Embedding Model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
Step 4 — Connect to ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)
Step 5 — Create a Fresh Collection
try:
    client.delete_collection("manual_vectors")
except Exception:
    pass

collection = client.get_or_create_collection(
    name="manual_vectors"
)
Step 6 — Create Documents
documents = [
    "Python is used for AI.",
    "Java is used for enterprise applications.",
    "Docker packages applications into containers."
]
Step 7 — Generate Embeddings Yourself

This is the key difference.

embeddings = model.encode(documents)

Now print:

print(type(embeddings))
print(len(embeddings))
print(len(embeddings[0]))

Expected output:

<class 'numpy.ndarray'>

3

384

You've just created three embedding vectors yourself.

📌 Stop Here

Don't add them to ChromaDB yet.

I want you to inspect the embeddings variable and understand what it contains.

In the next lesson, we'll take those vectors and store them manually using:

collection.add(
    embeddings=embeddings.tolist(),
    ...
)

When you complete that, you'll fully understand why production projects have separate embeddings.py and vector_store.py files, and you'll be ready to move into the RAG module where these pieces come together into a complete document question-answering system.