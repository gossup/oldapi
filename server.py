import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    hello = "HELLO BITCH"
    return hello
    
@app.route('/next')
def next():
    hello = "HELLO NEXT"
    return hello

if __name__ == '__main__':
    app.run()
