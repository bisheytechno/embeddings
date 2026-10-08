# Embeddings

Learning text embeddings from scratch — foundation for RAG and semantic search in AI engineering.

---

## What This Covers

- Text embeddings — converting text to numbers
- Cosine similarity — comparing text similarity
- Semantic search — finding relevant documents

---

## Tech Stack

- Python 3.x
- sentence-transformers
- VS Code

---

## Project Structure

```
embeddings/
│
├── myvenv/
├── embeddings.py        → Basic embedding
├── similarity.py        → Cosine similarity
├── semantic_search.py   → Semantic search
├── requirements.txt     → Dependencies
├── .gitignore
└── README.md
```

---

## How to Run

**1. Clone:**
```bash
git clone https://github.com/bisheytechno/embeddings.git
cd embeddings
```

**2. Virtual Environment:**
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

**3. Install:**
```bash
pip install -r requirements.txt
```

**4. Run:**
```bash
python embeddings.py
python similarity.py
python semantic_search.py
```

---

## Key Concepts

| Concept | What it does |
|---------|-------------|
| model.encode() | Text → Numbers (384 dimensions) |
| util.cos_sim() | Similarity score between two texts |
| argmax() | Find most similar document |
| Semantic Search | Find relevant docs by meaning |

---

## Similarity Scores

```
1.0  → Identical
0.8+ → Very similar
0.5  → Somewhat similar
0.0  → Completely different
```

---

## Requirements

```
sentence-transformers
```

---

## Author

**Bishal KC** — Aspiring AI Engineer

---

## License

MIT License