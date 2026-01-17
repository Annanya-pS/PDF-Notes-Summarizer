CHUNK_SUMMARY_PROMPT = """
You are given a part of a document.

Summarize this chunk clearly and concisely.
Focus only on factual content.

Chunk:
{chunk}
"""

FINAL_SUMMARY_PROMPT = """
You are given summaries of multiple chunks from a document.

Combine them into:
1. A coherent overall summary
2. 5–8 key bullet points

Chunk summaries:
{summaries}
"""

QA_PROMPT = """
Based on the following document summary, generate:
- 5 important questions
- Their accurate answers

Document summary:
{summary}
"""
