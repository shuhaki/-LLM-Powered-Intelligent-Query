# LLM Document Processing System

## Overview
The LLM Document Processing System is a MERN + FastAPI based solution for intelligent document query and retrieval. It allows users to upload unstructured documents, ask natural language questions, and receive structured, explainable answers with supporting references.

## Tech Stack
- **Frontend:** React.js
- **Backend API:** Node.js + Express
- **AI Microservice:** FastAPI (Python)
- **Database:** MongoDB
- **Testing:** Postman Mock Server
- **AI Models:** Embeddings + LLMs

## Features
- Upload PDFs, DOCX, and email text
- Extract and embed document text
- Perform semantic search using embeddings
- Return structured responses with clause references
- Store documents & query history in MongoDB
- Interactive and responsive React UI

## Setup
1. Clone the repository
2. Install dependencies for backend (`npm install`) and frontend (`npm install`)
3. Set up `.env` with MongoDB URI and API keys
4. Start the backend (`npm run dev`) and frontend (`npm start`)
5. Run FastAPI service (`uvicorn main:app --reload`)

## API Endpoints
- `POST /upload` – Upload a document
- `POST /embed` – Generate embeddings
- `POST /query` – Answer user queries
- `GET /history` – Retrieve query/document history

## License
MIT License
