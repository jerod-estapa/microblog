from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jerod'}
    posts = [
        {
            'author': {'nickname': 'Lucy'},
            'body': 'Beautiful day in Fort Collins!'
        },
        {
            'author': {'nickname': 'Sadie'},
            'body': "Can't wait for winter!"
        }
    ]
    return  render_template('index.html',
                            title="Jerod's Microblog",
                            user=user,
                            posts = posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)