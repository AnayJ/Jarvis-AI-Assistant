from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.models import ChatRequest
from backend.services.llm import generate_response
import backend.services.state as state

router = APIRouter()


@router.post("/chat")
def chat(req: ChatRequest):
    state.stop_generation = False

    return StreamingResponse(
        generate_response(req.message),
        media_type="text/plain"
    )


@router.post("/stop")
def stop():
    state.stop_generation = True
    return {"status": "stopped"}