#!/usr/bin/python3
"""Display a list of cities by states and their id"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Render list of cities by state"""
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html', states=states,
                            amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Teardown and close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
