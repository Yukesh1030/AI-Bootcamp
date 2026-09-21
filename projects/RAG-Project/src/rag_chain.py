import os

from dotenv import load_dotenv

# pyrefly: ignore [missing-import]
from openai import OpenAI

from src.retriever import retrieve_documents


# Load environment variables
load_dotenv()


# Create Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# Model
model_name = os.getenv(
    "MODEL_NAME",
    "llama-3.1-8b-instant"
)


def ask_rag(query):

    # --------------------------------
    # 1. Retrieve relevant documents
    # --------------------------------

    documents = retrieve_documents(
        query,
        n_results=3
    )

    print("\nRetrieved Documents:")
    print(documents)


    # --------------------------------
    # 2. Convert documents into context
    # --------------------------------

    context = "\n\n".join(documents)


    print("\n==============================")
    print("CONTEXT SENT TO AI")
    print("==============================")

    # print(context)


    # --------------------------------
    # 3. Create RAG prompt
    # --------------------------------

    prompt = f"""
You are an AI assistant that answers questions about a resume.

Use ONLY the information provided in the CONTEXT below.

If the answer exists in the CONTEXT, answer the question clearly.

If the answer is not present in the CONTEXT, say:
"I don't know based on the provided document."

Do not make up information.

CONTEXT:
--------------------
{context}
--------------------

QUESTION:
{query}

ANSWER:
"""


    # --------------------------------
    # 4. Send prompt to Groq
    # --------------------------------

    response = client.chat.completions.create(

        model=model_name,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )


    # --------------------------------
    # 5. Extract AI response
    # --------------------------------

    answer = response.choices[0].message.content


    return answer