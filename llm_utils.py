# 📌 llm_utils.py — Uses OpenAI to generate Hindglish replies

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_reply(user_input):
    # 💬 Prompt with friendly chatbot tone
    prompt = f"""
You are a helpful assistant that replies in friendly Hindglish.
User: {user_input}
Assistant:"""

    # 🔧 Optional: Add custom instructions here if needed later

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot who replies in Hindglish."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=150,
        temperature=0.7
    )

    return response.choices[0].message["content"].strip()
