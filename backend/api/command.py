from fastapi import APIRouter

from backend.models import ChatRequest
from backend.services.handle import handle_command

router = APIRouter()

@router.post("/command")
def command(req: ChatRequest):

    result = handle_command(req.message)

    if result:
        return {
            "handled": True,
            **result
        }

    return {
        "handled": False
    }