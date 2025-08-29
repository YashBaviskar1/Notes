from sentence_transformers import SentenceTransformer


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


statement = "This is a sentence." 

embedding = model.encode(statement)
print(embedding.shape)
print(embedding[:10])