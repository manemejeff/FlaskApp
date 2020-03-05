from theapp.myapp import app
from theapp.forms import LoginForm
from flask import render_template


@app.route('/')
def index():
    return '<h1>You are on the index.</h1>'


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('index.html', form=form)
