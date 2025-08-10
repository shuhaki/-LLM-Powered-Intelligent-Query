import os
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, Header
from pydantic import BaseModel

from app.pdf_utils import extract_text_from_pdf_url
from app.embed_utils import embed_and_search_chunks
from app.llm_utils import query_llm

app = FastAPI()

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # ✅ Now this loads from .env

if not openai.api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Please set it in the .env file.")

print("🔑 API Key Loaded:", openai.api_key[:8] + "********")  # Safe logging

class HackRxRequest(BaseModel):
    documents: str
    questions: list[str]

@app.post("/hackrx/run")
async def run_hackrx(request: HackRxRequest, authorization: str = Header(...)):
    try:
        pdf_text = extract_text_from_pdf_url(request.documents)
        answers = []

        for question in request.questions:
            top_chunks = embed_and_search_chunks(pdf_text, question)
            answer = query_llm(question, top_chunks)
            answers.append(answer)

        return {"answers": answers}

    except Exception as e:
        return {"error": str(e)}
