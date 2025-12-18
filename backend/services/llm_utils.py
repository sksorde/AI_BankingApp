import os
import json
from ollama import Ollama

client = Ollama()

CACHE_FILE = os.path.join(os.path.dirname(__file__), "llm_cache.json")
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
else:
    cache = {}

def get_llm_response(prompt: str):
    if prompt in cache:
        return cache[prompt]
    response = client.completions.create(model="llama3", prompt=prompt, max_tokens=50)
    cache[prompt] = response.text
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)
    return response.text
