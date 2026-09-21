def reciprocal_rank_fusion(
    result_lists,
    k=60
):

    scores = {}
    documents = {}

    for results in result_lists:

        for result in results:

            document = result["document"]
            rank = result["rank"]

            if document not in scores:
                scores[document] = 0.0
                documents[document] = document

            scores[document] += 1 / (
                k + rank
            )

    ranked_documents = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    output = []

    for rank, (document, score) in enumerate(
        ranked_documents,
        start=1
    ):

        output.append({
            "document": document,
            "score": score,
            "rank": rank
        })

    return output