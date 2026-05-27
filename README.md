

Jarvis-AI-Assistant 🤖⚡

JARVIS is a futuristic, local AI assistant inspired by Iron Man’s iconic assistant. Built with a modern web interface, real-time streaming responses, voice interaction, and desktop automation capabilities, JARVIS runs entirely on your own machine — keeping your data private while giving you a powerful AI companion.

✨ Features -:
🧠 AI-Powered Conversations
Runs fully locally using Ollama + Gemma models
Real-time streaming responses (ChatGPT-like typing)
Conversation memory support
Fast and lightweight local inference

🎤 Voice Interaction:
Voice input using browser speech recognition
Jarvis can speak responses back to the user
Hands-free interaction support

💻 Modern Futuristic UI:
Beautiful Iron Man inspired interface
Animated glowing effects & glassmorphism design
Responsive layout for desktop and mobile
Real-time typing indicators

⚡ Interruptible Responses:
Stop AI generation anytime using:
ESC key
Stop button
Instant response interruption for smoother UX

🌐 Smart Website & Search Handling:
Jarvis can:
Open websites dynamically
Search the web instantly
Launch commonly used platforms directly

Examples:
open youtube
open github
search machine learning roadmap

🖥️ Desktop Automation:

Jarvis can control your PC using natural commands:

Supported actions:
Open applications
Close applications
Launch websites
Execute assistant commands

Examples:

open chrome
close spotify
Kill Mark 42

📱 Mobile Access - Access Jarvis directly from your phone over the same WiFi network.

🛠️ Tech Stack -: 
Frontend
HTML5
JavaScript
Tailwind CSS
Backend
Python
FastAPI
AI Runtime
Ollama
AI Models
Gemma 2B / Gemma 4
Additional Libraries
psutil
pygetwindow
SpeechRecognition APIs
StreamingResponse (FastAPI)

🚀 Getting Started
Prerequisites: 

Make sure you have installed:

1.Python 3.10+
2.Ollama
Installation:
1️⃣ Clone Repository
git clone https://github.com/AnayJ/Jarvis-AI-Assistant.git

cd Jarvis-AI-Assistant
2️⃣ Install Backend Dependencies
cd backend

pip install -r requirements.txt
3️⃣ Install Ollama

Download Ollama from:

https://ollama.com/download

4️⃣ Pull AI Model

Recommended lightweight model:

ollama pull gemma:2b

Optional:

ollama pull gemma4:e2b

▶️ Running Jarvis:
Start Backend-
cd backend

python -m uvicorn app:app --host 0.0.0.0 --port 8000
Start Frontend-
cd frontend

python -m http.server 5500
Open in Browser

Desktop:

http://127.0.0.1:5500/frontend/index.html

Phone (same WiFi):

http://YOUR_LOCAL_IP:5500/frontend/index.html

🎮 Usage:

Examples:

Hi
open youtube
search operating system concepts
Kill Mark 42
🔥 Current Capabilities

✅ Local AI Assistant
✅ Streaming Responses
✅ Voice Interaction
✅ Desktop Automation
✅ Website Launcher
✅ Mobile Access
✅ Stop Generation
✅ Memory Support
✅ Modern UI

📌 Future Improvements
Internet-enabled AI tools
Smarter natural language command execution
Android app version
AI vision support
Multi-chat history
Workflow automation

🤝 Contributing-:

Contributions, ideas, and improvements are welcome!

Steps:
Fork the repository
Create your feature branch
git checkout -b feature/AmazingFeature
Commit your changes
git commit -m "Add AmazingFeature"
Push to your branch
git push origin feature/AmazingFeature
Open a Pull Request
⚠️ Disclaimer

JARVIS includes desktop automation features. Use responsibly and avoid executing unsafe or destructive commands.

👨‍💻 Developer

Built by Anay Joshi 🚀
Inspired by Iron Man’s JARVIS 😈
