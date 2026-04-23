import webbrowser
import time
import subprocess
import sys
import os

# Start Flask app in background
print("Starting Flask app...")
flask_process = subprocess.Popen(
    [sys.executable, "app.py"],
    cwd=os.path.dirname(os.path.abspath(__file__)),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait a moment for server to start
time.sleep(3)

# Open browser
print("Opening browser...")
webbrowser.open("http://127.0.0.1:5000")

print("Flask app is running at http://127.0.0.1:5000")
print("Close this window or press Ctrl+C to stop the server")

try:
    flask_process.wait()
except KeyboardInterrupt:
    print("\nShutting down...")
    flask_process.terminate()
    flask_process.wait()
