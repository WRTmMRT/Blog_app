from flask import flash, redirect, render_template, url_for
from main_app import app
from main_app.forms import RegistrationForm, LoginForm
from main_app.models import User, Post

posts = [
    
    {
        'author':'Mark Glasse',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'Febuary 1, 2022'
    },
    
    {
        'author':'Xx_Tru3G0m3r_xX',
        'title': 'post',
        'content': "second post content",
        'date_posted': 'Febuary 4, 2022'
    },
    
    {
        'author':'the_lemmon101',
        'title': 'post',
        'content': 'third post content',
        'date_posted': 'Febuary 4, 2022'
    }
]

#Routes to pages
@app.route("/") #Route to main page
@app.route("/home") #Route to home page
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") #Route to about page
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST']) #Route to registration page
def register():
    form = RegistrationForm()
    #Check if form is valid
    if form.validate_on_submit():
        flash(f'Account made for {form.username.data}', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login unsuccessful, Please check your username and password', 'danger')
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST']) #Route to login page
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@post.com" and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
    else:
        flash('Login unsuccessful, Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
