from fastapi import FastAPI

from config import OLLAMA_HOST, OLLAMA_MODEL
from llm import generate_response
from handle import handle_command

from models import Request


from fastapi.middleware.cors import (
    CORSMiddleware,
)
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
from pathlib import Path


import time

stopgeneration = False

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


FRONTEND = Path(__file__).parent.parent / "frontend" / "UI.html"


@app.get("/")
def home():
    return FileResponse(FRONTEND)


@app.post("/chat")
def chat(req: Request):
    return StreamingResponse(generate_response(req.message), media_type="text/plain")


@app.get("/health")
def health():
    return {"status": "healthy", "service": "Jarvis", "server": "Edith"}


@app.post("/stop")
def stop():
    global stop_generation
    stop_generation = True
    return {"status": "stopped"}
