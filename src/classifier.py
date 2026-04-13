from transformers import pipeline

class Classifier:
    def __init__(self):
        self.category_classifier = pipeline(
            task="zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        self.sentiment_classifier = pipeline(
            task="text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    
    def categorize(self, question: str) -> dict:
        categories = [
            "billing and payments",
            "technical support",
            "account management",
            "product information",
            "shipping and delivery"
        ]

        result = self.category_classifier(question, categories)

        return {
            "category": result["labels"][0],
            "score": round(result["scores"][0], 4)
        }
        
    def detect_urgency(self, question: str) -> str:
        result = self.sentiment_classifier(question)
        label = result[0]["label"]

        if label == "NEGATIVE":
            return "HIGH"
        return "NORMAL"