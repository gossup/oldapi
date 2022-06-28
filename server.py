import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    port = os.getenv("PORT")
    return port
    
@app.route('/next', methods=['POST', 'GET'])
def next():
    result = ""
    for i in sys.argv:
        old = result
        result = old + i
    return result
    
@app.route('/again', methods=['POST', 'GET'])
def again():
    url = os.environ['HTTP_HOST']
    uri = os.environ['REQUEST_URI']
    return url + uri
    
@app.route('/andagain', methods=['POST', 'GET'])
def andagain():
    url = os.getenv('HTTP_HOST')
    uri = os.getenv('REQUEST_URI')
    return url + uri

if __name__ == '__main__':
    app.run()
