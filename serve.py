from flask import Flask, request
import socket
import subprocess
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def handler():
    if request.method == "POST":
        subprocess.Popen(["python", "stress_cpu.py"])
        return "POST REQUEST SUCCEEDED"
    else:
        return socket.gethostname()

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True, port = 8000)