import os

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from openai import OpenAI


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

print("API KEY LOADED:", bool(api_key))

if not api_key:
    raise ValueError("GROQ_API_KEY was not loaded.")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


print("\nChecking available Groq models...\n")

models = client.models.list()

for model in models.data:
    print(model.id)