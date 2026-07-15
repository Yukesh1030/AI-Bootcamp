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



AI Developer Bootcamp
Module 3 – Lesson 9
⭐ Why We Can't Keep Sending the Entire Chat Forever?

This is one of the most important engineering problems in GenAI.

Imagine This Conversation
You : Hi

AI : Hello!

You : My name is Yukesh.

AI : Nice to meet you.

You : Explain Python.

AI : ...

You : Explain Django.

AI : ...

...

Suppose after 1000 questions your messages list looks like:

messages = [
    ...
    2000 messages
]

Question:

Every time you ask a new question...

Do we send all 2000 messages?

Yes, if we don't optimize.

Visualize It

Current Request

Question 1
↓

Question 2
↓

Question 3
↓

...

↓

Question 2000
↓

New Question

Every API call sends everything.

Problem 1 — Token Cost 💰

Suppose:

Each message ≈ 100 tokens

Conversation:

2000 Messages

×

100 Tokens

=

200,000 Tokens

Imagine you're paying per token.

You're paying for the same old messages over and over again.

Problem 2 — Context Window

Suppose your model supports

128,000 Tokens

Your conversation becomes

200,000 Tokens

What happens?

Conversation

↓

200K Tokens

↓

Model supports

↓

128K Tokens

↓

❌ Doesn't fit

The model literally cannot read everything.

Problem 3 — Speed

Imagine sending

5 KB

versus

5 MB

Which is faster?

Obviously

5 KB

Larger requests mean:

More network traffic
More processing
Higher latency
So...

How does ChatGPT talk to me for hours?

Great question.

It doesn't keep every message forever.

Instead, it uses smart memory strategies.

Strategy 1 — Sliding Window

Imagine this conversation:

Q1

Q2

Q3

Q4

Q5

Q6

Q7

Instead of sending everything:

The application sends only the most recent messages.

Example:

Q5

Q6

Q7

Older messages are dropped.

Visual
Old

↓

Q1

Q2

Q3

Q4

──────────────

Recent

↓

Q5

Q6

Q7

Only the recent window is sent.

This is called a Sliding Window.

Strategy 2 — Conversation Summary

Imagine this conversation:

100 Messages

Instead of sending all 100 messages:

The application creates a summary.

Example:

Summary:

User is Yukesh.

Learning AI.

Completed Python.

Interested in RAG.

Now instead of 100 messages:

We send

Summary

+

Recent Messages

This reduces token usage dramatically.

Strategy 3 — Long-Term Memory

Imagine you tell the AI:

My name is Yukesh.

I work as a Frontend Developer.

I'm learning AI.

Months later...

You ask:

What is my learning goal?

How does the AI know?

Not because it kept every conversation.

Instead:

Important Information

↓

Stored Separately

↓

Retrieved When Needed

This is long-term memory, managed by the application.

Strategy 4 — RAG

Suppose your chatbot has access to:

500 PDFs

Does it send all 500 PDFs every time?

No.

Instead:

Question

↓

Embedding

↓

Vector Database

↓

Cosine Similarity

↓

Top 5 Chunks

↓

LLM

Sound familiar?

We've already learned every concept in this pipeline.

Complete Production Architecture
User Question
        │
        ▼
Conversation History
        │
        ▼
Sliding Window
        │
        ▼
Conversation Summary
        │
        ▼
Relevant Memories
        │
        ▼
RAG Retrieval
        │
        ▼
Final Prompt
        │
        ▼
LLM
        │
        ▼
Answer

This is very close to how modern AI assistants are built.

Let's Build This in Our Chatbot

Right now our chatbot sends:

messages

which keeps growing forever.

We can improve it.

Example

Suppose we keep only the last 6 messages.

Conceptually:

if len(messages) > 7:
    messages = [messages[0]] + messages[-6:]

Let's understand this.

messages[0]

Always keeps the system prompt.

System

↓

You are a helpful AI tutor.

We never remove it.

messages[-6:]

Take only the last 6 messages.

If the conversation is:

System

Q1

A1

Q2

A2

Q3

A3

Q4

A4

After trimming:

System

Q2

A2

Q3

A3

Q4

A4

The oldest conversation is removed.

Why Keep the System Prompt?

If we remove it...

The AI forgets its role.

Imagine the system prompt is:

You are an HR interviewer.

If you delete it...

The AI may stop behaving like an interviewer.

Interview Question ⭐⭐⭐⭐⭐
Why do AI applications trim conversation history?

Professional Answer

AI applications trim conversation history to stay within the model's context window, reduce token costs, improve response speed, and maintain relevant conversational context.

Assignment

Modify your chatbot so that:

The system message is never removed.
Only the last 6 conversation messages are kept.
Print the total number of messages after each response:
print(f"Messages Stored: {len(messages)}")

Watch how the count grows and then stabilizes after trimming.

🧠 Mentor Tip

Everything you've learned so far forms the foundation of real AI systems.

The next few lessons are where you'll start building features that companies actually use.

🚀 Next Lesson (One of the Most Exciting)
Streaming Responses

Right now your chatbot behaves like this:

You: Explain AI

(wait 3 seconds...)

AI:
Artificial Intelligence is...

But ChatGPT behaves like this:

AI:
Artific...
Artificial...
Artificial Intelligence...

Letter by letter.

Word by word.

In the next lesson, you'll build streaming responses using the API, just like ChatGPT, Gemini, Claude, and Cursor. You'll learn how streaming works under the hood and implement it yourself step by step. This is a feature that immediately makes your chatbot feel much more professional.

🎓 AI Developer Bootcamp
Module 3 – Lesson 10
⭐ Streaming Responses (Like ChatGPT)
🎯 Today's Goal

Right now your chatbot behaves like this:

You : What is AI?

(wait 2–3 seconds)

AI :
Artificial Intelligence (AI) is...

But ChatGPT behaves like this:

You : What is AI?

AI :
A...
Ar...
Art...
Artif...
Artificial...
Artificial Intelligence...

How does it do that?

Let's learn.

First Question
Does ChatGPT Generate the Entire Answer First?

Most beginners think:

LLM

↓

Creates Full Answer

↓

Sends It

❌ Wrong.

What Actually Happens

The LLM predicts one token at a time.

Remember our Token lesson?

Example:

Question

What is AI?

The model predicts

Token 1

Artificial

↓

Token 2

Intelligence

↓

Token 3

is

↓

Token 4

a

↓

Token 5

field

↓

...

The answer is built token by token.

Without Streaming

The API waits until all tokens are generated.

LLM

↓

Token1

↓

Token2

↓

Token3

↓

Token4

↓

Done

↓

Send Entire Answer

That's what your chatbot currently does.

With Streaming

The API sends each token immediately.

LLM

↓

Token1

↓

Send

↓

Token2

↓

Send

↓

Token3

↓

Send

↓

Token4

↓

Send

Exactly like ChatGPT.

Why Streaming?

Imagine an answer that takes

20 seconds.

Without Streaming

20 Seconds

↓

Nothing

↓

Whole Answer

Looks like the app is frozen.

With Streaming

1 sec

↓

Artificial

↓

2 sec

↓

Artificial Intelligence

↓

3 sec

↓

Artificial Intelligence is...

The user sees progress immediately.

How Does the API Know?

When we make the request, we tell it:

stream=True

That one parameter changes how the server sends data.

Current Code

Right now you have:

response = client.chat.completions.create(
    model=model_name,
    messages=messages
)
Step 1

Add

stream=True

Like this:

response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    stream=True
)

Question:

What changes?

Instead of getting one response,

you receive a stream.

Think of it like YouTube.

A video isn't downloaded completely before it starts playing.

It streams.

Same idea.

Step 2

Can we print the response like before?

print(response.choices[0].message.content)

❌ No.

Why?

Because

response

is no longer a single object.

It is an iterator (a stream of chunks).

What is an Iterator?

Think of it as a delivery person bringing one package at a time.

Instead of:

📦📦📦📦📦

You receive:

📦

↓

📦

↓

📦

↓

📦

One after another.

Step 3

We need a loop.

for chunk in response:

This means:

"Keep reading each chunk until the stream ends."

Visual
Chunk 1

↓

Chunk 2

↓

Chunk 3

↓

Chunk 4

Python reads each one.

Step 4

Inside each chunk

The new token is stored in:

chunk.choices[0].delta.content

Notice

Previously

response.choices[0].message.content

Now

chunk.choices[0].delta.content

Because we're receiving partial updates.

Step 5

Sometimes

delta.content

is None.

So check first:

if chunk.choices[0].delta.content:

This avoids printing empty values.

Step 6

Print without a newline

print(chunk.choices[0].delta.content, end="", flush=True)

Let's understand this.

end=""

Normally

print("Hello")
print("World")

Output

Hello
World

But

print("Hello", end="")
print("World")

Output

HelloWorld

Streaming needs continuous output.

flush=True

Normally Python buffers output.

With

flush=True

It immediately displays each token.

Without it,

you may not see the typing effect.

Step 7

After the loop finishes

Print one newline.

print()

So the next prompt starts on a new line.

Complete Streaming Code

Replace your response printing section with:

response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    stream=True
)

print("\nAI : ", end="")

full_response = ""

for chunk in response:

    if chunk.choices[0].delta.content:

        token = chunk.choices[0].delta.content

        full_response += token

        print(token, end="", flush=True)

print()
Wait...

Why full_response?

Great question.

During streaming we receive

Artificial

↓

Intelligence

↓

is

↓

...

If we don't join them,

we cannot save the assistant reply into messages.

So we build:

full_response += token

At the end

full_response

contains

Artificial Intelligence is...
Final Step

Save the assistant reply.

messages.append(
    {
        "role":"assistant",
        "content":full_response
    }
)

Now your chatbot remembers both:

User messages
Assistant replies
Visual Flow
User Question

↓

Append User

↓

Send Messages

↓

Stream Tokens

↓

Join Tokens

↓

Append Assistant

↓

Next Question
Interview Question ⭐⭐⭐⭐⭐
What is streaming in LLMs?

Professional Answer

Streaming is the process of receiving generated tokens incrementally from the language model instead of waiting for the complete response. It improves perceived responsiveness and user experience.

