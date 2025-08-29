import chromadb 
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
pdf_path = "fractalWorkingPaper.pdf"
Client = chromadb.Client()
collections = Client.create_collection("documents")
reader = PdfReader(pdf_path)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
extracted_text = ""

for page in reader.pages : 
    extracted_text += page.extract_text()

print( " No of words in the pdf : ", len(extracted_text.split()))


def chunk_text(text, chunk_size=300, overlap = 50):
    words = text.split()
    chunks = []
    size = len(words)
    i = 0 
    while i < size :
        chunk = words[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

print(" No of Chunks : ", len(chunk_text(extracted_text)))
data = chunk_text(extracted_text)


embeddings = model.encode(data, batch_size=32, show_progress_bar=True)

collections.add(
    ids = [f"chunk_{i}" for i in range(len(data))],
    documents=data,
    embeddings=embeddings.tolist()

)


query = "What type of Caste Based Discrimination occurs in india?"
query_embedding = model.encode(query)

results = collections.query(
    query_embeddings=[query_embedding.tolist()],
    n_results= 2
)

print("Query Results:")
print(results)