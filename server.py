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
    name = request.json['name']
    if not name:
        return { 'message': "Missing name." }
    return { 'message': name }

@app.route('/next', methods=['POST', 'GET'])
def next():
    depID = os.getenv('depID')
    if not depID:
        return { 'Error': "Missing depID." }
    hostname = os.getenv('db2-hostname')
    if not hostname:
        return { 'Error': "Missing hostname." }
    token = request.args.get('token')
    if not token:
        return { 'Error': "Missing token." }
    since = request.json['since']
    if not since:
        return { 'Error': "Missing since." }
        
    split = since.split(',')
    createdAt = "'{0} {1}'".format(split[0], split[1])
    
    getPostsCommand = "SELECT p.parentId AS parentId, p.createdBy AS createdBy FROM GOSSUP.post p WHERE p.createdAt > {0} GROUP BY parentId, createdBy ORDER BY p.createdBy;".format(createdAt)

    getPostsSqlCommand = {
        'commands': getPostsCommand,
        'limit': 1000,
        'separator': ";",
        'stop_on_error': "yes"
    }
    
    headers = {
    'accept': "application/json",
    'authorization': "Bearer {}".format(token),
    'content-type': "application/json",
    'x-deployment-id': "{}".format(depID)
    }
    
    conn = http.client.HTTPSConnection(hostName)
    
    conn.request("POST", "/dbapi/v4/sql_jobs", headers=headers, body=json.dumps(getPostsSqlCommand))

    postRes = conn.getresponse()
    postData = postRes.read()
    
    return { 'message': getPostsCommand }

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

@app.route('/andagain', methods=['POST', 'GET'])
def andagain():
    input_json = request.get_json(force=True)
    return input_json

if __name__ == '__main__':
    app.run()
