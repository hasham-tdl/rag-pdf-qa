import fitz  # PyMuPDF
import re
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


# -----------------------------
# CONFIG
# -----------------------------

PDF_PATH = "data/book.pdf"
INDEX_PATH = "index/book_faiss"



# -----------------------------
# PDF TEXT EXTRACTION
# -----------------------------

def extract_text(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        page_text = page.get_text()
        if page_text:
            text += page_text + "\n"

    return text


# -----------------------------
# QUESTION-BASED CONTEXTUAL CHUNKING (NOVEL-TUNED)
# -----------------------------

def chunk_text(text: str) -> List[str]:
    chunks = []

    # Normalize newlines
    text = re.sub(r"\r\n", "\n", text)

    # Split into lines for easier parsing
    lines = text.split("\n")

    current_chunk = []
    in_answer = False

    for line in lines:
        line_stripped = line.strip()

        # Start of a new question
        if line_stripped.startswith("Q:"):
            # Save previous chunk if it exists
            if current_chunk:
                chunks.append("\n".join(current_chunk).strip())
                current_chunk = []

            current_chunk.append(line)
            in_answer = False
            continue

        # Start of answer
        if line_stripped.startswith("A:") and current_chunk:
            current_chunk.append(line)
            in_answer = True
            continue

        # Collect answer lines until paragraph ends
        if in_answer:
            if line_stripped == "":
                # Blank line → end of answer paragraph
                chunks.append("\n".join(current_chunk).strip())
                current_chunk = []
                in_answer = False
            else:
                current_chunk.append(line)

    # Catch any trailing chunk
    if current_chunk:
        chunks.append("\n".join(current_chunk).strip())

    return chunks
# -----------------------------
# FAISS INDEX CREATION
# -----------------------------

def create_faiss_index(chunks: List[str]):
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    vectorstore.save_local(INDEX_PATH)


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":
    print("Extracting text from PDF...")
    text = extract_text(PDF_PATH)

    print("Chunking text by paragraph...")
    chunks = chunk_text(text)

    print(f"Chunks created: {len(chunks)}")
    print(f"Largest chunk size: {max(len(c) for c in chunks)} characters")

    print("Creating FAISS index with Ollama embeddings...")
    create_faiss_index(chunks)

    print("FAISS index created and saved successfully.")
