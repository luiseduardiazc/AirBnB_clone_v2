'''
module hello
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' route / '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' route /hbnb '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''
    Recive text by parameter
    '''
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
