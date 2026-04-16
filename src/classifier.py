from transformers import pipeline

class Classifier:
    def __init__(self):
        self.category_classifier = pipeline(
            task="zero-shot-classification",
            model="facebook/bart-large-mnli"
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
        urgency_keywords = [
            "urgent", "critical", "broken", "not working",
            "can't", "cannot", "error", "crash", "failed",
            "down", "emergency", "asap", "immediately"
        ]
        question_lower = question.lower()
        if any(keyword in question_lower for keyword in urgency_keywords):
            return "HIGH"
        return "NORMAL"