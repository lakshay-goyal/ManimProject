from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
ai_api_key = os.getenv("AI_API_KEY")

client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")

def response_generator(content):
    stream = client.chat.completions.create(
        model="deepseek-r1:8b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": content},
        ],
        max_tokens=1024,
        temperature=0.7,
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

def chatbot_response(text):
    return response_generator(text)