"""
    Example Controllers
"""

from app import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from app.models.Hello import Hello
"""
#route index
@app.route('/', methods = ['GET', 'POST'])
def index():
    data = {
        "title": "Flask-up",
        "body": "Flask-up and running"
    }
    return render_template('index.html', data = data)

#route hello
@app.route('/hello', methods = ['GET', 'POST'])
def hello():
    data = {
        "title": "Hello World",
        "body": "Flask simple MVC"
    }
    return render_template('hello.html', data = data)

