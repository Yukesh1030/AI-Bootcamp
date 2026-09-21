from src.pdf_loader import load_pdf
from src.chunking import chunk_text
from src.embeddings import generate_embeddings
from src.vector_store import store_documents
from src.rag_chain import ask_rag


# ==========================================
# PDF → CHUNKS → EMBEDDINGS → CHROMADB
# ==========================================

text = load_pdf(
    "data/Yukesh_G_ATS_Resume.pdf"
)

print("\nPDF loaded successfully.")

print(
    "Total characters:",
    len(text)
)


chunks = chunk_text(
    text,
    chunk_size=500,
    overlap=100
)

print(
    "Total chunks:",
    len(chunks)
)


embeddings = generate_embeddings(
    chunks
)

print(
    "Embeddings generated successfully."
)

print(
    "Embedding count:",
    len(embeddings)
)

print(
    "Embedding dimension:",
    len(embeddings[0])
)


store_documents(
    chunks,
    embeddings
)

print(
    "Stored successfully in ChromaDB."
)


# ==========================================
# RAG CHAT
# ==========================================

print("\n===================================")
print("        AI RAG CHATBOT")
print("===================================")

print(
    "Ask questions about your resume."
)

print(
    "Type 'exit' to quit."
)


while True:

    query = input(
        "\nYou: "
    )


    if query.lower() == "exit":

        print(
            "\nGoodbye! 👋"
        )

        break


    try:

        answer = ask_rag(
            query
        )

        print(
            "\nAI:"
        )

        print(
            answer
        )


    except Exception as e:

        print(
            "\nError:",
            e
        )