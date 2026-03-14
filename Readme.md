# 🧠 Neural Search Engine (Semantic Search)

A production-style **Neural Search Engine** that retrieves semantically relevant documents using **transformer embeddings + FAISS vector search**.
This project demonstrates how modern AI systems perform **semantic retrieval**, similar to technologies used in **RAG pipelines, recommendation engines, and AI assistants**.

Instead of relying on keyword matching, this system understands the **meaning of text** and retrieves relevant documents even if exact words are different.

---

# 📌 Project Overview

Traditional search systems depend on **keyword matching**.

Example:

Query
`How to improve database performance?`

Keyword search may fail if documents contain phrases like:

* query optimization
* indexing techniques
* caching strategies

Semantic search solves this by converting text into **dense vector embeddings** and retrieving documents based on **semantic similarity**.

This project implements a **complete semantic search pipeline** including:

* Text embedding generation
* FAISS vector indexing
* REST API for search
* Streamlit UI for interactive search

---

# ⚙️ System Architecture

```
Documents
   ↓
Text Preprocessing
   ↓
Embedding Model (Sentence Transformer)
   ↓
Vector Embeddings
   ↓
FAISS Vector Index
   ↓
FastAPI Search API
   ↓
Streamlit User Interface
```

---

# 🚀 Features

✔ Semantic document retrieval
✔ Transformer-based embeddings
✔ FAISS vector similarity search
✔ REST API serving with FastAPI
✔ Interactive search interface using Streamlit
✔ Persistent vector index storage
✔ Scalable retrieval pipeline

---

# 🧩 Technologies Used

| Component            | Technology            |
| -------------------- | --------------------- |
| Embedding Model      | Sentence Transformers |
| Vector Search        | FAISS                 |
| API Server           | FastAPI               |
| UI Interface         | Streamlit             |
| Data Processing      | Pandas / NumPy        |
| Programming Language | Python                |

---

# 📁 Project Structure

```
neural-search-engine
│
├── data
│   └── wikipedia_chunks.csv
│
├── models
│   ├── faiss_index.index
│   └── documents.pkl
│
├── build_index.py
├── search_api.py
├── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The project uses a **Wikipedia text chunk dataset**.

Each document is divided into smaller chunks for better semantic retrieval.

Example dataset format:

| id | chunk                                                          |
| -- | -------------------------------------------------------------- |
| 1  | Deep learning uses neural networks for representation learning |
| 2  | Database indexing improves query performance                   |

Chunking improves search accuracy by retrieving **relevant paragraphs instead of entire documents**.

---

# 🧠 Embedding Model

The system uses a **Sentence Transformer model**:

```
BAAI/bge-base-en-v1.5
```

Properties:

* 384 dimensional embeddings
* Fast inference
* Strong semantic similarity performance

Embedding example:

```
"machine learning models"

→ [0.21, -0.43, 0.66, ...]
```

These vectors represent the **semantic meaning of text**.

---

# 🔎 Vector Search with FAISS

The project uses **Facebook AI Similarity Search (FAISS)** to perform fast nearest-neighbor retrieval.

FAISS enables efficient search among thousands or millions of embeddings.

Process:

```
Query
   ↓
Query Embedding
   ↓
FAISS Similarity Search
   ↓
Top-K Relevant Documents
```

Distance metric used:

```
L2 distance
```

---

# 🛠 Installation

Clone the repository:

```
git clone https://github.com/yourusername/neural-search-engine.git
cd neural-search-engine
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 📦 Build the Vector Index

Run the index builder to generate embeddings and create the FAISS index.

```
python build_index.py
```

This step will:

1. Load dataset
2. Generate embeddings
3. Build FAISS index
4. Save index to disk

Output files:

```
models/faiss_index.index
models/documents.pkl
```

---

# 🌐 Start the Search API

Launch the FastAPI server.

```
uvicorn search_api:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🖥 Run the Streamlit Interface

Start the search UI.

```
streamlit run streamlit_app.py
```

Open the browser:

```
http://localhost:8501
```

Search interface example:

```
Enter search query:
[ machine learning models ]

Results:
1. Machine learning models require large datasets
2. Deep learning is a subset of machine learning
3. Neural networks enable representation learning
```

---

# 🔍 Example API Request

POST request:

```
/search
```

Request body:

```
{
  "text": "machine learning algorithms",
  "top_k": 5
}
```

Response:

```
{
  "query": "machine learning algorithms",
  "results": [
    {
      "rank": 1,
      "text": "...",
      "score": 0.42
    }
  ]
}
```

---

# 📈 Performance Optimization

The system includes:

* Batch embedding generation
* FAISS IVF index
* Persistent vector storage

Possible future improvements:

* GPU FAISS indexing
* hybrid search (BM25 + embeddings)
* cross-encoder re-ranking
* query expansion

---

# 🧪 Example Queries

Example queries to test the search engine:

```
machine learning algorithms
history of artificial intelligence
database optimization techniques
deep neural networks
distributed systems architecture
```

---

# 🧠 Applications

Semantic search is used in many modern AI systems:

* RAG pipelines
* document search
* enterprise knowledge retrieval
* recommendation systems
* AI assistants
* research paper retrieval

---

# 🚀 Future Improvements

Planned improvements for the system:

* Hybrid keyword + semantic search
* Re-ranking models
* Real-time indexing
* distributed vector database
* multilingual search support

---

# 👨‍💻 Author

Developed as part of an **AI/ML portfolio project demonstrating neural search systems**.

---

# 📜 License

This project is released under the **MIT License**.
