from flask import render_template
from app import app

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