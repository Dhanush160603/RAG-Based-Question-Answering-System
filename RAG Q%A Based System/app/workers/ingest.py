from app.services.parser import parse_file
from app.services.chunker import chunk_text
from app.services.embeddings import embed_text
from app.services.vectorstore import save_embeddings

def ingest_document(file_path: str, filename: str):
    """
    Background job to ingest documents:
    parse → chunk → embed → store
    """
    text = parse_file(file_path)
    chunks = chunk_text(text)

    for chunk in chunks:
        embedding = embed_text(chunk)
        save_embeddings(filename, chunk, embedding)
