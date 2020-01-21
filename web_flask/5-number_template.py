#!/usr/bin/python3
'''
module hello
'''
from flask import Flask
from flask import render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    '''
    Recive optional text
    The default value of text is "is cool"
    '''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    '''
    is a number
    '''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_a_number_template(n):
    '''
    is a number template
    '''
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
