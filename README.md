
# 📖 Bible Study Pal

Bible Study Pal is a **Retrieval-Augmented Generation (RAG)** based Bible study assistant built with **Python** and **Streamlit**.  
It enables users to ask questions based on **New Testament Bible commentary / interpretation content** and generates contextual answers using a Large Language Model.

This project is in its **early development stage** and was created to learn RAG concepts without using frameworks like LangChain.

---

## 🚀 Features

- Bible commentary ingestion (PDF / TXT)
- Text chunking and embeddings
- Semantic search using FAISS
- Context-aware answers using Gemini (Flash-Lite)
- Simple Streamlit-based UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- FAISS
- sentence-transformers
- Google Gemini (Flash-Lite)
- PyPDF2

---

## ▶️ Run Locally

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
````

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Notes:

* Early-stage prototype; responses may be inaccurate
* Built for learning 

