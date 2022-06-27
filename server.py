import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template
from urllib.parse import urlparse
from urllib.parse import parse_qs

app = Flask(__name__)

@app.route('/')
def main():
    url = os.getenv("URL")
    return url
    
@app.route('/next')
def next():
    url = os.getenv("URL")
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)['name'][0]
    
@app.route('/url')
def andagain():
    url = os.environ['URL']
    return url
    
@app.route('/url2')
def andagain():
    return __url__
    
@app.route('/again')
def again():
    url = os.environ['HTTP_HOST']
    uri = os.environ['REQUEST_URI']
    return url + uri
    
@app.route('/andagain')
def andagain():
    return __args__

if __name__ == '__main__':
    app.run()
