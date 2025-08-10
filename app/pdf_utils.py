# app/pdf_utils.py

import requests
from PyPDF2 import PdfReader
from io import BytesIO

def extract_text_from_pdf_url(pdf_url: str) -> str:
    response = requests.get(pdf_url)
    response.raise_for_status()

    reader = PdfReader(BytesIO(response.content))
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text
