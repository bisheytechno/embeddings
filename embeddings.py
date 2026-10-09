from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

embedding = model.encode("Hello, I love Python!")
embedding1 = model.encode("My favourite programming language is python!")
print(embedding)