#!/usr/bin/python3
'''
module hbnb_filters
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def find_state():
    """ hbnb_filters
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(self):
    ''' teardown_db '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
