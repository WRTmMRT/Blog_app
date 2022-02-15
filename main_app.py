from pydoc import render_doc
from flask import Flask, render_template
app = Flask(__name__)


posts = [
    
    {
        'author':'Mark Glasse',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'Febuary 1, 2022'
    },
    
    {
        'author':'Xx_Tru3G0m3r_xX',
        'title': 'Help!!',
        'content': "Im super horny and I can't fix it, please help me GamerGuys!! ",
        'date_posted': 'Febuary 4, 2022'
    },
    
    {
        'author':'the_lemmon101',
        'title': 'To @Xx_Tru3G0m3r_xX',
        'content': 'bro wtf, hella cringe',
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

#Allows main app to run the web server
if __name__ == '__main__' :
    app.run(debug=True)
