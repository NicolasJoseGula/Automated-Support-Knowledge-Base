import gradio as gr
from src.document_processor import process_document
from src.knowledge_base import KnowledgeBase
from src.qa_engine import QAEngine
from src.classifier import Classifier
from src.summarizer import Summarizer

kb = KnowledgeBase()
qa_engine = QAEngine()
classifier = Classifier()
summarizer = Summarizer()

def load_document(file):
    if file is None:
        return "No file is uploaded.", []
    
    message = kb.add_document(file.name)
    return message, kb.list_documents()

def ask_question(question):
    if not question.strip():
        return "", "", "", ""
    
    context = kb.find_relevant_chunk(question)
    qa_result = qa_engine.answer(question, context)
    category_result = classifier.categorize(question)
    urgency = classifier.detect_urgency(question)
    
    answer = qa_result["answer"]
    confidence = f"{qa_result['score'] * 100:.1f}%"
    category = f"{category_result['category']} ({category_result['score'] * 100:.1f}%)"
    
    return answer, confidence, category, urgency

def summarize_document(file_name):
    if not file_name:
        return "Select a document to summarize."
    
    for doc in kb.documents:
        if doc["file_name"] == file_name:
            return summarizer.summarize(doc["full_text"])
        
    return "Document not found."

with gr.Blocks(title="Automated Support Knowledge Base") as app:
    
    gr.Markdown("# Automated Support Knowledge Base")
    gr.Markdown("Upload support documents and ask questions about them.")
    
    with gr.Tab("Documents"):
        gr.Markdown("### Upload Documents")
        file_input = gr.File(label="Upload PDF", file_types=[".pdf"])
        upload_btn = gr.Button("Load Document", variant="primary")
        upload_output = gr.Texbox(label="Status")
        doc_list = gr.Dropdown(label="Loaded Documents", choices=[], interactive=False)
        
        upload_btn.click(
            fn=load_document,
            inputs=file_input,
            outputs=[upload_output, doc_list]
        )
        
    with gr.Tab("Ask a question"):
        gr.Markdown("### Ask anything about your documents")
        question_input = gr.Textbox(label="Your Question", placeholder="e.g. What is the return policy?")
        ask_btn = gr.Button("Ask", variant="primary")
        
        with gr.Row():
            answer_output = gr.Textbox(label="Answer")
            confidence_output = gr.Textbox(label="Confidence")

        with gr.Row():
            category_output = gr.Textbox(label="Category")
            urgency_output = gr.Textbox(label="Urgency")

        ask_btn.click(
            fn=ask_question,
            inputs=question_input,
            outputs=[answer_output, confidence_output, category_output, urgency_output]
        )

    with gr.Tab("Summarize"):
        gr.Markdown("### Get a summary of a loaded document")
        doc_selector = gr.Dropdown(label="Select Document", choices=[])
        summarize_btn = gr.Button("Summarize", variant="primary")
        summary_output = gr.Textbox(label="Summary", lines=6)

        summarize_btn.click(
            fn=summarize_document,
            inputs=doc_selector,
            outputs=summary_output
        )
        
if __name__ == "__main__":
    app.launch()