import os
from google import genai

# Create Gemini client using API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(question: str, context: str) -> str:
    if not context.strip():
        return "Answer not found in document."

    prompt = f"""
Using the context below, answer the question as accurately as possible.
If the context is partially relevant, summarize what can be inferred.
If the answer is completely missing, say "Answer not found in document".

Context:
{context}

Question:
{question}
"""


    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text.strip()
