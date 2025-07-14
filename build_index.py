# File: scripts/build_index.py
import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
INDEX_PATH = "data/vector_store/index.faiss"
DOCS_PATH = "data/vector_store/docs.json"
CHUNKS_FILE = "data/processed_chunks.json"

model = SentenceTransformer(EMBED_MODEL)

with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

texts = [chunk["content"] for chunk in chunks]
embeddings = model.encode(texts, show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(np.array(embeddings))

faiss.write_index(index, INDEX_PATH)

with open(DOCS_PATH, "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print("Index built and saved.")