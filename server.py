import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    name = request.args.get('name')
    if not name:
        return { 'message': request.args }
    return { 'message': name }

@app.route('/next', methods=['POST', 'GET'])
def next():
    name = request.args.get('name')
    if not name:
        return { 'message': "NO NAME" }
    return { 'message': name }

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
