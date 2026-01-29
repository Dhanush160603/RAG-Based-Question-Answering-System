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
