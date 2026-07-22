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