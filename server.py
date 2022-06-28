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
    input_json = request.get_json(force=True)
    return jsonify(input_json)
    
@app.route('/andagain', methods=['POST', 'GET'])
def andagain():
    input_json = request.get_json(force=True)
    return input_json

if __name__ == '__main__':
    app.run()
