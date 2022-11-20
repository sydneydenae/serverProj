from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)
app.data = defaultdict(int)