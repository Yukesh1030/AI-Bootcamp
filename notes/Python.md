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



