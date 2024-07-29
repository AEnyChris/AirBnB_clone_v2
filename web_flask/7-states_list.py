#!/usr/bin/python3
"""Display a list of states and their id"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def disp_state_list():
    """Render list of states from template"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Teardown and close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
