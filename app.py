#!/usr/bin/env python3
"""A minimal Flask app to pass SAST and DAST checks."""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Return a basic status message."""
    return jsonify({"status": "alive"}), 200

if __name__ == "__main__":
    # Run on port 8080 for DAST (ZAP) testing
    app.run(host="0.0.0.0", port=8080, debug=False)