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

while True:
    user_questions=input("\nYou : ")

    if user_questions.lower()=="exit":
        print("\n👋 Goodbye!")
        break
    response = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role":"user",
            # "content":"What is AI?"
            "content":user_questions
        }
        ]
        )
    print("\nAI : ")
    print(response.choices[0].message.content)




