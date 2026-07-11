import webbrowser
import subprocess
import psutil
from backend.services.deploy import deploy_mark_42

def list_apps():
    apps = [p.info["name"] for p in psutil.process_iter(["name"])]
    return list(set(apps))


def open_app(app_name):
    try:
        subprocess.Popen(app_name)
        return f"Opening {app_name} "
    except:
        try:
            subprocess.Popen(f"{app_name}.exe")
            return f"Opening {app_name} "
        except:
            webbrowser.open(f"https://www.google.com/search?q={app_name}")
            return f"Couldn't find {app_name}, searching online "


#  CLOSE APP
def close_app(app_name):
    try:
        for proc in psutil.process_iter(["name"]):
            name = proc.info["name"]
            if name and app_name.lower() in name.lower():
                proc.kill()
                return f"Closed {name} "
        return f"Couldn't find {app_name}"
    except Exception as e:
        return f"Error closing app: {str(e)}"

def handle_command(message):

    msg = message.lower().strip()

    if msg in ["hi", "hello", "hey"]:
        return "Hello sir, what can I do for you today?"

    #OPEN#

    if msg.startswith("open "):
        target = msg.replace("open ", "").strip()

        websites = {
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "github": "https://github.com",
            "linkedin": "https://linkedin.com",
            "twitter": "https://twitter.com",
        }

        if target in websites:
            return {
                "type": "action",
                "action": "open_url",
                "url": websites[target],
                "message": f"Opening {target.title()} 🌐"
            }

        if "." in target:
            return {
                "type": "action",
                "action": "open_url",
                "url": f"https://{target}",
                "message": f"Opening {target} 🌐"
            }

        return open_app(target)

    #DEPLOY#

    if msg == "deploy mark 42":
        return deploy_mark_42()

    #SEARCH#

    if msg.startswith("search "):
        query = msg.replace("search ", "").strip()

        return {
            "type": "action",
            "action": "open_url",
            "url": f"https://www.google.com/search?q={query}",
            "message": f"Searching for {query} 🔍"
        }

    #CLOSE#

    if msg.startswith("close "):
        app = msg.replace("close ", "").strip()
        return close_app(app)

    return None