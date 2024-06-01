from flask import render_template
from app import app

# This is the main entry point for the application.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Mary'},
            'body': 'I love the movie!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts)
