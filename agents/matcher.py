from langchain.vectorstores import Chroma
import numpy as np
from typing import Dict


vectorstore = Chroma(persist_directory="investor_chroma_db", embedding_function=None)  # No auto-embed
def match_investors(state):
    query_vector = np.array(state["embedding"])
    db = vectorstore._collection.get(include=["documents", "embeddings", "metadatas"])
    investor_embeddings = np.array(db["embeddings"])
    investor_docs = db["documents"]
    investor_metadata = db["metadatas"]

    sims = np.dot(investor_embeddings, query_vector) / (
        np.linalg.norm(investor_embeddings, axis=1) * np.linalg.norm(query_vector)
    )
    top_k = sims.argsort()[-5:][::-1]

    raw_matches = []
    for idx in top_k:
        raw_matches.append({
            "name": investor_metadata[idx].get("name", "Unknown"),
            "similarity": sims[idx],
            "profile": investor_docs[idx]
        })

    return {"query": state["query"], "raw_matches": raw_matches}
