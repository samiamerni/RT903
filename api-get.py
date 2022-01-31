import flask
from flask import jsonify
#TPL = flask.render_template # Pour éviter de toujours taper flask.render_template...
#import sys
import os
app = flask.Flask(__name__)

@app.route('/')
def info():
   return jsonify({"message":os.environ.get('MSG')})
   # return jsonify({"message":sys.argv[1]})

if __name__ == '__main__':
#    app.config['DEBUG'] = True
    #app.run(host='0.0.0.0', port=int(sys.argv[2]))
    app.run(host='0.0.0.0', port=os.environ.get('PYTHON_PORT'))
