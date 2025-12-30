# 📖 Bible Study Pal

Bible Study Pal is a simple RAG-based Bible study assistant built using Python and Streamlit.
It allows users to ask questions based on New Testament Bible commentary PDFs, retrieves relevant passages using embeddings and FAISS, and generates contextual answers using Gemini (Flash-Lite).

This project is in its early development stage and was built as a learning exercise to understand how Retrieval-Augmented Generation (RAG) works without using heavy frameworks like LangChain.

## 🚀 Features

Upload Bible commentary / interpretation PDFs
Chunking and embedding of text using sentence-transformers
Vector storage and similarity search using FAISS
Context-aware answers generated using Gemini LLM
Simple and clean UI built with Streamlit
Focused specifically on Bible study (New Testament)

## How It Works

PDF Ingestion
Bible commentary PDFs are read and converted into text.

Text Chunking & Embeddings
Text is split into chunks and converted into vector embeddings.

Vector Search (FAISS)
Relevant chunks are retrieved based on user questions.

Answer Generation (Gemini)
Retrieved context is passed to Gemini to generate a meaningful response.

## 🛠️ Tech Stack

Python
Streamlit – UI
FAISS – Vector database
sentence-transformers – Embeddings
Google Gemini (Flash-Lite) – LLM
PyPDF2 – PDF processing


## Setup Instructions
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

## Note:
This project is built for learning and experimentation purposes.
Contributions, suggestions, and improvements are welcome.




