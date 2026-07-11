import webbrowser
import subprocess
import psutil
from deploy import deploy_mark_42

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
            return f"Opening {url} "

        # Otherwise treat it as an app
        return open_app(target)

    elif msg == "deploy mark 42":
        return deploy_mark_42()

    # Search
    elif msg.startswith("search "):
        query = msg.replace("search ", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query} "

    # Close apps
    elif msg.startswith("close "):
        app = msg.replace("close ", "")
        return close_app(app)

    return None
