import faiss
import pickle
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("index/faiss.index")
chunks = pickle.load(open("index/chunks.pkl", "rb"))

def retrieve_context(query, k=6):
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k)
    return "\n".join([chunks[i] for i in indices[0]])

def ask_gemini(question):
    context = retrieve_context(question)

    prompt = f"""
You are a Bible Study assistant.

Use ONLY the commentary excerpts below to answer.
Explain clearly and theologically.
If the commentary is insufficient, say so honestly.

COMMENTARY EXCERPTS:
{context}

QUESTION:
{question}
"""

    llm = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = llm.generate_content(prompt)
    return response.text
