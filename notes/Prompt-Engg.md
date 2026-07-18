Prompt Engineering (One of the Highest-Paid AI Skills)
Before We Start...

I want to ask you one question.

Suppose I ask ChatGPT:

Explain Python.

Output:

Python is a programming language...

Now I ask:

Explain Python like I'm a 5-year-old.

Output:

Imagine Python is like a box of LEGO blocks...

Same model.

Same knowledge.

Different answer.

Why?

Because the prompt changed.

What is a Prompt?
Beginner Definition

A prompt is the input or instruction that you provide to an AI model to guide its response.

Interview Definition ⭐⭐⭐⭐⭐

A prompt is a structured input provided to a Large Language Model that defines the task, context, constraints, and expected output, influencing how the model generates its response.

Think of the LLM as a New Employee

Imagine you hire a new employee.

You simply say:

Write something about AI.

You'll probably get a generic result.

Now imagine you say:

You are a senior AI professor.

Explain Artificial Intelligence to a first-year engineering student.

Use simple language.

Give two real-life examples.

Limit the explanation to 200 words.

You'll get a much better answer.

The employee didn't become smarter.

Your instructions became better.

The same is true for LLMs.

The Anatomy of a Good Prompt

Every professional prompt has four parts.

Role
    ↓
Task
    ↓
Context
    ↓
Constraints

Let's understand each.

1. Role

Tell the model who it should act as.

Examples:

You are a Python Instructor.

You are a Java Interviewer.

You are a Medical Doctor.

You are a Cybersecurity Expert.

This changes the style and perspective of the response.

2. Task

Tell it exactly what to do.

Examples:

Explain Python.

Summarize this article.

Translate this text.

Generate interview questions.
3. Context

Provide background information.

Example:

I already know Java.

I'm learning Python for AI development.

Explain only the differences.

Without context, the model has to guess.

4. Constraints

Specify limits.

Examples:

Use bullet points.

Maximum 100 words.

Don't use technical jargon.

Return JSON only.

These constraints make outputs more predictable and useful.

Example Comparison
❌ Weak Prompt
Tell me about Python.
✅ Strong Prompt
You are a senior Python instructor.

Explain Python to a software engineer who already knows Java.

Use simple English.

Give three practical examples.

Limit the answer to 250 words.

Which one would you expect to produce a better result?

Almost always, the second.

Why Prompt Engineering Matters

Prompt engineering affects:

Response quality
Accuracy
Consistency
Cost (fewer retries)
User experience

That's why it's a core AI engineering skill.

🧪 Your First Experiment

Open your chatbot and ask these three prompts one by one.

Prompt 1
Explain Python.
Prompt 2
You are a senior Python trainer.

Explain Python to a 10-year-old child.
Prompt 3
You are a senior Python trainer.

Explain Python to an experienced Java developer.

Compare Java and Python.

Use a table.

Include code examples.

Keep the answer under 300 words.
Your Assignment

After running all three prompts, answer these questions:

Which response was the best?
Why was it better?
Which parts of the prompt (role, task, context, constraints) had the biggest impact?

Don't just tell me "Prompt 3 is better." Explain why.


Module 4 – Prompt Engineering
Lesson 11.2 – System Prompt (The Brain of Your AI Application)
Before We Write Any Code

Let's answer one question.

Why does ChatGPT behave differently from GitHub Copilot?

ChatGPT can:

Write emails
Explain mathematics
Tell stories
Answer history questions

GitHub Copilot mainly:

Writes code
Explains code
Fixes bugs
Generates tests

Question:

Are they different LLMs?

Not necessarily.

Many AI applications use the same foundation model but give it different instructions.

Those instructions are called the System Prompt.

Think Like a Movie Actor 🎬

Imagine an actor.

Today he plays:

👨 Doctor

Tomorrow:

👮 Police Officer

Next week:

🧑‍💻 Software Engineer

Same actor.

Different role.

The script changes.

The LLM is exactly the same.

The system prompt is its script.

Three Roles in Every Conversation

You already know them.

System

↓

User

↓

Assistant

Let's understand them deeply.

1️⃣ System

The developer talks to the AI.

Example:

{
    "role":"system",
    "content":"You are a senior Python instructor."
}

The user never sees this.

This message tells the AI how to behave.

2️⃣ User

The user's request.

{
    "role":"user",
    "content":"Explain Python."
}
3️⃣ Assistant

The AI's previous answer.

{
    "role":"assistant",
    "content":"Python is..."
}
Real Conversation
messages = [

{
"role":"system",
"content":"You are a Python Tutor."
},

{
"role":"user",
"content":"Explain Lists."
},

{
"role":"assistant",
"content":"Lists are..."
},

{
"role":"user",
"content":"Give examples."
}

]

Notice something.

The system message appears only once.

But it's sent with every API request.

Why?

Suppose we remove it.

The conversation becomes

messages = [

{
"role":"user",
"content":"Explain Lists."
}

]

Now the AI doesn't know:

Should I teach?
Should I interview?
Should I summarize?
Should I answer briefly?
Should I explain deeply?

The system prompt provides that guidance.

Experiment 1

Use this system prompt:

You are a strict Python interviewer.

Never give direct answers.

Always ask follow-up questions.

Keep responses under 100 words.

Then ask:

What is a list in Python?

Notice how the behavior changes.

Experiment 2

Change only the system prompt:

You are a friendly teacher.

Explain everything using simple English.

Give real-life examples.

Encourage the student.

Ask the same question.

What is a list in Python?

Same model.

Completely different behavior.

Experiment 3

System Prompt

You are a senior Java interviewer.

Answer only with interview questions.

Never explain the answers.

User

Teach me Java.

What happens?

The AI starts asking questions instead of teaching.

Where Is the System Prompt Stored?

Remember your messages list.

messages = [
    {
        "role":"system",
        "content":"You are..."
    }
]

The system prompt is simply the first message.

Every time you call the API:

response = client.chat.completions.create(
    model=model_name,
    messages=messages
)

the entire list, including the system prompt, is sent.

Can the User Change the System Prompt?

Normally, no.

The user only controls:

{
    "role":"user"
}

The developer controls:

{
    "role":"system"
}

This separation lets you build reliable AI applications.

Real Products
AI Coding Assistant
You are a senior software engineer.

Write production-quality code.

Always explain time complexity.

Suggest best practices.

Avoid deprecated APIs.
Medical Assistant
You are a licensed medical information assistant.

Explain conditions in simple language.

Do not diagnose.

Recommend consulting a healthcare professional when appropriate.
HR Interview Bot
You are an HR interviewer.

Ask one question at a time.

Wait for the candidate's response.

Give feedback after each answer.

One LLM.

Different system prompts.

Different products.

Let's Improve Your Chatbot

Right now, your system prompt is:

{
    "role":"system",
    "content":"You are a helpful AI tutor."
}

That's good, but it's too generic.

Let's make it much more useful for your learning journey.

Replace it with:

{
    "role": "system",
    "content": """
You are an expert AI Developer and mentor.

Teach concepts from beginner to advanced.

Explain every topic step by step.

Use simple English.

Whenever appropriate:
- give real-world examples
- explain internal working
- explain interview answers
- explain common mistakes
- ask one practice question after every explanation

Never skip steps.
"""
}

Now your chatbot becomes your personal AI mentor.

Mini Challenge

Try these three different system prompts:

Version 1
You are a senior AI engineer.
Version 2
You are a strict interviewer.
Version 3
You are an AI mentor who teaches step by step with examples and interview tips.

Ask exactly the same user question:

Explain Transformers.

Compare the answers.

You'll see how powerful the system prompt is.

Interview Question ⭐⭐⭐⭐⭐

What is a System Prompt?

Professional Answer:

A system prompt is a developer-defined instruction that establishes the AI assistant's behavior, role, tone, and constraints. It is sent as part of the conversation history with every API request and guides how the model responds to user inputs.

🏆 Homework

Modify your chatbot so the system prompt makes it behave like:

A Senior AI Engineer with 15 years of experience who mentors junior developers step by step.

Test it with five different AI-related questions and observe how the style changes.



Lesson 11.3 – Zero-Shot, One-Shot & Few-Shot Prompting
Before We Start

Imagine you're hiring a new employee.

You ask:

"Write a professional email."

The employee writes something.

Now imagine you first show them one example of a good email.

Do you think their next email will be better?

✅ Yes.

Now imagine you show them five examples.

Even better.

The same principle applies to LLMs.

The Three Prompting Techniques
Prompt Engineering

│

├── Zero-Shot

├── One-Shot

└── Few-Shot
1️⃣ Zero-Shot Prompting
Definition

You ask the model to perform a task without giving any examples.

Example:

Translate this into French:

Hello, how are you?

No examples.

The model uses its pre-trained knowledge.

Another Example
Summarize this article.

Again,

No example.

This is Zero-Shot.

Why is it called "Zero-Shot"?

Because the model gets:

0 Examples
Real AI Example
Explain RAG.

The model already knows RAG.

No examples needed.

Advantages
Fast
Short prompt
Low token cost
Disadvantages

Sometimes the model misunderstands your expectations.

2️⃣ One-Shot Prompting

Now suppose we give one example.

Example:

Convert text into JSON.

Example:

Input:
John is 25 years old.

Output:
{
"name":"John",
"age":25
}

Now convert:

Alice is 30 years old.

Notice what happened?

We taught the model the expected format.

Why?

Instead of guessing,

the model copies the pattern.

Visual
One Example

↓

Learn Pattern

↓

Generate Similar Output
Advantages
More consistent output
Better formatting
Lower error rate
3️⃣ Few-Shot Prompting

Now we give multiple examples.

Example:

Sentiment Analysis

Example 1

Input:
I love Python.

Output:
Positive

-------------------

Example 2

Input:
This movie is terrible.

Output:
Negative

-------------------

Example 3

Input:
The weather is okay.

Output:
Neutral

-------------------

Now classify:

I hate traffic.

The model sees the pattern across several examples.

Why is Few-Shot Powerful?

Imagine teaching a child.

One example helps.

Five examples make the rule much clearer.

Visual Comparison
Zero-Shot

Question

↓

AI

---------------

One-Shot

Example

↓

Question

↓

AI

---------------

Few-Shot

Example

Example

Example

↓

Question

↓

AI
Real Company Example

Suppose you're building an AI Resume Analyzer.

Zero-Shot
Analyze this resume.
One-Shot
Example Resume

↓

Example Analysis

↓

Analyze this resume.
Few-Shot
Resume 1

↓

Analysis

------------

Resume 2

↓

Analysis

------------

Resume 3

↓

Analysis

------------

Analyze this new resume.

The AI produces much more consistent evaluations.

When Should You Use Each?
Technique	When to Use
Zero-Shot	General tasks the model already knows
One-Shot	When you need a specific output format
Few-Shot	When consistency and pattern matching are important
Live Experiment

Open your chatbot.

Prompt 1 (Zero-Shot)
Classify this review as Positive or Negative.

"I love this laptop."
Prompt 2 (One-Shot)
Example:

Review:
I love Python.

Sentiment:
Positive

Now classify:

"I love this laptop."
Prompt 3 (Few-Shot)
Example 1

Review:
I love Python.

Sentiment:
Positive

-----------------

Example 2

Review:
This phone is terrible.

Sentiment:
Negative

-----------------

Example 3

Review:
The weather is okay.

Sentiment:
Neutral

-----------------

Review:
I love this laptop.

Compare the outputs.

Why Does This Work?

The LLM doesn't "memorize" these examples.

Instead, it uses them as context.

Remember the Transformer lesson?

The examples become part of the messages sent to the model.

The Transformer uses self-attention to recognize the pattern and continue it.

Everything you've learned so far is connecting:

Messages
      ↓
Context
      ↓
Transformer
      ↓
Self-Attention
      ↓
Pattern Recognition
      ↓
Response
Interview Question ⭐⭐⭐⭐⭐
What is the difference between Zero-Shot, One-Shot, and Few-Shot Prompting?

Professional Answer:

Zero-shot prompting asks the model to perform a task without providing examples. One-shot prompting includes a single example to demonstrate the expected format or behavior. Few-shot prompting provides multiple examples, allowing the model to infer patterns and produce more consistent, accurate outputs for similar tasks.

🎯 Mini Assignment

Create three prompts for the same task:

Task: Extract information from a sentence.

Sentence:

Yukesh is 22 years old and lives in Salem.
Write a Zero-Shot prompt.
Write a One-Shot prompt.
Write a Few-Shot prompt.

Try them in your chatbot and compare the results.



Lesson 11.4 — Structured Output & JSON
The Biggest Beginner Mistake

Suppose you ask:

Analyze this resume.

The AI might answer:

This candidate has strong Python skills.
He also knows React.
Overall score is 90%.

Looks good.

But...

How will React display the score?

How will Django save it into MySQL?

How will you draw a chart?

Impossible.

Because this is just plain English.

What Software Wants

Programs communicate using structured data.

Most common format?

👉 JSON.

What is JSON?

You already know JavaScript.

JSON stands for:

JavaScript Object Notation

It is simply a structured way to represent data.

Example:

{
    "name": "Yukesh",
    "age": 22,
    "city": "Salem"
}
Why Do AI Applications Love JSON?

Imagine this flow:

LLM

↓

JSON

↓

Python

↓

Django API

↓

React

↓

Dashboard

Every layer understands JSON.

Example 1

Instead of asking

Tell me about Python.

Ask

Explain Python.

Return the answer in JSON format with:

- definition
- advantages
- disadvantages
- applications

Now the model may return:

{
    "definition": "...",
    "advantages": [
        "...",
        "..."
    ],
    "disadvantages": [
        "...",
        "..."
    ],
    "applications": [
        "...",
        "..."
    ]
}

Now your React app can do:

data.definition

data.advantages

data.applications

No text parsing needed.

Why Is This Better?

Without JSON

LLM

↓

Paragraph

↓

Regex

↓

Split()

↓

Hope it works 😅

With JSON

LLM

↓

JSON

↓

json.loads()

↓

Done

Much cleaner.

Python Side

Suppose the AI returns:

{
    "name":"Yukesh",
    "skills":["Python","React"]
}

Python can do:

import json

data = json.loads(response_text)

print(data["name"])

print(data["skills"])

Now your AI response becomes a Python dictionary.

Real Project Example

Imagine your future Resume Analyzer.

Instead of this:

Candidate has good Python skills.

ATS Score: 87

Missing Skills:

Docker

AWS

Return this:

{
    "candidate_name":"Yukesh",
    "ats_score":87,
    "strengths":[
        "Python",
        "React"
    ],
    "missing_skills":[
        "Docker",
        "AWS"
    ],
    "recommendations":[
        "Learn Docker",
        "Learn AWS"
    ]
}

React can directly display:

ATS Score Card

↓

Strength Cards

↓

Recommendation Cards
Prompt Engineering for JSON

Instead of:

Analyze this resume.

Use:

Analyze this resume.

Return ONLY valid JSON.

Do not include markdown.

Do not explain.

Fields:

candidate_name

score

strengths

weaknesses

recommendations

Notice the wording.

"Return ONLY valid JSON"

This reduces formatting mistakes.

But...

Can We Trust the AI?

Suppose you asked for JSON.

The AI replies:

Sure!

```json
{
...
}
```

Problem.

Those triple backticks make it not pure JSON.

Your parser fails.

This Is Why Modern APIs Added JSON Mode

Older Prompt Engineering:

Please return JSON.

Not guaranteed.

Modern APIs provide structured output modes that are much more reliable.

Depending on the provider and SDK, you may use features such as:

JSON response formats
Structured outputs
Schema-based responses

These reduce the chance of invalid JSON.

Industry Example

Imagine you're building:

AI Interview System

User uploads a resume.

The AI returns:

{
    "score":91,
    "confidence":"High",
    "recommended_role":"AI Developer",
    "missing_skills":[
        "Docker",
        "Kubernetes"
    ]
}

Your React frontend can immediately:

Show a progress bar
Draw charts
Display missing skills
Save the result in MySQL

No manual text parsing.

How This Connects to Django

Remember your stack?

React

↓

Django

↓

LLM

↓

Groq

Django already communicates using JSON.

So your AI response naturally fits into your existing backend.

Interview Question ⭐⭐⭐⭐⭐
Why is JSON preferred over plain text in AI applications?

Professional Answer

JSON provides a structured, machine-readable format that can be easily parsed and integrated into applications. It enables reliable communication between LLMs, backend services, databases, and frontend frameworks without requiring fragile text parsing.

Small Exercise

Modify your chatbot prompt to ask:

You are an AI career advisor.

Analyze a candidate.

Return ONLY valid JSON.

Fields:

name

role

skills

experience_level

recommendations

Ask it to analyze yourself.

Observe whether the model returns valid JSON.

🚀 Next Lesson (One of the Most Important for Modern AI)

Now that you know how to get structured output, we'll learn Tool Calling (Function Calling).

This is where LLMs stop being "chatbots" and start becoming AI assistants.

Imagine asking:

"What's the weather in Salem?"

Without tools, the model guesses.

With tool calling:

User
    │
    ▼
LLM
    │
    ▼
Calls Weather API
    │
    ▼
Receives Live Weather
    │
    ▼
Answers User

This concept is the foundation of:

ChatGPT tools
GitHub Copilot
Cursor AI
Claude tools
MCP (Model Context Protocol)
AI Agents

Once you understand tool calling, you'll see how LLMs interact with real-world systems instead of just generating text. This is one of the biggest transitions from prompt engineering to agentic AI.



Lesson 11.5 – Tool Calling (Function Calling)
First Question

Imagine I ask ChatGPT:

What is the current weather in Salem?

Question:

Can an LLM know today's weather?

No.

Why?

Because the LLM only knows what it learned during training plus whatever you send in the current prompt. It doesn't automatically have live internet access.

Think Like a Human

Suppose I ask you:

What's the current weather in Salem?

You don't know either.

So what do you do?

Question

↓

Open Weather App

↓

Read Weather

↓

Tell Me

Exactly.

You use a tool.

LLMs Work the Same Way

Without tools:

User

↓

LLM

↓

"I don't know today's weather."

With tools:

User

↓

LLM

↓

Weather API

↓

Live Weather

↓

LLM

↓

Answer
What Is a Tool?
Beginner Definition

A tool is an external function, API, database, or service that an LLM can use to obtain information or perform actions beyond its built-in knowledge.

Interview Definition ⭐⭐⭐⭐⭐

Tool calling is the capability of an LLM to request the execution of external functions or APIs in order to retrieve information or perform actions that are outside the model's internal knowledge.

Real Examples
Without Tool
User:
What time is it in Tokyo?

LLM:
I don't know the current time.
With Tool
User

↓

LLM

↓

Clock API

↓

Current Time

↓

LLM

↓

"It is 10:30 PM."
More Examples
Calculator

User:

875463 × 7832

Without tool:

The LLM might make an arithmetic mistake.

With tool:

LLM

↓

Calculator

↓

Correct Answer

↓

User
Database

User:

What is Yukesh's ATS Score?

LLM:

Database

↓

Score = 91

↓

Answer
Email

User:

Send an email to Manoj.

LLM:

Email API

↓

Send Email

↓

Success

↓

User
Tool Calling Architecture
User Question

↓

LLM

↓

Do I know this?

↓

YES
│
└── Generate Answer

NO
│
▼
Select Tool

↓

Execute Tool

↓

Receive Result

↓

Generate Final Answer
Important Concept
The LLM Does Not Execute Python

Many beginners think:

LLM

↓

Runs Python

❌ Wrong.

Instead:

LLM

↓

Requests Tool

↓

Python Program Executes Tool

↓

Returns Result

↓

LLM Uses Result

The application executes the function, not the model.

Simple Python Example

Suppose you have this function:

def get_weather(city):
    return f"The weather in {city} is 31°C and Sunny."

The LLM doesn't call it directly.

Instead, the flow is:

User

↓

LLM

↓

"I need get_weather(city='Salem')"

↓

Python executes get_weather("Salem")

↓

Result

↓

LLM

↓

Final Response
Another Example

User:

What is 547 × 832?

Instead of guessing:

LLM

↓

Calculator Tool

↓

455104

↓

LLM

↓

"The answer is 455104."
Why Is This Better?

Without Tool:

LLM guesses.

With Tool:

LLM retrieves.

This makes answers more reliable for tasks that require external information or exact computation.

Where Does RAG Fit?

Remember RAG?

Question

↓

Embedding

↓

Vector DB

↓

Relevant Chunks

↓

LLM

The retriever itself is effectively a tool.

The LLM asks for relevant context, the application retrieves it, then the LLM answers using that retrieved information.

Tool Calling vs RAG
Tool Calling	RAG
Calls APIs/functions	Retrieves documents
Weather API	Vector Database
Calculator	PDF Search
Email Service	Knowledge Base
Executes actions	Retrieves context
Modern AI Applications
LLM

├── Weather Tool

├── Calculator Tool

├── Gmail Tool

├── Calendar Tool

├── Database Tool

├── SQL Tool

├── PDF Search Tool

└── Web Search Tool

One model.

Many tools.

Where Does MCP Come In?

Remember the roadmap?

We'll learn MCP (Model Context Protocol) later.

MCP provides a standard way for AI models to discover and use tools.

Instead of writing custom integrations for every application, tools can expose a common interface.

So you can think of MCP as:

MCP

↓

Standard Language

↓

LLM

↓

Any Tool

We'll build an MCP server ourselves later in the course.

Interview Question ⭐⭐⭐⭐⭐
What is Tool Calling?

Professional Answer:

Tool calling enables an LLM to request the execution of external functions or APIs. The application executes the requested tool, returns the result to the model, and the model uses that result to generate its final response. This allows AI systems to access live data and perform real-world actions beyond the model's built-in knowledge.

Assignment

Think about your future AI Resume Analyzer.

List five tools it could use.

For example:

PDF Reader
Resume Parser
Skill Database
ATS Scoring Engine
Job Description Matcher

Don't worry about coding them yet—just identify what external capabilities your application would need.

🚀 What's Next?

Now we move into LLM Engineering, where the concepts become more practical.

Module 5 – Embedding Models

This is where you'll finally answer questions like:

Why do we need a separate embedding model when we already have an LLM?
Why doesn't ChatGPT use the LLM itself for similarity search?
What is sentence-transformers/all-MiniLM-L6-v2, which you saw in your friend's project?
How does text become vectors before entering a vector database?

This module connects directly to RAG, ChromaDB, FAISS, LangChain, and every production retrieval system. Once you understand embedding models, you'll be ready to build your first complete RAG application instead of just using one.


