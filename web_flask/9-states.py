"""Display a list of cities by states and their id"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_states(id=None):
    """Render list of cities by state"""
    all_states = list(storage.all(State).values())
    if not id:
        states = all_states
        print(f"states: {states}")
    else:
        states = [state for state in all_states if state.id == id]
        print(f"states: {states}")
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Teardown and close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
