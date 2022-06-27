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
    if not args:
        return "Nothing"
    return args
    
@app.route('/again')
def again():
    n = sys.argv[1]
    return n
    
@app.route('/andagain')
def andagain():
    return sys.argv[1]

if __name__ == '__main__':
    app.run()
