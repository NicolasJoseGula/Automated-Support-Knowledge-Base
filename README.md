# Automated Support Knowledge Base

An AI-powered support system that allows users to upload documents and get instant answers, automatic categorization, urgency detection, and document summaries — all powered by Hugging Face Transformers.

---

## Features

- **Question Answering** — Ask natural language questions and get precise answers extracted from your documents
- **Auto Categorization** — Automatically classifies each question into a support category (billing, technical, account, etc.)
- **Urgency Detection** — Detects the sentiment of the user's question to flag high-priority requests
- **Document Summarization** — Generates concise summaries of loaded documents
- **Multi-document Support** — Load multiple PDFs and search across all of them

---

## Tech Stack

| Component | Technology |
|---|---|
| NLP Pipelines | Hugging Face Transformers |
| Question Answering | `distilbert-base-cased-distilled-squad` |
| Categorization | `facebook/bart-large-mnli` (zero-shot) |
| Sentiment / Urgency | `distilbert-base-uncased-finetuned-sst-2-english` |
| Summarization | `cnicu/t5-small-booksum` |
| PDF Extraction | PyPDF |
| UI | Gradio |

---

## Project Structure

```
automated-support-kb/
├── app.py                    # Gradio UI — entry point
├── requirements.txt
├── src/
│   ├── document_processor.py # PDF extraction and text chunking
│   ├── knowledge_base.py     # Document store and relevance search
│   ├── qa_engine.py          # Question answering pipeline
│   ├── classifier.py         # Category and urgency classification
│   └── summarizer.py         # Document summarization pipeline
└── documents/                # Place your PDF files here
```

---

## How It Works

1. **Ingest** — PDFs are loaded and split into overlapping chunks of ~400 words
2. **Search** — When a question is asked, the most relevant chunk is retrieved using keyword matching
3. **Answer** — The QA model extracts a precise answer from that chunk
4. **Classify** — The question is categorized using zero-shot classification and flagged for urgency based on sentiment

---

## Installation

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Then open your browser at `http://localhost:7860`

---

## Skills Demonstrated

- Hugging Face `pipeline()` API for multiple NLP tasks
- `AutoTokenizer` and `AutoModel` integration
- PDF text extraction with PyPDF
- Text chunking with overlap for context preservation
- Zero-shot classification without task-specific training
- Multi-component AI system design
- Interactive UI with Gradio
