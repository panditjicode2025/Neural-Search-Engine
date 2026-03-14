import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


print("Loading dataset...")

df = pd.read_csv("data/wikipedia_books_dataset.csv")

texts = df["content"].tolist()
print("Loading embedding model...")
model = SentenceTransformer("BAAI/bge-base-en-v1.5")

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    batch_size=64,
    show_progress_bar=True
)

embedding_matrix = np.array(embeddings).astype("float32")

dimension = embedding_matrix.shape[1]

print("Building FAISS IVF index...")

nlist = 100
quantizer = faiss.IndexFlatL2(dimension)

index = faiss.IndexIVFFlat(
    quantizer,
    dimension,
    nlist,
    faiss.METRIC_L2
)

index.train(embedding_matrix)
index.add(embedding_matrix)

faiss.write_index(index, "models/faiss_index.index")

df.to_pickle("models/documents.pkl")

print("Index built and saved.")