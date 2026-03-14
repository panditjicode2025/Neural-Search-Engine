import faiss
import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

print("Loading FAISS index...")

index = faiss.read_index("models/faiss_index.index")

df = pd.read_pickle("models/documents.pkl")

model = SentenceTransformer("BAAI/bge-base-en-v1.5")

app = FastAPI(title="Neural Search API")


class Query(BaseModel):
    text: str
    top_k: int = 5


@app.get("/")
def home():
    return {"message": "Neural Search Engine API running"}


@app.post("/search")
def search(query: Query):

    query_embedding = model.encode([query.text]).astype("float32")

    distances, indices = index.search(query_embedding, query.top_k)

    results = []

    for i, idx in enumerate(indices[0]):

        results.append({
            "rank": i + 1,
            "text": df.iloc[idx]["content"],
            "score": float(distances[0][i])
        })

    return {"query": query.text, "results": results}