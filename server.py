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
    return { 'message': name }

@app.route('/next', methods=['POST', 'GET'])
def next():
    token = request.args.get('token')
    if not token:
        return { 'message': "Missing token." }
    return { 'message': token }

@app.route('/again', methods=['POST', 'GET'])
def again():
    content = request.json
    json = jsonify(content)
    name = json.get('name')
    if not name:
        return { 'message': "Missing token." }
    return { 'message': name }

@app.route('/andagain', methods=['POST', 'GET'])
def andagain():
    input_json = request.get_json(force=True)
    return input_json

if __name__ == '__main__':
    app.run()
