import webbrowser
import subprocess
import requests
from backend.config import *
def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr


def trigger_render():
    try:
        requests.post(RENDER_HOOK)
        # return "Render deployment triggered"
    except Exception as e:
        return f"Render deploy failed: {str(e)}"


def deploy_mark_42():
    run_command("git add .")
    run_command('git commit -m "Deploy Mark 42"')
    run_command("git push origin main")

    trigger_render()

    webbrowser.open("https://fitness-tracker-vb2x.vercel.app")

    return "Mark 42 Deployed, All Systems Online Sir."
