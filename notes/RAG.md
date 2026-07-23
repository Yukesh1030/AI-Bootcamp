Retrieval Augmented Generation (RAG)
⭐ Lesson 1 – What is RAG?

This is probably the most important concept in modern AI engineering.

First, let's understand the problem.

Imagine you ask ChatGPT:

Who is Yukesh G?

It doesn't know unless you tell it.

Or ask:

What is inside my company policy PDF?

Again, it doesn't know.

Why?

Because the model was trained before your PDF even existed.

Problem with an LLM
                 LLM

        Knowledge until Training

               │
               ▼

     ❌ Doesn't know your PDF

     ❌ Doesn't know today's documents

     ❌ Doesn't know company data

     ❌ Doesn't know private files

An LLM cannot magically read your files.

Traditional Solution

People used to do this:

PDF

↓

Copy everything

↓

Paste into ChatGPT

↓

Ask Question

Problems:

PDF may have 500 pages.
Token limits.
Repeating the same upload every time.
Slow and expensive.
RAG Solution

Instead of sending the whole document...

Send only the relevant part.

PDF

↓

Chunking

↓

Embeddings

↓

Vector Database

↓

User Question

↓

Semantic Search

↓

Relevant Chunks

↓

LLM

↓

Answer

This is RAG.

What does RAG mean?

R = Retrieval

Retrieve relevant information.

A = Augmented

Augment (add) that information to the prompt.

G = Generation

Generate the final answer.

Example

Suppose your PDF contains:

Page 1
Company History

Page 2
Leave Policy

Page 3
Travel Policy

Page 4
Salary Policy

Page 5
Health Insurance

User asks:

How many casual leaves do employees get?

Should we send all 5 pages?

No.

Instead:

User Question

↓

Vector Search

↓

Page 2 (Leave Policy)

↓

LLM

↓

Answer

The LLM only receives the relevant chunk.

Internal Pipeline
                 PDF

                  │

          PDF Loader

                  │

             Chunking

                  │

            Embeddings

                  │

             ChromaDB

                  │

          Semantic Search

                  │

         Relevant Chunks

                  │

           Prompt Builder

                  │

                LLM

                  │

             Final Answer
Where does each file fit?

Remember your friend's project?

src

pdf_loader.py

chunking.py

embeddings.py

vector_store.py

retriever.py

rag_chain.py

Now map them:

pdf_loader.py
      │
      ▼
Reads PDF

-----------------------

chunking.py
      │
      ▼
Splits PDF into chunks

-----------------------

embeddings.py
      │
      ▼
Converts chunks into vectors

-----------------------

vector_store.py
      │
      ▼
Stores vectors in ChromaDB

-----------------------

retriever.py
      │
      ▼
Finds relevant chunks

-----------------------

rag_chain.py
      │
      ▼
Sends retrieved chunks to the LLM

For the first time, those filenames should make sense.

Why not fine-tune the LLM?

Suppose your company updates its leave policy today.

Without RAG:

Change PDF

↓

Fine-tune LLM again

↓

Expensive

↓

Slow

With RAG:

Change PDF

↓

Update ChromaDB

↓

Done ✅

No retraining needed.

Real Companies Using RAG

Almost every enterprise AI assistant uses this architecture.

Examples:

Internal company chatbots
HR assistants
Customer support bots
Legal document search
Medical document assistants
Banking knowledge assistants

The LLM provides language understanding, while the vector database provides up-to-date knowledge.

Interview Question ⭐⭐⭐⭐⭐
What is RAG?

Professional Answer:

Retrieval-Augmented Generation (RAG) is an AI architecture where relevant information is retrieved from an external knowledge base using semantic search and provided as additional context to an LLM before it generates a response. This enables accurate, up-to-date, and domain-specific answers without retraining the model.

Mini Assignment (Theory)

Answer these questions:

Q1

Why don't we send the entire PDF to the LLM?

Q2

What is the job of ChromaDB in RAG?

Q3

Why is RAG preferred over fine-tuning for frequently changing documents?

🚀 Next Lesson (Module 7 – Lesson 2)

We'll start building a real RAG project from scratch.

We'll create this folder structure:

RAG-Project
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── data/
│   └── sample.pdf
│
├── src/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_chain.py
│
└── prompts/
    └── prompt_template.py

You might notice something familiar: this is almost identical to your friend's project. That's intentional. Instead of just explaining the architecture, we'll build it file by file so that by the end of Module 7 you'll understand exactly what every component does and why it's there.

Excellent, Yukesh! 🔥

Now we stop learning individual concepts and start building a real production-level RAG application.

This is exactly how a GenAI developer would structure a project in a company.

🎓 AI Developer Bootcamp
Module 7 – Retrieval-Augmented Generation (RAG)
⭐ Lesson 2 – Project Setup & Architecture

Today we'll create the foundation of our RAG application.

🎯 Goal

By the end of today's lesson, you'll have:

✅ A professional folder structure
✅ Virtual environment
✅ Required packages installed
✅ .env configuration
✅ A sample PDF ready
✅ A project that can grow into a production RAG system
🧠 First Understand the Big Picture

We're going to build this:

                 USER

                   │

                   ▼

          Ask Question

                   │

                   ▼

             Retriever

                   │

                   ▼

            ChromaDB

                   ▲

             Embeddings

                   ▲

              Chunking

                   ▲

             PDF Loader

                   ▲

                PDF

                   │

                   ▼

            Relevant Context

                   │

                   ▼

              Groq/OpenAI

                   │

                   ▼

              Final Answer

Every folder we create today represents one step in this pipeline.

Step 1 – Create a New Project

Inside your existing structure:

AI-BOOTCAMP/

projects/

    AI-Chatbot/

    Embedding-Demo/

    ChromaDB-Demo/

    RAG-Retriever/

    RAG-Project ⭐

Create:

RAG-Project
Step 2 – Open Terminal

Navigate to the project.

cd projects
cd RAG-Project

Check your path.

It should look similar to:

(venv)

E:\learn\GenAI\AI-BOOTCAMP\projects\RAG-Project>
Step 3 – Folder Structure

Create these folders manually in VS Code.

RAG-Project

│

├── data

├── src

├── prompts

├── chroma_db

├── app.py

├── config.py

├── .env

├── requirements.txt

└── README.md
Why each folder?
📁 data

Stores

PDFs

Word Files

Text Files

Example

data/

company_policy.pdf

python_notes.pdf

docker_book.pdf
📁 src

Contains all source code.

src/

pdf_loader.py

chunking.py

embeddings.py

vector_store.py

retriever.py

rag_chain.py

Exactly like your friend's project.

📁 prompts

Stores prompt templates.

Later

Instead of writing

prompt = """
You are a helpful AI assistant...
"""

inside Python,

we'll keep prompts separately.

Much cleaner.

📁 chroma_db

Stores

SQLite Database

Embeddings

Collections

Exactly what you learned in Module 6.

Step 4 – Install Packages

Run

pip install chromadb

Next

pip install sentence-transformers

Next

pip install pypdf

Next

pip install python-dotenv

Next

pip install openai

Finally

pip freeze > requirements.txt
Why these packages?
ChromaDB
Store vectors
Sentence Transformers
Generate embeddings
PyPDF
Read PDF files
python-dotenv
Load API keys securely
OpenAI SDK

Used with

Groq

OpenAI

OpenRouter

because they expose an OpenAI-compatible API.

Step 5 – Create .env

Inside

RAG-Project

Create

.env

Write

GROQ_API_KEY=your_api_key_here

MODEL_NAME=llama-3.3-70b-versatile

Don't hardcode your API key in Python.

Why use .env?

❌ Bad

api_key="gsk_xxxxxxxxxxxxxxxxx"

If you upload your project to GitHub,

everyone can see your key.

✅ Good

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")

Safe.

Professional.

Step 6 – Create config.py
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv("MODEL_NAME")
Why config.py?

Instead of

load_dotenv()

inside

every file,

we load configuration once.

Then import it anywhere.

Example

from config import GROQ_API_KEY

Much cleaner.

Step 7 – Create Empty Source Files

Inside

src/

create

pdf_loader.py

chunking.py

embeddings.py

vector_store.py

retriever.py

rag_chain.py

Leave them empty for now.

We'll implement them one by one.

Step 8 – Add a PDF

Inside

data/

put

sample.pdf

Don't worry about its content.

Any small PDF is fine.

We'll use it in the next lesson.

Final Folder Structure
RAG-Project

│

├── data
│     └── sample.pdf

├── src
│     ├── pdf_loader.py
│     ├── chunking.py
│     ├── embeddings.py
│     ├── vector_store.py
│     ├── retriever.py
│     └── rag_chain.py

├── prompts

├── chroma_db

├── app.py

├── config.py

├── .env

├── requirements.txt

└── README.md
🧠 Architecture Mapping

Now you can finally map every file to its responsibility.

sample.pdf
      │
      ▼
pdf_loader.py
      │
      ▼
chunking.py
      │
      ▼
embeddings.py
      │
      ▼
vector_store.py
      │
      ▼
retriever.py
      │
      ▼
rag_chain.py
      │
      ▼
Groq LLM
      │
      ▼
Final Answer

Each file has one responsibility, making the project easier to maintain and extend.

Interview Question ⭐⭐⭐⭐⭐
Why do we split a RAG project into multiple files?

Professional Answer:

A modular RAG project separates responsibilities such as PDF loading, chunking, embedding generation, vector storage, retrieval, and LLM interaction. This improves maintainability, reusability, testing, and scalability, making the system easier to extend and debug.

🎯 Mini Assignment

Before moving to Lesson 3:

✅ Create the RAG-Project folder.
✅ Create the complete folder structure.
✅ Install all required packages.
✅ Create the .env and config.py.
✅ Add any small PDF as data/sample.pdf.
✅ Create the empty source files under src/.
🚀 Next Lesson (Module 7 – Lesson 3)

We'll implement the first real component:

pdf_loader.py

You'll learn:

How PDFs are read programmatically.
Why PDFs can't be sent directly to an LLM.
How to extract text page by page.
How to prepare the extracted text for chunking.

At the end of Lesson 3, your application will be able to open a PDF and extract its contents automatically—the first real step in a production RAG pipeline.


Until now we've manually written:

documents = [
    "Python is a programming language",
    "Java is an OOP language"
]

Real companies don't do this.

Instead they have

PDFs
Word files
Excel files
Websites
Database records

The first step is always:

Document
     │
     ▼
Read Text

That's today's lesson.

🎓 AI Developer Bootcamp
Module 7 — Lesson 3
Building pdf_loader.py
🎯 Goal

By the end of this lesson you'll understand

Why PDFs must be loaded first
How PyPDF works
How pages are extracted
How to return text for chunking
First Understand the Pipeline

Suppose your company uploads

Employee_Handbook.pdf

Can the LLM directly read

Employee_Handbook.pdf

No.

The LLM understands

TEXT

not PDF files.

So we must convert

PDF

↓

Plain Text

↓

Chunking
Visual
sample.pdf

↓

pdf_loader.py

↓

Plain Text

↓

chunking.py
Step 1

Open

src/

↓

pdf_loader.py
Step 2

Import PyPDF

from pypdf import PdfReader

Question

Why not

import pypdf

Because we only need

PdfReader
What is PdfReader?

Think of it like

open("sample.txt")

For text files.

For PDFs,

PdfReader()

opens the PDF.

Step 3

Create a function

from pypdf import PdfReader

def load_pdf(file_path):

Question

Why a function?

Because later

load_pdf("company.pdf")

load_pdf("resume.pdf")

load_pdf("book.pdf")

The same function can read any PDF.

Step 4

Open the PDF

reader = PdfReader(file_path)

Think

sample.pdf

↓

PdfReader

↓

Reader Object
What is inside reader?

It contains

reader

│

├── metadata

├── pages

└── attachments

Today we only need

pages
Step 5

Create an empty string

text = ""

Why?

Because every page will be added to this variable.

Imagine

Page 1

↓

text

then

Page 2

↓

text

Finally

All Pages

↓

One String
Step 6

Loop through pages

for page in reader.pages:

Question

What is

reader.pages

Suppose

PDF

Page 1

Page 2

Page 3

Then

reader.pages

acts like

[
Page1,

Page2,

Page3
]

So

for page in reader.pages:

means

Take

Page 1

↓

Page 2

↓

Page 3

one by one.

Step 7

Extract text

text += page.extract_text()

This is the most important line.

Let's understand it.

Suppose

Page 1 contains

Python

After first iteration

text = "Python"

Page 2 contains

Java

Now

text += "Java"

becomes

PythonJava

Better version

text += page.extract_text() + "\n"

Now

Python

Java

Much cleaner.

Step 8

Return the text

return text

Now the function returns

Entire PDF

instead of

PDF Object
Complete Code
from pypdf import PdfReader

def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text() + "\n"

    return text
Step 9

Open

app.py

Import

from src.pdf_loader import load_pdf

Call the function

text = load_pdf("data/sample.pdf")

Print

print(text)
Complete app.py
from src.pdf_loader import load_pdf

text = load_pdf("data/sample.pdf")

print(text)
What Happens Internally?
sample.pdf

↓

PdfReader

↓

Page 1

↓

Extract Text

↓

Page 2

↓

Extract Text

↓

Page 3

↓

Extract Text

↓

One Large String

↓

app.py
Output Example

Suppose

sample.pdf contains

Python

Java

Docker

Output

Python

Java

Docker

Congratulations.

Your RAG application can now read PDFs.

Why Not Send This Directly to the LLM?

Suppose your PDF has

500 Pages

This becomes

300,000 Characters

Too large.

LLMs have context limits.

So next lesson we'll split it into small pieces.

This process is called

Chunking
Interview Questions ⭐⭐⭐⭐⭐
Q1. Why do we need a PDF loader in RAG?

Professional Answer:

A PDF loader extracts readable text from PDF documents. Since LLMs cannot process PDF files directly, the extracted text is used for chunking, embedding generation, and retrieval.

Q2. What does PdfReader do?

Professional Answer:

PdfReader opens a PDF document and provides access to its pages, metadata, and other information. It allows us to extract text from each page programmatically.

🎯 Mini Assignment

Use your own PDF.

For example,

AI Notes.pdf

or

Python.pdf

Change

load_pdf("data/sample.pdf")

to your PDF.

Run it.

Check whether all pages are printed correctly.

🏆 Current Pipeline

You've now completed:

PDF
 │
 ▼
pdf_loader.py ✅
 │
 ▼
Plain Text
 │
 ▼
Chunking ❌
 │
 ▼
Embeddings ❌
 │
 ▼
ChromaDB ❌
 │
 ▼
Retriever ❌
 │
 ▼
LLM ❌
🚀 Next Lesson (Lesson 4 – Chunking)

This is where you'll understand why everyone talks about "chunks" in RAG.

We'll answer questions like:

Why not embed the whole PDF?
What is a chunk?
What is chunk overlap?
How do we choose chunk size?
Why does poor chunking lead to poor AI answers?

By the end of that lesson, you'll build a reusable chunking.py module that prepares documents for embedding—the same approach used in production frameworks like LangChain and LlamaIndex.


This lesson is one of the most important lessons in the entire RAG pipeline.

Many beginners think RAG means:

PDF
 ↓
Embedding
 ↓
LLM

❌ This is wrong.

The correct pipeline is:

PDF
 ↓
Chunking ⭐⭐⭐⭐⭐
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
LLM

If your chunking is poor, even GPT-5 or Claude or Gemini won't give good answers because they only answer based on the retrieved chunks.

🎓 AI Developer Bootcamp
Module 7 – Lesson 4
📚 Chunking
🎯 Lesson Goal

By the end of this lesson you'll understand:

✅ What is a Chunk?
✅ Why Chunking is needed
✅ Chunk Size
✅ Chunk Overlap
✅ How to build your own chunker
✅ How companies chunk documents
First Question

Suppose your PDF contains

Page 1

Python is a programming language.

It is easy to learn.

It supports AI.

It supports Data Science.

It supports Automation.

It supports Web Development.

...500 Pages...

Question:

Should we generate ONE embedding for all 500 pages?

Answer

❌ No.

Why?

Because an embedding represents one semantic meaning.

If we embed the entire PDF:

Python

Java

Docker

AWS

Kubernetes

Linux

React

HR Policy

Leave Policy

Finance

...

One vector tries to represent everything.

That vector becomes too general.

Real Life Example

Imagine a book.

1000 Pages

You ask:

"What is Docker?"

Should AI search all 1000 pages?

No.

Instead

Book

↓

Page 245

↓

Docker Chapter

↓

Answer
Solution

Split the document.

This is called

⭐ Chunking

Visual

PDF

↓

Chunk 1

↓

Chunk 2

↓

Chunk 3

↓

Chunk 4

Each chunk gets

its own embedding.

Example

Suppose the PDF says

Python is easy.

Python supports AI.

Java is object oriented.

Docker packages applications.

AWS provides cloud services.

Instead of one document

we create

Chunk 1

Python is easy.

Python supports AI.

--------------------

Chunk 2

Java is object oriented.

--------------------

Chunk 3

Docker packages applications.

AWS provides cloud services.

Now

each chunk

↓

One embedding.

Why is this better?

User asks

"What is Docker?"

ChromaDB compares against

Chunk 1

Python

❌

------------

Chunk 2

Java

❌

------------

Chunk 3

Docker

✅

Retrieval becomes much more accurate.

What is Chunk Size?

Question.

How big should a chunk be?

Suppose

1000 characters

Should we split every

5 characters

?

Example

Pytho

n is

a pro

gramm

ing

Impossible.

Meaning is destroyed.

Should we split every

50000 characters

?

Again

No.

Too much information.

Companies choose something like

500 Characters

1000 Characters

1500 Characters

depending on the use case.

Visual

Small Chunk

Python is easy.

Good for

Precise retrieval.

Huge Chunk

Entire Chapter

Good for

Context

Bad for retrieval.

What is Chunk Overlap?

One of the most important concepts.

Suppose

Chunk size

100 characters

Document

Python is a programming language.

It is widely used in AI.

It is also used in Web Development.

Without overlap

Chunk 1

Python is a programming language.

-----------------

Chunk 2

It is widely used in AI.

-----------------

Chunk 3

It is also used in Web Development.

Notice

Chunk 2 starts with

It

Question

Who is

"It"?

Python?

Java?

Docker?

Meaning is lost.

Solution

Overlap.

Example

Chunk 1

Python is a programming language.

---------------------

Chunk 2

programming language.

It is widely used in AI.

---------------------

Chunk 3

widely used in AI.

It is also used in Web Development.

Now

every chunk remembers

some previous context.

Visual

Without overlap

AAAA BBBB

CCCC DDDD

EEEE FFFF

Meaning breaks.

With overlap

AAAA BBBB

BBBB CCCC

CCCC DDDD

DDDD EEEE

Much better.

Step 1

Open

src/

↓

chunking.py
Step 2

Create

def chunk_text(text,
               chunk_size=500):

Question

Why a function?

Because later

chunk_text(pdf)

chunk_text(book)

chunk_text(notes)

Everything uses the same logic.

Step 3

Create an empty list

chunks = []

This will store

all chunks.

Step 4

Loop

for i in range(
    0,
    len(text),
    chunk_size
):

Let's understand.

Suppose

Text

1000 Characters

Chunk size

200

Python generates

0

200

400

600

800

Exactly what we need.

Step 5

Slice

chunk = text[
    i:i+chunk_size
]

Suppose

chunk_size=10

Text

ABCDEFGHIJKLMN

Iteration 1

A B C D E F G H I J

Iteration 2

K L M N

Simple slicing.

Step 6

Append

chunks.append(chunk)

Now

chunks

↓

[
Chunk1,

Chunk2,

Chunk3
]
Step 7

Return

return chunks
Complete Code
def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i+chunk_size]

        chunks.append(chunk)

    return chunks
Step 8

Open

app.py

Import

from src.chunking import chunk_text

After

text = load_pdf(
    "data/sample.pdf"
)

write

chunks = chunk_text(
    text,
    chunk_size=500
)

Print

print(len(chunks))

Then

for index, chunk in enumerate(chunks):

    print("=" * 50)

    print(f"Chunk {index+1}")

    print(chunk)
Output
Chunk 1

Python...

----------------

Chunk 2

Java...

----------------

Chunk 3

Docker...

Congratulations.

You have officially built

a document chunker.

Why Our Chunker Is Still Simple

The chunker you built works, but it has a limitation.

Imagine this sentence:

Artificial Intelligence is transforming healthcare and finance.

If the character limit falls in the middle:

Artificial Intelligence is trans

forming healthcare and finance.

The sentence gets broken, making retrieval less effective.

Production systems avoid this by splitting at sentence or paragraph boundaries and by adding overlap.

We'll improve our chunker in later lessons.

Interview Questions ⭐⭐⭐⭐⭐
Q1. What is chunking?

Professional Answer:

Chunking is the process of dividing a large document into smaller, meaningful pieces before generating embeddings. This improves semantic retrieval accuracy and ensures that relevant context is returned during RAG.

Q2. Why don't we embed the entire PDF?

Professional Answer:

Embedding an entire PDF creates a single vector representing many different topics, which reduces retrieval quality. Smaller chunks preserve semantic meaning and allow more precise searches.

Q3. What is chunk overlap?

Professional Answer:

Chunk overlap is the practice of repeating a portion of the previous chunk in the next chunk. It preserves context across chunk boundaries and improves retrieval quality.

🧠 Industry Insight

Our manual chunker helps you understand the concept, but production systems rarely implement chunking from scratch.

Frameworks like LangChain provide text splitters such as RecursiveCharacterTextSplitter, which preserve sentence boundaries and support configurable chunk sizes and overlaps. You'll learn those after you've mastered the underlying logic.

🎯 Assignment
Implement chunk_text() exactly as shown.
Load your sample.pdf.
Print:
Total number of chunks.
Every chunk.
Experiment with:
chunk_size=200
chunk_size=500
chunk_size=1000

Observe how the number of chunks changes and think about the trade-off between retrieval precision and context.

🚀 Next Lesson (Lesson 5 – Smarter Chunking with Overlap)

We'll upgrade your chunker to support:

chunk_text(
    text,
    chunk_size=500,
    overlap=100
)

This is the approach used in production RAG systems because it preserves context across chunk boundaries and significantly improves retrieval quality. After that, we'll connect those chunks to your embedding model and begin building the complete ingestion pipeline.


