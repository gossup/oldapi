from flask import Flask
from flask_db2 import DB2
from threading import Thread

app = Flask(__name__)

@app.route('/')

def home():
    return f"<h1>😎I'm Awake Already!🔥</h1>"

def run():
  app.run()

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
