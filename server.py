import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    port = os.getenv("PORT")
    return port
    
@app.route('/next')
def next(args):
    l = sys.argv[1:]
    if not l:
        return "No Arguments"
    else:
        return sys.argv[1:]
    
@app.route('/again')
def again():
    name = sys.argv[1:]
    return name

if __name__ == '__main__':
    app.run()
