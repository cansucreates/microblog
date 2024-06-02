from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm # This import statement at the top of the file makes the LoginForm class available in the module.

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # The flash() function is a way to show a message to the user. 
        # This message is set in the view function and removed when the user visits another page.
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)