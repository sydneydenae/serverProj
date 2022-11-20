from flask import Flask, request, jsonify
from collections import defaultdict
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

app.run(host='0.0.0.0')
