from flask import render_template, url_for, flash, redirect
from . import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog.posts_data import posts

@app.route('/')
@app.route('/Home')
def Home():
    return render_template('home.html', posts = posts)

#About Page
@app.route('/About')
@app.route('/About')
def About():
    return render_template('about.html', title = 'About Page')

#
@app.route('/Register', methods = ['GET', 'POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # warning class of bootstrap success
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('Home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/Login', methods =['GET', 'POST'] )
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'you have been logged in!', 'success')
            redirect(url_for('Home'))
        else:
            flash(f'login unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form) 