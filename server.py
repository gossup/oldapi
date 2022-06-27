import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main(args):
    bitch = args.get('name')
    name = "BITCH"
    if bitch:
        name = bitch
    hello = "HELLO {0}".format(name)
    return hello
    
@app.route('/next')
def next():
    hello = os.getenv('XXX')
    return hello

if __name__ == '__main__':
    app.run()
