"""Main backend"""

import flask
from flask_cors import CORS
from waitress import serve

app = flask.Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def hello():
    return "Hey"

def main():
    print("Starting backend on port 5000..")
    serve(app, host="0.0.0.0", port=5000)
