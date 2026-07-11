from backend.config import client
from backend.config import OLLAMA_MODEL
from backend.services.handle import handle_command
import json

chat_history = [
    {
        "role": "system",
        "content": "You are Jarvis, an AI assistant that can control the user's PC safely.",
    }
]


def generate_response(message):
    global chat_history, stop_generation

    stop_generation = False  # reset

    try:

        chat_history.append({"role": "user", "content": message})

        stream = client.chat(
            model=OLLAMA_MODEL,
            messages=chat_history,
            stream=True,
            options={"num_predict": 300, "temperature": 0.7},
        )

        full_reply = ""

        for chunk in stream:
            if stop_generation:
                yield "\n\n Stopped."
                return

            part = chunk["message"]["content"]
            full_reply += part
            yield part

        chat_history.append({"role": "assistant", "content": full_reply})

    except Exception as e:
        yield f" Error: {str(e)}"
