from rank_bm25 import BM25Okapi


class HybridSearchService:

    def keyword_search(self, query, documents, top_k=3):

        tokenized_docs = [doc.split() for doc in documents]
        bm25 = BM25Okapi(tokenized_docs)

        tokenized_query = query.split()

        scores = bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [doc for doc, _ in ranked[:top_k]]


hybrid_search_service = HybridSearchService()