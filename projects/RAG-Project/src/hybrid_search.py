from src.semantic_search import semantic_search
from src.keyword_search import BM25Retriever
from src.corpus import get_all_documents
from src.rrf import reciprocal_rank_fusion


class HybridRetriever:

    def __init__(self):

        data = get_all_documents()

        self.documents = data["documents"]

        self.bm25 = BM25Retriever(
            self.documents
        )


    def search(
        self,
        query,
        top_k=5
    ):

        # --------------------------------
        # 1. Semantic Search
        # --------------------------------

        semantic_results = semantic_search(
            query,
            top_k=top_k
        )


        # --------------------------------
        # 2. Keyword Search
        # --------------------------------

        keyword_results = self.bm25.search(
            query,
            top_k=top_k
        )


        # Add rank information
        keyword_results = [
            {
                "document": result["document"],
                "rank": index + 1
            }
            for index, result
            in enumerate(keyword_results)
        ]


        # --------------------------------
        # 3. RRF Fusion
        # --------------------------------

        hybrid_results = reciprocal_rank_fusion(
            [
                semantic_results,
                keyword_results
            ]
        )


        return hybrid_results[:top_k]