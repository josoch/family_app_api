from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"status": "OK"}

@app.get("/income")
def read_income() -> List[dict]:
    with open("api.json", "r") as f:
        data = json.load(f)
    return data["income"]

@app.get("/expense")
def read_expense() -> List[dict]:
    with open("api.json", "r") as f:
        data = json.load(f)
    return data["expense"]

@app.get("/budget")
def read_user() -> List[dict]:
    with open("api.json", "r") as f:
        data = json.load(f)
    return data["budget"]

@app.get("/user")
def read_user() -> List[dict]:
    with open("api.json", "r") as f:
        data = json.load(f)
    return data["user"]
