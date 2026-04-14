from transformers import pipeline

class Summarizer:
    def __init__(self):
        self.pipeline = pipeline(
            task="summarization",
            model="cnicu/t5-small-booksum"
        )
        
    def summarize(self, text: str, min_tokens: int = 50, max_tokens: int = 150) -> str:
        if not text:
            return "No document text provided."
        
        max_input_words = 800
        words = text.split()
        if len(words) > max_input_words:
            text = " ".join(words[:max_input_words])
            
        result = self.pipeline(
            text,
            min_new_tokens=min_tokens,
            max_new_tokens=max_tokens
        )
        
        return result[0]["summary_text"]