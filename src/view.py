from src.app import app
from flask import render_template


@app.route('/hello')
def hello_world():
    return render_template('base_templates/main.html', title='Hello World')


@app.route('/')
def index_page():
    return render_template('main.html', title='Home')


@app.route('/login')
def sign_in():
    return render_template('sign_up.html', title='Sign_in')
