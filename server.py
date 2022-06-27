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
    if bitch:
        return "{}".format(bitch)
    else:
        return "NOTHING"
    
@app.route('/next')
def next():
    hello = "HI"
    return hello

if __name__ == '__main__':
    app.run()
