#!/usr/bin/python3
"""Script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """To display Hello HBNB! """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """To display HBNB """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_is_cool(text='is cool'):
    """Displays “Python ” followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def numbern(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays html page only n == integer"""
    return render_template("5-number.html", num=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
