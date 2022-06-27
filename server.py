import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    port = os.getenv("name")
    return port
    
@app.route('/next')
def next():
    result = ""
    for item, value in os.environ.items():
        old = result
        result = old + '{}: {}'.format(item, value)
    return result
    
@app.route('/again')
def again():
    n = __name__
    return n
    
@app.route('/andagain')
def andagain():
    return __args__

if __name__ == '__main__':
    app.run()
