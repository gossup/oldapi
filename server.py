import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    bitch = args.get('name')
    return bitch
    
@app.route('/next')
def next():
    return os.args
    
@app.route('/again')
def again():
    return sys.args

if __name__ == '__main__':
    app.run()
