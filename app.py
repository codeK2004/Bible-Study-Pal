import streamlit as st
from rag import ask_gemini

st.set_page_config(page_title="Bible Study Pal", layout="centered")

st.title("📖 Bible Study Pal")
st.caption("New Testament Commentary Based Q&A (RAG)")

question = st.text_input("Ask a Bible question:")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Searching scripture commentary..."):
            answer = ask_gemini(question)
        st.markdown("### 🧠 Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
