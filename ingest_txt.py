import faiss
import pickle
from sentence_transformers import SentenceTransformer

TXT_PATH = "data/bible_commentary.txt"

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def chunk_text(text, chunk_size=220, overlap=50):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start += chunk_size - overlap

    return chunks

def main():
    print("Reading TXT file...")
    text = read_txt(TXT_PATH)

    print("Chunking text...")
    chunks = chunk_text(text)

    print("Creating embeddings...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)

    print("Saving FAISS index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, "index/faiss.index")
    with open("index/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("TXT ingestion complete!")

if __name__ == "__main__":
    main()
