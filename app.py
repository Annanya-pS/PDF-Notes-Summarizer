import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

from pdf_utils import extract_text_from_pdf
from chunking import chunk_text
from prompts import (
    CHUNK_SUMMARY_PROMPT,
    FINAL_SUMMARY_PROMPT,
    QA_PROMPT
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AIPIPE_API_KEY"),
    base_url="https://aipipe.org/openai/v1"
)

st.title("PDF / Notes Summarizer")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("Please upload a text-based PDF to begin.")
    st.stop()

chunk_summaries = []
if uploaded_file:
    raw_text = extract_text_from_pdf(uploaded_file)

    if not raw_text or not raw_text.strip():
    st.error(
        "No extractable text found. "
        "This app supports text-based PDFs only."
    )
    st.stop()

    chunks = chunk_text(raw_text)

    st.write(f"Total chunks: {len(chunks)}")

    

    for i, chunk in enumerate(chunks):
        with st.spinner(f"Summarizing chunk {i+1}/{len(chunks)}"):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": CHUNK_SUMMARY_PROMPT.format(chunk=chunk)
                    }
                ],
                temperature=0.3,
                max_tokens=200
            )

            summary = response.choices[0].message.content
            chunk_summaries.append(summary)

combined_summaries = "\n".join(chunk_summaries)

final_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": FINAL_SUMMARY_PROMPT.format(
                summaries=combined_summaries
            )
        }
    ],
    temperature=0.4,
    max_tokens=500
)

final_output = final_response.choices[0].message.content
st.subheader("Summary & Key Points")
st.write(final_output)

qa_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": QA_PROMPT.format(
                summary=final_output
            )
        }
    ],
    temperature=0.5,
    max_tokens=400
)

st.subheader("Q&A")
st.write(qa_response.choices[0].message.content)
