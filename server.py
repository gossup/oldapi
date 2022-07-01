from flask import Flask
from flask_db2 import DB2

app = Flask(__name__)

app.config['DB2_DATABASE'] = 'sample'
app.config['DB2_HOSTNAME'] = 'localhost'
app.config['DB2_PORT'] = 50000
app.config['DB2_PROTOCOL'] = 'TCPIP'
app.config['DB2_USER'] = 'db2inst1'
app.config['DB2_PASSWORD'] = 'db2inst1'

db = DB2(app) #You forgot that


@app.route('/')
def index():
    cur = db.connection.cursor()
    return cur.execute("")

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
