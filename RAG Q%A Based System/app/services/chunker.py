def chunk_text(text, chunk_size=3):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    chunks = []

    for i in range(0, len(lines), chunk_size):
        chunks.append(" ".join(lines[i:i + chunk_size]))

    return chunks
