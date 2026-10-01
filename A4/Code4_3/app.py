import os
import socket
from datetime import datetime
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

APP_TITLE = os.getenv("APP_TITLE", "Custom Cloud Dashboard")
APP_ENV = os.getenv("APP_ENV", "Development")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f7f6; color: #333; }
        .card { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
        h1 { color: #0070f3; margin-top: 0; }
        .badge { display: inline-block; padding: 5px 10px; background: #e0f2fe; color: #0369a1; border-radius: 4px; font-weight: bold; }
        ul { list-style: none; padding: 0; }
        li { margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px; }
        strong { color: #555; }
    </style>
</head>
<body>
    <div class="card">
        <h1>{{ title }}</h1>
        <p><span class="badge">Environment: {{ env }}</span></p>
        <ul>
            <li><strong>Task:</strong> SWE40006 - Task 4.3 Distinction Level</li>
            <li><strong>Container Hostname:</strong> {{ hostname }}</li>
            <li><strong>Server Time:</strong> {{ time }}</li>
            <li><strong>Status:</strong> Active & Containerized</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(
        HTML_TEMPLATE,
        title=APP_TITLE,
        env=APP_ENV,
        hostname=hostname,
        time=current_time
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "environment": APP_ENV})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)