from src.corpus import get_all_documents


data = get_all_documents()

print("Number of documents:", len(data["documents"]))


for i, document in enumerate(data["documents"]):

    print("\nDocument:", i)

    print(document[:300])