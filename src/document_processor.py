from pypdf import PdfReader
import re

def clean_text(text: str) -> str:
    text = re.sub(r'[^\x20-\x7E\n]', ' ', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return clean_text(text)

def chunk_text(text: str, chunk_size: int=400, overlap: int=50) -> list[str]:
    words = text.split()
    chunks = []
    start = 0
    
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def process_document(file_path: str) -> dict:
    file_name = file_path.split("/")[-1].split("\\")[-1]
    full_text = extract_text_from_pdf(file_path)
    chunks = chunk_text(full_text)

    return {
        "file_name": file_name,
        "full_text": full_text,
        "chunks": chunks
}
