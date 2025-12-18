
from fastapi import FastAPI
from services.otp import verify_otp
from services.chat import chat_llm
from services.summary import summarize_transactions
from services.llm_utils import get_llm_response
import pandas as pd
import os

app = FastAPI()

# current file: backend/api/main.py
API_DIR = os.path.dirname(os.path.abspath(__file__))        # backend/api
BACKEND_DIR = os.path.dirname(API_DIR)                      # backend
PROJECT_ROOT = os.path.dirname(BACKEND_DIR)                 # project root

csv_path = os.path.join(PROJECT_ROOT, "data", "mock", "transactions.csv")

print("Resolved CSV path:", csv_path)
print("CSV exists:", os.path.exists(csv_path))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/chat")
def chat(q: str):
    return {"reply": get_llm_response(q)}

@app.post("/otp")
def otp(code: str):
    return verify_otp(code)


@app.get("/summary")
def summary():
    #df = pd.read_csv("data/mock/transactions.csv")
    df = pd.read_csv(csv_path)
    return {"summary": summarize_transactions(df)}

@app.get("/deb")
def deb():
    try:
        return {
            "base_dir": str(PROJECT_ROOT),
            "csv_path": str(csv_path),
            "file_exists": os.path.exists(csv_path)
        }
    except Exception as e:
        return {"error": str(e)}
