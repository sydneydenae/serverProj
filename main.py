from flask import Flask, request, jsonify
from collections import defaultdict
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
  record = json.loads(request.data)
  print(record)
  if 'first_name' in record and 'bison_id' in record:
    bid = record['bison_id']
    app.data[bid] += 1
    return jsonify({'status': 'success'})
  else:
    return jsonify({'status': 'failed first_name or bison_id not provided'})

@app.route('/validate', methods=['GET'])
def validate():
  record = json.loads(request.data)
  if 'bison_id' in record:
    bid = record['bison_id']
    if app.data[bid] >= 10:
      return jsonify({'status': 'complete'})
    else:
      return jsonify({'status': 'number of requests not fulfilled'})

    

app.run(host='0.0.0.0')
