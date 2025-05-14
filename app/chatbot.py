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
            {
                "role": "system",
                "content": "You are an AI specialized in generating Manim (Mathematical Animation Library) code. "
                        "Your role is to create accurate and functional Manim scripts based on user-provided topics. "
                        "Follow these rules strictly:\n"
                        "1. Only generate Manim code (Python) for mathematical/algorithmic visualizations\n"
                        "2. Ensure the code is complete, error-free, and uses Manim CE (Community Edition) syntax\n"
                        "3. After providing the code, add numbered steps to run the program\n"
                        "4. Format response: first the code in ```python block, then 'Steps to Run:' section\n"
                        "5. If the request is unclear or not feasible for Manim, clarify but still provide best-attempt code"
            },
            {
                "role": "user",
                "content": content
            },
        ],
        temperature=0.0,
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

def chatbot_response(text):
    return response_generator(text)