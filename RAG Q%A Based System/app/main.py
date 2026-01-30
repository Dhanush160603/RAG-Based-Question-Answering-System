import os
import time
import PyPDF2

from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

from app.api.upload import router
from app.models.schemas import AskRequest
from app.config import UPLOAD_FOLDER
from app.services.chunker import chunk_text
from app.services.embeddings import text_to_vector, cosine_similarity
from app.services.vectorstore import add_vectors, search_vectors
from app.services.llm import generate_answer
from fastapi import Request


app = FastAPI(title="RAG-Based Question Answering System")

# Rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "RAG API running"}

@limiter.limit("5/minute")
@app.post("/ask")
def ask_question(request: Request, payload: AskRequest):

    start = time.time()

    file_path = os.path.join(UPLOAD_FOLDER, payload.filename)
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    # Read document
    if payload.filename.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""

    # Chunk + embed + store
    chunks = chunk_text(text)
    add_vectors(chunks, text_to_vector)

    # Retrieve
    question_vec = text_to_vector(payload.question)
    result = search_vectors(question_vec, cosine_similarity)

    # LLM generation
    answer = generate_answer(payload.question, result["text"])

    return {
        "question": payload.question,
        "answer": answer,
        "retrieved_context": result["text"],
        "similarity_score": round(result["score"], 3),
        "latency_seconds": round(time.time() - start, 3)
    }
