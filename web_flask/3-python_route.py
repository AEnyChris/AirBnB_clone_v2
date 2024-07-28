#!/usr/bin/python3
"""Display Python is <given text>"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Render Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """Render HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Render C is text"""
    new_text = text.replace("_", " ")
    return f"C {new_text}"


@app.route("/python/", defaults={'text': "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """Render Python is text"""
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
