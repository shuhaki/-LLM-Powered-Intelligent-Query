from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

def query_llm(question, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"Use the below document to answer the question:\n\n{context}\n\nQ: {question}\nA:"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
