from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Professor Portier'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST']) # specify methods
def login():
    form = LoginForm() # instantiate object
    if form.validate_on_submit():  # POST method validates
        flash('Login requested for user {},'
              'remember_me = {}'.format(form.username.data,
                                        form.remember_me.data))
        # flash to display messages for prototype, driver
        return redirect(url_for('index')) # navigation when complete
    return render_template('login.html',
                           title='Sign In',
                           form=form) # pass form
