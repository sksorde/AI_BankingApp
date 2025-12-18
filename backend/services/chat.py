
import ollama

def chat_llm(prompt: str):
    res = ollama.chat(model="llama3", messages=[{"role":"user","content":prompt}])
    return res["message"]["content"]
