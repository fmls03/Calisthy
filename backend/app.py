from flask import Flask, jsonify
from flask_login import login_fresh
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_marshmallow import Marshmallow
from passlib.hash import sha256_crypt
import os
from flask_cors import CORS
from login import *

secret_key = str(os.urandom(256))

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key   
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fmls03:Schipilliti03@localhost/Calisthy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)


ma = Marshmallow(app)
db = SQLAlchemy(app)


app.register_blueprint(login_bp)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    username = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    email = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    passw = db.Column(db.VARCHAR(255), nullable = False) 
    height = db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, nullable = False)

    training_plan = db.relationship('Training_plan', back_populates='user')


    def __init__(self, username, email, passw, height, weight):
        self.username = username
        self.email = email
        self.passw = passw
        self.height = height
        self.weight = weight

    def to_json(self):        
        return {'id': self.id,
                "username": self.name,
                "email": self.email,
                'height': self.height,
                'weight': self.weight
                }

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)



class Training_plan(db.Model):
    __tablename__ = 'training_plan'
    id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    creator = db.Column(db.VARCHAR(255), db.ForeignKey('user.username'))
    plan_id = db.Column(db.Integer, db.ForeignKey('plan_exercise.id'))
    plan = db.relationship('Plan_exercise')
    date = db.Column(db.DATE)
    private = db.Column(db.Boolean)

    user = db.relationship('User', back_populates='training_plan')

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
    ex = db.relationship('Exercise')

    def __init__(self, exercise, user, sets, reps, rest):
        self.exercise = exercise
        self.user = user
        self.sets = sets
        self.reps = reps
        self.rest = rest




def fn():
    return jsonify('bau')

print(app)

if __name__ == '__main__':
    app.run()