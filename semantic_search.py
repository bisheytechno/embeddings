from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')


docs = [
    "Python is a programming language",
    "Nepal is in Asia",
    "Machine learning uses data to train models",
    "Kathmandu is the capital of Nepal",
    "Deep learning uses neural networks"
]


query = "How does AI learn?"


doc_embeddings   = model.encode(docs)
query_embedding  = model.encode(query)


scores  = util.cos_sim(query_embedding, doc_embeddings)[0]

best_idx = scores.argmax()

print(f"Query: {query}")
print(f"Best match: {docs[best_idx]}")
print(f"Score: {scores[best_idx]:.3f}")