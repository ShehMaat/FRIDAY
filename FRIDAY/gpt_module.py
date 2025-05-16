# gpt_module.py

import openai
from config import OPENAI_API_KEY
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        return "Sorry, I couldn't connect to OpenAI at the moment."
