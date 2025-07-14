# File: scripts/query_engine.py
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import subprocess

INDEX_PATH = "data/vector_store/index.faiss"
DOCS_PATH = "data/vector_store/docs.json"
EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

model = SentenceTransformer(EMBED_MODEL)
index = faiss.read_index(INDEX_PATH)
with open(DOCS_PATH, "r", encoding="utf-8") as f:
    documents = json.load(f)

def query_local_llm(prompt):
    # Replace this with actual LLM call (llama.cpp or GPT4All)
    result = subprocess.run(["echo", f"[LLM] Answering: {prompt}"], capture_output=True, text=True)
    return result.stdout.strip()

def search_and_answer(query, top_k=5):
    embedding = model.encode([query])
    D, I = index.search(np.array(embedding), top_k)
    context = "\n".join([documents[i]['content'] for i in I[0]])
    full_prompt = f"Answer the question based on the following scripture context:\n{context}\n\nQuestion: {query}"
    return query_local_llm(full_prompt)

if __name__ == "__main__":
    while True:
        q = input("Ask (type 'exit' to quit): ")
        if q.lower() == "exit":
            break
        print(search_and_answer(q))