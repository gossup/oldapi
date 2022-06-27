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
    arg = os.getarg("name")
    return port
    
@app.route('/again')
def again():
    rg = os.getargs("name")
    return rg
    
@app.route('/andagain')
def andagain():
    rg = os.args()
    return rg

if __name__ == '__main__':
    app.run()
