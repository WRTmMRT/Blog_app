from main_app import app
from pydoc import render_doc

#Allows main app to run the web server
if __name__ == '__main__' :
    app.run(debug=True)
