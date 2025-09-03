from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "🤖 Bot is alive and running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    run_flask()
