# PDF / Notes Summarizer

## Overview
This project is a text-based PDF summarizer built using Python, Streamlit, and a Large Language Model accessed via AIpipe.org.  
It demonstrates how long documents are processed by LLMs using chunking and prompt chaining.

## Features
- Upload a PDF and extract text
- Chunk large documents to handle context limits
- Generate:
  - Overall summary
  - Key bullet points
  - Question & Answer set
- Uses multiple LLM calls (one per chunk + synthesis)

## Supported PDFs
✅ Text-based PDFs (generated from Word, LaTeX, Google Docs, etc.)

❌ Scanned PDFs  
❌ Image-only PDFs  
❌ PDFs where text is embedded as images

This system does **not** use OCR or vision models.  
LLMs only receive extracted text tokens.

## Tech Stack
- Python
- Streamlit
- PyPDF
- AIpipe (OpenAI-compatible API)

## Key Concepts Demonstrated
- Context window limitations
- Recursive chunking with overlap
- Prompt chaining
- Stateless LLM calls
- Why LLMs do not "read" documents

## Architecture
PDF Upload -> Text Extraction (PyPDF) -> Chunking with Overlap -> LLM Call per Chunk -> Intermediate Summaries -> Final Synthesis-> Q&A Generation


## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

