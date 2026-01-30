VECTOR_STORE = []

def add_vectors(chunks, embed_fn):
    VECTOR_STORE.clear()
    for chunk in chunks:
        VECTOR_STORE.append({
            "text": chunk,
            "vector": embed_fn(chunk)
        })

def search_vectors(query_vector, similarity_fn):
    best = {"text": "", "score": 0.0}

    for item in VECTOR_STORE:
        score = similarity_fn(query_vector, item["vector"])
        if score > best["score"]:
            best = {"text": item["text"], "score": score}

    return best
