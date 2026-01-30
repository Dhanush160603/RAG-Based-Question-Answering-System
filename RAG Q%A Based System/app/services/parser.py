import os
from PyPDF2 import PdfReader

def parse_file(file_path: str) -> str:
    """
    Parse TXT or PDF files and return extracted text
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return _parse_txt(file_path)

    elif ext == ".pdf":
        return _parse_pdf(file_path)

    else:
        raise ValueError("Unsupported file format")


def _parse_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def _parse_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    return text
