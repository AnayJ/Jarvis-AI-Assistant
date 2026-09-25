from backend.config import client, OLLAMA_MODEL
from backend.services.handle import handle_command
import backend.services.state as state


def generate_response(message):
    # Reset stop flag
    state.stop_generation = False

    try:
        # Handle custom commands first
        command_result = handle_command(message)
        if command_result:
            yield command_result
            return

        # Add user message to memory
        state.chat_history.append({
            "role": "user",
            "content": message
        })

        stream = client.chat(
            model=OLLAMA_MODEL,
            messages=state.chat_history,
            stream=True,
            options={
                "num_predict": 300,
                "temperature": 0.7,
            },
        )

        full_reply = ""

        for chunk in stream:

            # Stop generation if requested
            if state.stop_generation:
                yield " You stopped the response."
                return

            part = chunk["message"]["content"]
            full_reply += part
            yield part

        # Save assistant response
        state.chat_history.append({
            "role": "assistant",
            "content": full_reply
        })

    except Exception as e:
        yield f" Error: {str(e)}"