from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
secret_key = os.environ.get('SECRET_KEY')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')
database = os.environ.get('DATABASE')

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(user = user, password = password, host = host, port = port, database = database)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app.route import  *