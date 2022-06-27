import os
import sys
import json
import http.client
from collections import Counter
from flask import Flask, render_template
from flask import Flask, request

app = Flask(__name__)

# Route all possible paths here
@app.route("/", defaults={"path": ""})
@app.route('/<string:path>')
@app.route("/<path:path>")

def index(path):
    [server_host, server_port] = request.host.split(':')
    path =  "/" + path
    query_params = request.args
    return query_params

#@app.route('/')
#def main():
#    port = os.getenv("PORT")
#    return port
#
#@app.route('/next')
#def next():
#    result = ""
#    for i in sys.argv:
#        old = result
#        result = old + i
#    return result
#
#@app.route('/again')
#def again():
#    url = os.environ['HTTP_HOST']
#    uri = os.environ['REQUEST_URI']
#    return url + uri
#
#@app.route('/andagain')
#def andagain():
#    url = os.getenv('HTTP_HOST')
#    uri = os.getenv('REQUEST_URI')
#    return url + uri

if __name__ == '__main__':
    app.run()
