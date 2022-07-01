from flask import Flask
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
