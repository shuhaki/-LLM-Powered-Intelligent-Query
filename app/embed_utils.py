from openai import OpenAI
import chromadb

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("docs")

def embed_and_search_chunks(text, query):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    ids = [f"id_{i}" for i in range(len(chunks))]
    embeddings = [client.embeddings.create(input=[chunk], model="text-embedding-ada-002").data[0].embedding for chunk in chunks]

    collection.upsert(documents=chunks, embeddings=embeddings, ids=ids)
    query_embed = client.embeddings.create(input=[query], model="text-embedding-ada-002").data[0].embedding
    results = collection.query(query_embeddings=[query_embed], n_results=3)
    return results["documents"][0]
