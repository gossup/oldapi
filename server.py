import json

from klein import Klein


class ItemStore(object):
    app = Klein()

    def __init__(self):
        self._items = {}

    @app.route('/')
    def items(self, request):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(self._items)

    @app.route('/<string:name>', methods=['PUT'])
    def save_item(self, request, name):
        request.setHeader('Content-Type', 'application/json')
        body = json.loads(request.content.read())
        self._items[name] = body
        return json.dumps({'success': True})

    @app.route('/<string:name>', methods=['GET'])
    def get_item(self, request, name):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(self._items.get(name))


if __name__ == '__main__':
    store = ItemStore()
    store.app.run('localhost', 8080)

#import os
#import sys
#import json
#import http.client
#from collections import Counter
#from flask import Flask, render_template, request, url_for, jsonify
#
#app = Flask(__name__)
#
#@app.route('/', methods=['POST', 'GET'])
#def main():
#    input_json = request.get_json(force=True)
#    return { 'input': input_json }
#
#@app.route('/next', methods=['POST', 'GET'])
#def next():
#    input_json = request.get_json(force=True)
#    return { 'input': jsonify(input_json) }
#
#@app.route('/again', methods=['POST', 'GET'])
#def again():
#    input_json = request.get_json(force=True)
#    return jsonify(input_json)
#
#@app.route('/andagain', methods=['POST', 'GET'])
#def andagain():
#    input_json = request.get_json(force=True)
#    return input_json
#
#if __name__ == '__main__':
#    app.run()
