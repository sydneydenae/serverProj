from flask import Flask, request, jsonify
from collections import defaultdict
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def hello_world():
    return "<p>Home route is working!</p>"

@app.route('/json_post', methods=['POST'])
def json_post():
  data = request.data
  print('Type:', type(data))
  data = json.loads(data)
  print('Data received from client', type(data), data)
  return jsonify(data)

app.run(host='0.0.0.0')
