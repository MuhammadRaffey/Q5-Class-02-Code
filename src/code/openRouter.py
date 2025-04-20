import requests
import json
import os
from dotenv import load_dotenv,find_dotenv


_=load_dotenv(find_dotenv())

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if OPENROUTER_API_KEY is None:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables.")



BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "meta-llama/llama-4-maverick:free"

response = requests.post(
  url=f"{BASE_URL}/chat/completions",
  headers={
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
  },
  data=json.dumps({
    "model": MODEL,
    "messages": [
      {
        "role": "user",
        "content": "Tell me about recursion in programming."
      }
    ]
  })
)

# print(response.json())

data = response.json()
with open("result.json", "w") as f:
    f.write(json.dumps(data, indent=4))
# content = data['choices'][0]['message']['content']
# print(content)