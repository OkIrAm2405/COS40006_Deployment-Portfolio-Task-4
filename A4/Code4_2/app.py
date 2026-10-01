from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Dockerized Python Flask App!</h1><p>Task 4.2 - Credit Level Completed.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)