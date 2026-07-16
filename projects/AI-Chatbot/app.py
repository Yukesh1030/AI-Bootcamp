from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
model_name=os.getenv("MODEL_NAME")

client =OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
messages = [
    {
        "role":"system",
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
]

while True:

    user_question = input("\nYou : ")

    if user_question.lower() == "exit" or user_question.lower() == "stop":
        print("\n👋 Goodbye!")
        # print(messages)
        break

    messages.append(
        {
            "role":"user",
            "content":user_question
        }
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=True
    )

    print("\nAI :")
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            full_response+=token
            print(token,end="",flush=True)
    print()

    # print(response.choices[0].message.content)



