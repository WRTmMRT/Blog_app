from pydoc import render_doc
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '16f147ed7bc9d2e0b8af5e0f59ba0ca1'

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


@app.route("/register") #Route to registration page
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login") #Route to login page
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

#Allows main app to run the web server
if __name__ == '__main__' :
    app.run(debug=True)
