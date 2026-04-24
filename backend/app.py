from fastapi import FastAPI
from pydantic import BaseModel
import ollama
from fastapi.middleware.cors import (
    CORSMiddleware,
)  # safety ke liye hai, connection b/w backend & frontend
from fastapi.responses import StreamingResponse
import subprocess
import webbrowser
import psutil
import pygetwindow as gw
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


class Request(BaseModel):
    message: str


chat_history = [
    {
        "role": "system",
        "content": "You are Jarvis, an AI assistant that can control the user's PC safely.",
    }
]


#  OPEN APP (SMART)
def open_app(app_name):
    try:
        subprocess.Popen(app_name)
        return f"Opening {app_name} 🚀"
    except:
        try:
            subprocess.Popen(f"{app_name}.exe")
            return f"Opening {app_name} 🚀"
        except:
            webbrowser.open(f"https://www.google.com/search?q={app_name}")
            return f"Couldn't find {app_name}, searching online 🔍"


#  CLOSE APP
def close_app(app_name):
    try:
        for proc in psutil.process_iter(["name"]):
            name = proc.info["name"]
            if name and app_name.lower() in name.lower():
                proc.kill()
                return f"Closed {name} ❌"
        return f"Couldn't find {app_name}"
    except Exception as e:
        return f"Error closing app: {str(e)}"


# SWITCH WINDOW
def switch_window(app_name):
    try:
        windows = gw.getWindowsWithTitle(app_name)

        if not windows:
            return f"No window found for {app_name}"

        win = windows[0]

        if win.isMinimized:
            win.restore()
            time.sleep(0.5)

        win.activate()
        time.sleep(0.5)

        return f"Switched to {win.title} 🔄"

    except Exception as e:
        return f"Error switching window: {str(e)}"


#  LIST RUNNING APPS (for debugging / smart matching)
def list_apps():
    apps = [p.info["name"] for p in psutil.process_iter(["name"])]
    return list(set(apps))


#  COMMAND HANDLER
def handle_command(message):
    msg = message.lower().strip()

    if msg in ["hi","hello","hey"]:
        return "Hello sir, what can I do for you today?"
    
    if msg.startswith("open "):
        target = msg.replace("open ", "").strip()

        # If user typed a domain-like name or common website
        if "." in target or target in [
            "youtube",
            "google",
            "github",
            "twitter",
            "linkedin",
        ]:
            # add https://www if not a domain
            if "." not in target:
                url = f"https://{target}.com"
            else:
                url = f"https://{target}"
            webbrowser.open(url)
            return f"Opening {url} 🌐"

        # Otherwise treat it as an app
        return open_app(target)

    # Search
    elif msg.startswith("search "):
        query = msg.replace("search ", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query} 🔍"

    # Close apps
    elif msg.startswith("close "):
        app = msg.replace("close ", "")
        return close_app(app)

    return None


def generate_response(message):
    global chat_history, stop_generation

    stop_generation = False  # reset

    try:
        command_result = handle_command(message)
        if command_result:
            yield command_result
            return

        chat_history.append({"role": "user", "content": message})

        stream = ollama.chat(
            model="mistral",
            messages=chat_history,
            stream=True,
            options={
                "num_predict": 300,
                "temperature": 0.7
            }
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


@app.post("/chat")
def chat(req: Request):
    return StreamingResponse(generate_response(req.message), media_type="text/plain")

@app.post("/stop")
def stop():
    global stop_generation
    stop_generation = True
    return {"status": "stopped"}
