#!/usr/bin/python3
"""A simple Hello World Application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Render Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hello", strict_slashes=False)
def hello():
    """Render HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
