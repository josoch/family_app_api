from fastapi import FastAPI
from typing import List
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK"}

@app.get("/income")
def read_income() -> List[dict]:
    with open("data.json", "r") as f:
        data = json.load(f)
    return data["income"]

@app.get("/expense")
def read_expense() -> List[dict]:
    with open("data.json", "r") as f:
        data = json.load(f)
    return data["expense"]