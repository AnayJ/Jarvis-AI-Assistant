from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware,
)
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
from pathlib import Path
from backend.services.llm import generate_response
from backend.services.handle import handle_command
from backend.models import ChatRequest

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
def chat(req: ChatRequest):

    return StreamingResponse(generate_response(req.message), media_type="text/plain")


@app.post("/command")
def command(req: ChatRequest):

    result = handle_command(req.message)

    if result:
        return {"handled": True, **result}

    return {"handled": False}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "Jarvis", "server": "Edith"}


@app.post("/stop")
def stop():
    global stop_generation
    stop_generation = True
    return {"status": "stopped"}
