import os
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def my_test_endpoint():
    input_json = request.get_json(force=True)
    # force=True, above, is necessary if another developer
    # forgot to set the MIME type to 'application/json'
    print 'data from client:', input_json
    dictToReturn = {'answer':42}
    return jsonify(dictToReturn)

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
