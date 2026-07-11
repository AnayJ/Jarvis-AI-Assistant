import os
import ollama

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://172.20.0.1:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")

client = ollama.Client(host=OLLAMA_HOST)

RENDER_HOOK = "https://api.render.com/deploy/srv-d8f85md9j78s73fuad9g?key=HcWVX542GvY"


GITHUB_REPO_URL = "https://github.com/AnayJ/Jarvis-AI-Assistant"
VERCEL_URL = "https://fitness-tracker-vb2x.vercel.app"
