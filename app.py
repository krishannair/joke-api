from flask import Flask, jsonify
from jokes import get_random_joke
import os

app = Flask(__name__)

@app.route('/')
def home():
  return jsonify({
    "message": "Welcome to random jokes API",
    "endpoints": {
      "/joke" : "GET - GET a random joke.",
      "/health": "GET - Health Checkup"
    }
  })

@app.route('/joke')
def joke():
  return jsonify({
    "joke" : get_random_joke(),
    "status" : "success"
  })

@app.route('/health')
def health():
  return jsonify({
    "status" : "healthy"
  }), 200

if __name__=='__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run('0.0.0.0', port=port, debug = False)