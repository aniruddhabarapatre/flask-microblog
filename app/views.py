from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = { 'nickname': 'Ani' }
    posts = [
            { 'author': { 'nickname': 'John' }, 'body': 'Beautiful day in Miami!' },
            { 'author': { 'nickname': 'Susan' }, 'body': 'The Avengers movie was cool.'}
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')

def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
