import subprocess
import time
import sys
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.join(PROJECT_DIR, "api.py")
STREAMLIT_PATH = os.path.join(PROJECT_DIR, "app.py")

print("🚀 Starting NuggetAI...")

backend_process = subprocess.Popen(
    [sys.executable, BACKEND_PATH],
    cwd=PROJECT_DIR,
)

print("✅ Flask backend starting...")

time.sleep(3)

streamlit_process = subprocess.Popen(
    [sys.executable, "-m", "streamlit", "run", STREAMLIT_PATH],
    cwd=PROJECT_DIR,
)

print("✅ Streamlit frontend starting...")

try:
    while backend_process.poll() is None and streamlit_process.poll() is None:
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n🛑 Shutting down NuggetAI...")
finally:
    for process in (backend_process, streamlit_process):
        if process.poll() is None:
            process.terminate()
    for process in (backend_process, streamlit_process):
        process.wait()

print("✅ Clean exit completed.")