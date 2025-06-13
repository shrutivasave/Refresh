from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS #allows to send req from a different urls

app = Flask(__name__)
CORS(app) #disables CORS errors

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" #specifying the location of local sqlite db stored on our machine
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) #create db instance giving access to mydatabase
#to create , modify, delete using "db" object this is ORM
