Q1. What is an API Key?

Answer

An API Key is a unique credential used to authenticate and authorize an application when accessing an API.
Q2. Why do we use a .env file?

Answer

A .env file stores sensitive configuration values such as API keys and model names outside the source code, improving security and maintainability.

Q3. Why should .env be added to .gitignore?

Answer

Because it contains sensitive credentials. Uploading it to GitHub could expose API keys and allow unauthorized access.

Q4. What happens if the API key is invalid?

Answer

The API rejects the request and typically returns:

401 Unauthorized

Q1. Why do we call load_dotenv()?

Answer:

To load environment variables from the .env file into the application's environment so they can be accessed securely.

Q2. Why use os.getenv() instead of writing the API key directly?

Answer:

It keeps secrets out of the source code, making the application more secure and easier to configure across environments.

Q3. Why do we pass base_url?

Answer:

Because we're using the OpenAI SDK to communicate with Groq's OpenAI-compatible API endpoint instead of OpenAI's own endpoint.




🎓 AI Developer Bootcamp
Module 3 - LLM Engineering
Lesson 7
⭐ Build Your First Interactive AI Chatbot

Today, we'll upgrade your application.

Current Program:

Question (Hardcoded)
        │
        ▼
AI
        │
        ▼
Answer

Today's Program:

You
 │
 ▼
Type Anything
 │
 ▼
AI
 │
 ▼
Answer
 │
 ▼
Ask Again
 │
 ▼
AI

Congratulations...

Today you're building your first chatbot.

Before Coding

Let's think.

Current code:

content="What is Artificial Intelligence?"

Question:

Can the user change the question?

❌ No.

It is hardcoded.

We need dynamic input.

Step 1

Replace

content="What is Artificial Intelligence?"

with

user_question = input("You : ")

Question:

What does input() do?

It waits for the user to type something.

Example

You : What is Python?

Now

user_question

contains

"What is Python?"
Step 2

Pass it to the AI.

Replace

"content":"What is Artificial Intelligence?"

with

"content": user_question

Now your program becomes dynamic.

Current Flow
You

↓

Type Question

↓

Stored in user_question

↓

Sent to Groq

↓

AI Reply
Step 3

Improve the Output

Instead of

print(response.choices[0].message.content)

Write

print("\nAI :")
print(response.choices[0].message.content)

Output

You : Explain Python

AI :

Python is...

Much cleaner.

Step 4

Problem

After answering once

the program exits.

Question

Is ChatGPT like that?

No.

It keeps asking.

So...

we need a loop.

Step 5

What is a Loop?

Suppose

Ask

↓

Answer

↓

Ask

↓

Answer

↓

Ask

↓

Answer

This repeats.

Python has

while
Step 6

Create an Infinite Chat

while True:

Meaning

Keep running forever.

Inside the loop

user_question = input("You : ")

Then

send it to Groq.

Then

print the answer.

Flow

while True

↓

Ask User

↓

AI Answer

↓

Go Back

↓

Ask Again
Step 7

Exit Option

Question

How do we stop?

User types

exit

or

quit

Python

if user_question.lower() == "exit":
    break

Question

What is break?

It stops the loop.

Flow

User

↓

exit

↓

break

↓

Program Ends
Step 8

Final Code

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

model = os.getenv("MODEL_NAME")

print("=" * 50)
print("🤖 AI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_question = input("\nYou : ")

    if user_question.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    print("\nAI :")
    print(response.choices[0].message.content)
Understanding Every Line
while True

Runs forever until break.

input()

Waits for user input.

lower()

Converts

EXIT
Exit
eXiT

into

exit

so all variations work.

break

Stops the loop.

messages

Every conversation with an LLM is sent as a list of messages.

Today we only have:

[
    {
        "role":"user",
        "content":"Explain Python"
    }
]

Soon you'll learn why there are also:

system
assistant

roles.

Try These Questions

Run your chatbot and ask:

What is Machine Learning?

Then

Explain RAG.

Then

Who invented Python?

Finally

exit
What You'll Notice

Ask:

My name is Yukesh.

Then

What is my name?

The AI will probably not remember.

Why?

Because every request is independent right now.

We're only sending the latest user message.



Lesson 7
⭐ Build Your First Interactive AI Chatbot

Today, we'll upgrade your application.

Current Program:

Question (Hardcoded)
        │
        ▼
AI
        │
        ▼
Answer

Today's Program:

You
 │
 ▼
Type Anything
 │
 ▼
AI
 │
 ▼
Answer
 │
 ▼
Ask Again
 │
 ▼
AI

Congratulations...

Today you're building your first chatbot.

Before Coding

Let's think.

Current code:

content="What is Artificial Intelligence?"

Question:

Can the user change the question?

❌ No.

It is hardcoded.

We need dynamic input.

Step 1

Replace

content="What is Artificial Intelligence?"

with

user_question = input("You : ")

Question:

What does input() do?

It waits for the user to type something.

Example

You : What is Python?

Now

user_question

contains

"What is Python?"
Step 2

Pass it to the AI.

Replace

"content":"What is Artificial Intelligence?"

with

"content": user_question

Now your program becomes dynamic.

Current Flow
You

↓

Type Question

↓

Stored in user_question

↓

Sent to Groq

↓

AI Reply
Step 3

Improve the Output

Instead of

print(response.choices[0].message.content)

Write

print("\nAI :")
print(response.choices[0].message.content)

Output

You : Explain Python

AI :

Python is...

Much cleaner.

Step 4

Problem

After answering once

the program exits.

Question

Is ChatGPT like that?

No.

It keeps asking.

So...

we need a loop.

Step 5

What is a Loop?

Suppose

Ask

↓

Answer

↓

Ask

↓

Answer

↓

Ask

↓

Answer

This repeats.

Python has

while
Step 6

Create an Infinite Chat

while True:

Meaning

Keep running forever.

Inside the loop

user_question = input("You : ")

Then

send it to Groq.

Then

print the answer.

Flow

while True

↓

Ask User

↓

AI Answer

↓

Go Back

↓

Ask Again
Step 7

Exit Option

Question

How do we stop?

User types

exit

or

quit

Python

if user_question.lower() == "exit":
    break

Question

What is break?

It stops the loop.

Flow

User

↓

exit

↓

break

↓

Program Ends
Step 8

Final Code

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

model = os.getenv("MODEL_NAME")

print("=" * 50)
print("🤖 AI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_question = input("\nYou : ")

    if user_question.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    print("\nAI :")
    print(response.choices[0].message.content)
Understanding Every Line
while True

Runs forever until break.

input()

Waits for user input.

lower()

Converts

EXIT
Exit
eXiT

into

exit

so all variations work.

break

Stops the loop.

messages

Every conversation with an LLM is sent as a list of messages.

Today we only have:

[
    {
        "role":"user",
        "content":"Explain Python"
    }
]

Soon you'll learn why there are also:

system
assistant

roles.

Try These Questions

Run your chatbot and ask:

What is Machine Learning?

Then

Explain RAG.

Then

Who invented Python?

Finally

exit
What You'll Notice

Ask:

My name is Yukesh.

Then

What is my name?

The AI will probably not remember.

Why?

Because every request is independent right now.

We're only sending the latest user message.



🎓 AI Developer Bootcamp
Module 3 – LLM Engineering
Lesson 8 — Conversation Memory (The Most Important Lesson So Far)

This lesson separates a simple AI chatbot from a ChatGPT-like chatbot.

Before Coding...

Let's understand why we need memory.

Imagine this conversation.

You : My name is Yukesh.

AI : Nice to meet you!

You : What is my name?

Your chatbot replies:

I don't know your name.

Why?

Because every time you ask something...

Your code only sends this:

messages=[
    {
        "role":"user",
        "content":user_question
    }
]

Every request starts from scratch.

How ChatGPT Works

When you ask:

Hi

The request is actually:

messages=[
   {"role":"user","content":"Hi"}
]

Then you ask:

My name is Yukesh

ChatGPT doesn't send only that sentence.

Instead it sends:

messages=[
   {"role":"user","content":"Hi"},
   {"role":"assistant","content":"Hello!"},
   {"role":"user","content":"My name is Yukesh"}
]

Then you ask:

What is my name?

Now it sends

messages=[
   {"role":"user","content":"Hi"},
   {"role":"assistant","content":"Hello!"},
   {"role":"user","content":"My name is Yukesh"},
   {"role":"assistant","content":"Nice to meet you!"},
   {"role":"user","content":"What is my name?"}
]

Now the model says

Your name is Yukesh.

It remembers because you sent the previous conversation.

Biggest Beginner Misconception

Most beginners think:

"The AI remembers everything."

❌ Wrong.

The model has no memory between API calls.

It only knows what you include in the messages list.

The messages List

Think of it like a notebook.

Initially:

messages=[]

Empty notebook.

User says:

Hello

We add:

messages.append(
    {
        "role":"user",
        "content":"Hello"
    }
)

Notebook:

[
 {"role":"user","content":"Hello"}
]

AI replies:

Hi!

We also save that.

messages.append(
    {
        "role":"assistant",
        "content":"Hi!"
    }
)

Notebook becomes:

[
 {"role":"user","content":"Hello"},
 {"role":"assistant","content":"Hi!"}
]

Next question:

My name is Yukesh

Notebook:

[
 {"role":"user","content":"Hello"},
 {"role":"assistant","content":"Hi!"},
 {"role":"user","content":"My name is Yukesh"}
]

See what's happening?

We're building the conversation ourselves.

Three Roles

You'll see these three roles everywhere in AI development.

1️⃣ System
{
   "role":"system",
   "content":"You are a helpful AI tutor."
}

This defines the AI's behavior.

Think of it as instructions given before the conversation starts.

2️⃣ User
{
   "role":"user",
   "content":"Explain AI."
}

The user's message.

3️⃣ Assistant
{
   "role":"assistant",
   "content":"Artificial Intelligence is..."
}

The AI's response.

Real Conversation
messages=[
    {
        "role":"system",
        "content":"You are an AI Tutor."
    },

    {
        "role":"user",
        "content":"Hi"
    },

    {
        "role":"assistant",
        "content":"Hello!"
    },

    {
        "role":"user",
        "content":"Explain Python."
    }
]

This is exactly what modern chat applications send.

Why Save the Assistant's Reply?

Many beginners ask:

"Why store the AI's answer?"

Imagine this:

You:
Tell me a joke.

AI:

A joke...

You:

Explain the joke.

If we don't save the assistant's previous answer...

The AI won't know which joke you're referring to.

Memory Flow
User
      │
      ▼
Save User Message
      │
      ▼
Send Entire History
      │
      ▼
AI
      │
      ▼
Receive Response
      │
      ▼
Save AI Response
      │
      ▼
Wait for Next Question
Professional Chatbot Architecture
messages=[]

↓

System Message

↓

User Question

↓

AI Reply

↓

Append Reply

↓

Next Question

↓

Append Question

↓

Send Full History

↓

Repeat

This is how ChatGPT, Claude, Gemini, Grok, and most AI assistants work.

Interview Questions
Q1. Why does a chatbot need conversation history?

Answer:

Because LLMs are stateless between API calls. To maintain context, the application must send previous messages along with the latest user query.

Q2. What are the three message roles?

Answer:

system – Sets the assistant's behavior.
user – Represents the user's input.
assistant – Represents the model's previous responses.
Q3. Does the LLM remember previous API calls automatically?

Answer:

No. Each API call is independent. The application must include prior conversation history in the messages list.

🛠️ Coding Challenge (Don't Scroll Further Yet)

This time, I don't want to give you the code immediately.

Instead, I want you to think like an engineer.

Your Challenge:
Create a list named messages.
Add a system message before the loop.
When the user types a question:
Append it to messages.
Send the entire messages list to the API.
After receiving the response:
Append the assistant's reply to messages.

Try building it yourself first.

Even if it's only 60% correct, that's okay.

