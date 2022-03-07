from pydoc import render_doc
from main_app import app
#Allows main app to run the web server
if __name__ == '__main__' :
    app.run(debug=True)
