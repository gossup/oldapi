import ibm_db
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>😎I'm Awake Already!🔥</h1>"

def run():
  app.run()

def keep_alive():
    t = Thread(target=run)
    t.start()
    

def connect_to_database():
  db_handler = SqliteDBConnect("uid={0};""pwd={1}".format(UID, PWD),
                                table_prefix="{}".format(TBL_PRFX))
  return db_handler

fd = {'_database': None}
def get_db():
  db = fd['_database']
  if not isinstance(db, SqliteDBConnect):
    fd['_database'] = connect_to_database()
    db = fd['_database']
return db

with application.app_context():
  #Get DB connection from application's context
  db = LocalProxy(lambda: get_db())


keep_alive()
