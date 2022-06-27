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
def next():
    result = ""
    for i in sys.argv:
        old = result
        result = old + i
    return result
    
@app.route('/again')
def again():
    n = os.getenv("name")
    return n
    
@app.route('/andagain')
def andagain():
    return sys.argv

if __name__ == '__main__':
    app.run()
