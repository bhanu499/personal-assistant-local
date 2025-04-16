import os
import yaml
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from llm_backends.openai_backend import OpenAIBackend
from llm_backends.local_backend import LocalLLMBackend

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load model and LLM backend
embedder = SentenceTransformer("all-MiniLM-L6-v2")
if config["llm_backend"] == "openai":
    llm = OpenAIBackend(api_key=config["openai_api_key"])
elif config["llm_backend"] == "local":
    llm = LocalLLMBackend(
    base_url=config["local_llm_url"],
    model=config.get("local_llm_model", "deepseek-r1:1.5b")
)
else:
    raise ValueError("Unknown LLM backend")

# Load notes
with open("notes/my_notes.txt", "r", encoding="utf-8") as f:
    notes_text = f.read()

# Chunk and embed notes
chunks = [notes_text[i:i+500] for i in range(0, len(notes_text), 500)]
embeddings = embedder.encode(chunks)
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

# User query loop
print("Ask me anything about your notes (type 'exit' to quit)")
while True:
    query = input("\n> ")
    if query.lower() == "exit":
        break
    query_embed = embedder.encode([query])
    D, I = index.search(np.array(query_embed), k=3)
    relevant_chunks = "\n\n".join([chunks[i] for i in I[0]])
    prompt = f"Use the following notes to answer the question:\n\n{relevant_chunks}\n\nQ: {query}\nA:"
    answer = llm.answer(prompt)
    print("\n" + answer)
