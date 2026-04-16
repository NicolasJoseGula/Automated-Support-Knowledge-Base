import re
from src.document_processor import process_document

STOP_WORDS = {
    "what", "is", "the", "a", "an", "in", "of", "to", "and", "or",
    "how", "why", "when", "where", "who", "which", "that", "this",
    "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "do", "does", "did", "will", "would", "could", "should", "may",
    "can", "about", "for", "with", "from", "by", "at", "on", "it"
}

class KnowledgeBase:
    def __init__(self):
        self.documents = []
        
    def add_document(self, file_path: str) -> str:
        doc = process_document(file_path)
        self.documents.append(doc)
        return f"Document '{doc['file_name']}' loaded successfully. ({len(doc['chunks'])})"
    
    def list_documents(self) -> list[str]:
        return [doc["file_name"] for doc in self.documents]
    
    def find_relevant_chunk(self, question: str) -> str:
        if not self.documents:
            return ""
        
        question_words = set(re.findall(r'\w+', question.lower())) - STOP_WORDS
        best_chunk = ""
        best_score = -1
        
        for doc in self.documents:
            for chunk in doc["chunks"]:
                chunk_words = set(re.findall(r'\w+', chunk.lower()))
                score = len(question_words & chunk_words)
                if score > best_score:
                    best_score = score
                    best_chunk = chunk
        return best_chunk
    
    
    
    
    
    
    
    
    
    
    
    
    
