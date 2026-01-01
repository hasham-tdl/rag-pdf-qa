📘 PDF-Based Retrieval-Augmented Generation (RAG)

A fully local Retrieval-Augmented Generation (RAG) system that allows natural-language querying of a PDF using Ollama, FAISS, and LangChain.

This project demonstrates how to:

Ingest and chunk structured PDFs

Embed text locally using Ollama

Store and search embeddings with FAISS

Generate grounded answers using an LLM

🚀 Features

📄 PDF ingestion via PyMuPDF

🧠 Semantic search using FAISS

🔗 Retrieval-Augmented Generation (RAG)

🤖 Local embeddings + LLMs via Ollama

🛑 Hallucination control via prompt grounding

💻 Runs fully offline after setup

🏗️ Project Architecture
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

📂 Project Structure
rag-pdf-qa/
├── ingest.py     # PDF ingestion + FAISS index creation
├── query.py      # Query-time RAG pipeline
├── data/         # PDF input (ignored in git)
├── index/        # FAISS index (ignored in git)

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/hasham-tdl/rag-pdf-qa.git
cd rag-pdf-qa

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Install & run Ollama

Download Ollama from https://ollama.com

Pull required models:

ollama pull nomic-embed-text
ollama pull llama3.1

5. Add your PDF
data/book.pdf

6. Build the index
python ingest.py

7. Query the document
python query.py

🧠 Example Query
Ask a question:
> What is OAuth authentication?

Answer:
OAuth is an authorization framework that...

🧪 Models Used
Purpose	Model
Embeddings	nomic-embed-text
LLM	llama3.1
📌 Notes

The system answers only using retrieved PDF content

If an answer is not found, it responds accordingly

Chunking is optimized for QA-style documents

🔮 Future Improvements

Source citations in answers

Streaming responses

UI with Streamlit

Multi-PDF support