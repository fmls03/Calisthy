from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_marshmallow import Marshmallow
from passlib.hash import sha256_crypt
import os

secret_key = str(os.urandom(256))

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key   
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fmls03:Schipilliti03@localhost/Calisthy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

mc = Marshmallow(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    username = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    email = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    passw = db.Column(db.VARCHAR(255), nullable = False) 
    height = db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, nullable = False)

    Training_plan = db.relationship('Training_plane', backref='user')

    def __init__(self, username, email, passw, height, weight):
        self.username = username
        self.email = email
        self.passw = passw
        self.height = height
        self.weight = weight

class Training_plan(db.Model):
    __tablename__ = 'training_plan'
    id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    creator = db.Column(db.VARCHAR(255), db.ForeignKey('user.username'), nullable= False)
    date = db.Column(db.DATE, nullable = False)
    private = db.Column(db.Boolean, nullable = False)

    def __init__(self, creator, date, private):
        self.creator = creator
        self.date = date
        self.private = private

class Exercise(db.Model):
    __tablename__ = 'exercise'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    description = db.Column(db.VARCHAR(600))
    path = db.Column(db.VARCHAR(255), nullable = False)

    plan_exercise = db.relationship('Plan_exercise', backref='exercise')

    def __init__(self, name, description, path):
        self.name = name
        self.description = description
        self.path = path


class Plan_exercise(db.Model):
    __tablename__ = 'plan_exercise'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    exercise = db.Column(db.VARCHAR(255), db.ForeignKey('exercise.name'))
    user = db.Column(db.VARCHAR(255), db.ForeignKey('user.username'))
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    rest = db.Column(db.Integer, nullable=False)

    def __init__(self, exercise, user, sets, reps, rest):
        self.exercise = exercise
        self.user = user
        self.sets = sets
        self.reps = reps
        self.rest = rest

if __name__ == '__main__':
    app.run()