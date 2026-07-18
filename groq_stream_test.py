import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Load .env from backend folder
env_path = Path(__file__).parent / "backend" / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("MODEL_NAME")

print("=" * 60)
print("Groq Streaming Test")
print("=" * 60)
print("Env File :", env_path)
print("API Key Loaded :", api_key is not None)
print("Model :", model)
print()

client = Groq(api_key=api_key)

stream = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Explain what Velar is in about 100 words."
        }
    ],
    temperature=0,
    stream=True,
)

print("Streaming Response:\n")

for chunk in stream:

    if chunk.choices:

        delta = chunk.choices[0].delta.content

        if delta:
            print(delta, end="", flush=True)

print("\n\nFinished!")