from flask_app.controllers import users
#import classes in controllers and always import flask app
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)

#everything for server.py