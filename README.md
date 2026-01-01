# 📘 PDF-Based Retrieval-Augmented Generation (RAG)

A fully **local Retrieval-Augmented Generation (RAG)** system that enables natural-language querying of PDFs using **Ollama**, **FAISS**, and **LangChain**.

This project demonstrates how to:

- 📄 Ingest and chunk structured PDFs  
- 🧠 Generate embeddings locally using Ollama  
- 🔍 Store and retrieve vectors with FAISS  
- 🤖 Produce grounded answers using a local LLM  

---

## 🚀 Features

- 📄 PDF ingestion via **PyMuPDF**
- 🧠 Semantic search using **FAISS**
- 🔗 Retrieval-Augmented Generation (RAG) pipeline
- 🤖 Local embeddings and LLMs via **Ollama**
- 🛑 Reduced hallucinations through prompt grounding
- 💻 Fully **offline** after initial setup

---

## 🏗️ Project Architecture

User Question  
↓  
Embedding (nomic-embed-text)  
↓  
FAISS Vector Search  
↓  
Relevant PDF Chunks  
↓  
LLM (llama3.1)  
↓  
Grounded Answer  

---

## 📂 Project Structure

rag-pdf-qa/  
├── ingest.py        # PDF ingestion & FAISS index creation  
├── query.py         # Query-time RAG pipeline  
├── data/            # PDF inputs (git-ignored)  
└── index/           # FAISS index files (git-ignored)  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
git clone https://github.com/hasham-tdl/rag-pdf-qa.git  
cd rag-pdf-qa  

### 2️⃣ Create and activate a virtual environment
python -m venv venv  
venv\Scripts\activate  

### 3️⃣ Install dependencies
pip install -r requirements.txt  

### 4️⃣ Install & run Ollama

Download Ollama from:  
https://ollama.com  

Pull the required models:
- ollama pull nomic-embed-text  
- ollama pull llama3.1  

### 5️⃣ Add your PDF
data/book.pdf  

### 6️⃣ Build the FAISS index
python ingest.py  

### 7️⃣ Query the document
python query.py  

---

## 🧠 Example Query

Ask a question:  
> What is OAuth authentication?  

OAuth is an authorization framework that...  

---

## 🧪 Models Used

Purpose: Embeddings — nomic-embed-text  
Purpose: LLM — llama3.1  

---

## 📌 Notes

- Answers are generated **only from retrieved PDF content**
- If relevant information is not found, the system responds accordingly
- Chunking strategy is optimized for QA-style documents
- Designed for **local, private, and offline** usage
