from backend.api.routes import *
from backend.config import OLLAMA_HOST, OLLAMA_MODEL
from backend.services.llm import generate_response
from backend.models import ChatRequest
from backend.services.handle import handle_command

import time

stopgeneration = False




