import flask
from flask import jsonify
#TPL = flask.render_template # Pour éviter de toujours taper flask.render_template...

app = flask.Flask(__name__)

@app.route('/')
def info():
    return jsonify("hello world")

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=80)
