from flask import Flask
from flaskblog.posts_data import posts
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt


app = Flask(__name__)

#configuration of the happen
app.config['SECRET_KEY'] = '0b931872351e7af96597'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///flask.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

from flaskblog import routes