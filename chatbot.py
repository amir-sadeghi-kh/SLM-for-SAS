import openai


def query_ollama(prompt):
    
    client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
    )

    response = client.chat.completions.create(
        model="llama3.1",
        temperature=0.7,
        n=1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        )
    
    return response.choices[0].message.content


response = query_ollama("Hi")

print(response)

