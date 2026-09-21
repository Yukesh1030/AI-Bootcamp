import re
from rank_bm25 import BM25Okapi

def tokenize(text):
    """
    Convert text into simple normalized tokens.
    """
    return re.findall(r"\b\w+\b", text.lower())

class BM25Retriever:
    def __init__(self, documents):
        self.documents = documents

        tokenized_documents = [tokenize(documents) for documents in documents]

        self.bm25 = BM25Okapi(tokenized_documents)

    def search(self,query,top_k=5):
        query_tokens = tokenize(query)
        scores = self.bm25.get_scores(query_tokens)

        ranked_indices = scores.argsort()[::-1][:top_k]

        results =[]

        for index in ranked_indices:
            results.append({"document": self.documents[index], 
                            "score": scores[index], 
                            "index": index})
        return results
