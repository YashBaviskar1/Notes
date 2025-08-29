import chromadb

Client = chromadb.Client()

collections = Client.create_collection("my_documents")

collections.add(
    ids=["1", "2"],
    documents=['this is a text', 'this is another text'],
    embeddings=[[0.1,0.2,0.3], [0.1,0.3,0.9]]
)

results = collections.query(
    query_embeddings=[[0.1,0.55,0.7]],
    n_results= 1
)

print(results)