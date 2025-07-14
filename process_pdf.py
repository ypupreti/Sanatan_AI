# File: scripts/process_pdfs.py
import os
import fitz  # PyMuPDF
from pathlib import Path
import json

CHUNK_SIZE = 500  # Tokens or words approx.

def extract_text_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for i, page in enumerate(doc):
        text = page.get_text()
        words = text.split()
        for j in range(0, len(words), CHUNK_SIZE):
            chunk_text = " ".join(words[j:j+CHUNK_SIZE])
            chunks.append({
                "content": chunk_text,
                "metadata": {
                    "source": pdf_path.name,
                    "page": i + 1
                }
            })
    return chunks

def process_all_pdfs(pdf_dir, output_file):
    all_chunks = []
    for pdf in Path(pdf_dir).glob("*.pdf"):
        print(f"Processing {pdf}")
        chunks = extract_text_chunks(pdf)
        all_chunks.extend(chunks)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_all_pdfs("data/pdfs", "data/processed_chunks.json")
