from PyPDF2 import PdfReader

pdf_path = "fractalWorkingPaper.pdf"

reader = PdfReader(pdf_path)
extracted_text = ""

for page in reader.pages : 
    extracted_text += page.extract_text()

print(len(extracted_text.split()))

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

print(len(chunk_text(extracted_text)))
data = chunk_text(extracted_text)
print(data[:10])