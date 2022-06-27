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
    return args
    
@app.route('/again')
def again():
    return "!"

if __name__ == '__main__':
    app.run()
