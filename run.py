import subprocess
import time
import sys
import os

BACKEND_PATH = os.path.join("backend", "api.py")
STREAMLIT_PATH = "app.py"

print("🚀 Starting NuggetAI...")

backend_process = subprocess.Popen(
    [sys.executable, BACKEND_PATH],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("✅ Flask backend starting...")

time.sleep(3)

streamlit_process = subprocess.Popen(
    ["streamlit", "run", STREAMLIT_PATH],
)

print("✅ Streamlit frontend starting...")

try:
    backend_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    print("\n🛑 Shutting down NuggetAI...")

    backend_process.terminate()
    streamlit_process.terminate()

    print("✅ Clean exit completed.")