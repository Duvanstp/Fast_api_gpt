import subprocess
import os

from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv


load_dotenv()

import openai

# bash_cod = 'set OPENAI_API_KEY="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"'
# subprocess.run(bash_cod , shell=True)

api_key = os.getenv('OPENAI_API_KEY')

print("Valor de OPENAI_API_KEY:", api_key)

openai.api_key = api_key
from openai import OpenAI

app = FastAPI()



client = OpenAI()
class Prompt(BaseModel):
    text: str = Field(min_length=10, max_length=100)

@app.post('/chat')
def generate_response(prompt: Prompt):
    text_length = 1000
    gpt3_model = 'gpt-3.5-turbo'

    completion = client.chat.completions.create(
        model = gpt3_model,
        messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt.text}
            ],
        max_tokens = text_length,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    # response = openai.Completion.create(
    #     engine = gpt3_model,
    #     prompt = prompt.text,
    #     max_tokens = text_length,
    #     n = 1,
    #     stop = None,
    #     temperature = 0.5
    # )
    return completion.choices[0].message