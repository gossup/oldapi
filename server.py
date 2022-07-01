import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return { 'message': "Hello" }

if __name__ == '__main__':
    app.run()
