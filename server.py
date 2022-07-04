import os
import sys
import json
from app import requests
from collections import Counter
from flask import Flask, render_template, request, session, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return { 'hello': "there" }
    
if __name__ == 'main':
    app.run()
