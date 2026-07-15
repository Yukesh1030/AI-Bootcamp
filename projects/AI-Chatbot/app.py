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
        "content":"You are a helpful AI tutor."
    }
]

while True:

    user_question = input("\nYou : ")

    if user_question.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    messages.append(
        {
            "role":"user",
            "content":user_question
        }
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    print("\nAI :")
    print(response.choices[0].message.content)



