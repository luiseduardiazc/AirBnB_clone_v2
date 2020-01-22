#!/usr/bin/python3
'''
module states
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_all_states():
    """lists states
    """
    states_dict = storage.all(State)
    states = []
    for k, v in states_dict.items():
        states.append(v)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def find_state(id):
    """lists states with specific id
    """
    states_dict = storage.all(State)
    states = []
    states_id = []
    for k, v in states_dict.items():
        states_id.append(v.id)
        states.append(v)
    return render_template('9-states.html', states=states,
                           states_id=states_id, id=id)


@app.teardown_appcontext
def teardown_db(self):
    ''' teardown_db '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
