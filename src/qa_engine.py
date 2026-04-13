from transformers import pipeline

class QAEngine:
    def __init__(self):
        self.pipeline = pipeline(
            task="question-answering",
            model="distilbert-base-cased-distilled-squad"
        )
        
        
    def answer(self, question: str, context: str) -> dict:
        if not context:
            return{
                "answer":"No relevant context found. Please upload a document first.",
                "score":0.0
            }
        
        result  = self.pipeline(question=question, context=context)
        
        return {
            "answer": result["answer"],
            "score": round(result["score"], 4)
            
        }
        
        