import os
import json
import time
import logging
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
start_time = time.time()

@app.route('/')
def get_venmo_data():
  session = requests.Session()
  url = "https://venmo.com/api/v5/public?limit={}"
  for i in range(50):
    response = session.get(url.format(1))
    response_dict = json.loads(response.text)
    for transaction in response_dict["data"]:
      print(unicode(transaction["message"]))
    url = response_dict["paging"]["next"] + "&limit={}"

if __name__ == "__main__":
    app.run()


#from flask import Flask
#from flask_db2 import DB2
#
#app = Flask(__name__)
#
#app.config['DB2_DATABASE'] = 'sample'
#app.config['DB2_HOSTNAME'] = 'localhost'
#app.config['DB2_PORT'] = 50000
#app.config['DB2_PROTOCOL'] = 'TCPIP'
#app.config['DB2_USER'] = 'db2inst1'
#app.config['DB2_PASSWORD'] = 'db2inst1'
#
#db = DB2(app) #You forgot that
#
#
#@app.route('/')
#def index():
#    cur = db.connection.cursor()
#    return cur.execute("")

#from flask import Flask
#from threading import Thread
#import sys
#import ibm_db
#
#app = Flask(__name__)
#
#@app.route('/')
#def home():
#    return f"<h1>😎I'm Awake Already!🔥</h1>"
#
#def run():
#  app.run()
#
#def keep_alive():
#    t = Thread(target=run)
#    t.start()
#
#keep_alive()
