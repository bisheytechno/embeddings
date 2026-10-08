from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

e1 = model.encode("Cat is a pet")
e2 = model.encode("Dog is a pet")
e3 = model.encode("Car is a vehicle")

print(util.cos_sim(e1, e2).item())
# 0.856 ← High! Similar!

print(util.cos_sim(e1, e3).item())
# 0.124 ← Low! Different!