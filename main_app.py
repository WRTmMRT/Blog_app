from pydoc import render_doc
from flask import Flask, flash, redirect, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '16f147ed7bc9d2e0b8af5e0f59ba0ca1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default-img')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"



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
    return render_template('login.html', title='Login', form=form)

#Allows main app to run the web server
if __name__ == '__main__' :
    app.run(debug=True)
