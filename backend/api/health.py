from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

FRONTEND = Path(__file__).parent.parent.parent / "frontend" / "UI.html"

@router.get("/")
def home():
    return FileResponse(FRONTEND)

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Jarvis",
        "server": "Edith"
    }