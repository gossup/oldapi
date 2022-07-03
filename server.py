import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    token = request.args.get('token')
    if not token:
        return { 'message': "Missing token." }
    name = request.args.get('token')
    if not name:
        return { 'message': "Missing name." }
    return { 'message': name }

@app.route('/next', methods=['POST', 'GET'])
def next():
    token = request.args.get('token')
    if not token:
        return { 'message': "Missing token." }
    return { 'message': token }

@app.route('/again', methods=['POST', 'GET'])
def again():
    depID = os.getenv('depID')
    if not depID:
        return { 'message': "Missing depID." }
    hostname = os.getenv('db2-hostname')
    if not hostname:
        return { 'message': "Missing hostname." }
    token = request.args.get('token')
    if not token:
        return { 'message': "Missing token." }
    name = request.json['name']
    if not name:
        return { 'message': "Missing name." }
    return { 'message': name }

if __name__ == '__main__':
    app.run()
