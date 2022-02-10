from flask import Flask
from numpy import true_divide

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>home</h1>"

@app.route("/about")
def about():
    return "<h6>about</h6>"


if __name__ == '__main__' :
    app.run(debug=True)
