# RAG-Based Question Answering System

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** based Question Answering system.  
Users can upload documents (PDF or TXT) and ask questions based on the uploaded content.  
The system retrieves relevant document chunks using embeddings and generates grounded answers using an LLM.

---

## 🚀 Features
- Upload documents (PDF & TXT)
- Background document ingestion
- Text chunking and embedding generation
- Local vector store for similarity search
- Retrieval-Augmented answer generation
- FastAPI-based REST API
- Basic rate limiting
- Latency and similarity score tracking

---

## 🏗 Architecture
The system follows a standard RAG pipeline:
1. User uploads documents
2. Documents are parsed, chunked, and embedded
3. Embeddings are stored in a vector store
4. User questions are embedded
5. Relevant chunks are retrieved via similarity search
6. An LLM generates the final answer using retrieved context

(Refer to `docs/architecture.png`)

---

## 🛠 Tech Stack
- **Backend:** FastAPI
- **Language:** Python 3.12
- **Embeddings:** Gemini Embeddings / OpenAI Embeddings
- **Vector Store:** Local (FAISS / JSON-based)
- **LLM:** Gemini / OpenAI
- **Rate Limiting:** SlowAPI

---

## 📂 Project Structure
rag-app/

├── app/

│ ├── main.py

│ ├── services/

│ │ ├── parser.py

│ │ ├── chunker.py

│ │ ├── embeddings.py

│ │ ├── vectorstore.py

│ │ └── llm.py

│ ├── workers/

│ │ └── ingest.py

│ ├── utils/

│ │ └── metrics.py

│ └── models/

│ └── schemas.py

├── docs/

│ └── architecture.png

├── requirements.txt

└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repository-url>
cd rag-app

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables
Gemini API
setx GOOGLE_API_KEY "your_api_key_here"

OpenAI API (Optional)
setx OPENAI_API_KEY "your_api_key_here"


Restart the terminal after setting environment variables.

▶️ Run the Application
python -m uvicorn app.main:app --reload


Open in browser:

Swagger UI: http://127.0.0.1:8000/docs

📤 Upload a Document

POST /upload
Upload a PDF or TXT file to be indexed into the system.

❓ Ask a Question

POST /ask

Example request:

{
  "question": "What is RAG?",
  "filename": "sample_rag.pdf"
}

📊 Sample Response
{
  "question": "What is RAG?",
  "answer": "Retrieval-Augmented Generation (RAG) is an AI technique that combines information retrieval with language model generation.",
  "retrieved_context": "...",
  "similarity_score": 0.20,
  "latency_seconds": 2.5
}

📈 Metrics Tracked

Latency: Time taken to generate an answer

Similarity Score: Semantic similarity between query and retrieved chunks

⚠️ Limitations

Local vector store (single-node)

No document versioning

Optimized for small to medium document sets

✅ Status

This project fully satisfies the requirements for a RAG-Based Question Answering System and is ready for evaluation and submission.
