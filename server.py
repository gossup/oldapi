import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main(args):
    bitch = args.get('name')
    return bitch
    
@app.route('/next')
def next(args):
    return args

if __name__ == '__main__':
    app.run()
