from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import *
from flask_marshmallow import Marshmallow


import os

from login import *
from signup import *
from changeTheme import *
from home import *

secret_key = str(os.urandom(256))

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key   
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fmls03:Schipilliti03@fmls.ddns.net/Calisthy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)


DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "100"))
WEB_CONCURRENCY = int(os.getenv("WEB_CONCURRENCY", "2"))
POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = dict(pool_size=POOL_SIZE, max_overflow=0)

ma = Marshmallow(app)
db = SQLAlchemy(app)

app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(changeTheme_bp)
app.register_blueprint(home_bp)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    username = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    email = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    passw = db.Column(db.VARCHAR(255), nullable = False) 
    theme = db.Column(db.Boolean)
    height = db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, nullable = False)

    training_plan = db.relationship('Training_plan', back_populates='user')


    def __init__(self, username, email, passw, theme, height, weight):
        self.username = username
        self.email = email
        self.passw = passw
        self.theme = theme
        self.height = height
        self.weight = weight

    def to_json(self):        
        return {'id': self.id,
                "username": self.username,
                "email": self.email,
                "theme": self.theme,
                'height': self.height,
                'weight': self.weight
                }


class Training_plan(db.Model):
    __tablename__ = 'training_plan'
    id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    title = db.Column(db.VARCHAR(255))
    description = db.Column(db.VARCHAR(255))
    creator = db.Column(db.VARCHAR(255), db.ForeignKey('user.username'))
    date = db.Column(db.DATE)
    private = db.Column(db.Boolean)

    user = db.relationship('User', back_populates='training_plan')

    def __init__(self, title, description, creator, date, private):
        self.title = title
        self.description = description
        self.creator = creator
        self.date = date
        self.private = private


class Training_planSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Training_plan
        load_istance = True


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
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    rest = db.Column(db.Integer, nullable=False)
    training_plan_id = db.Column(db.Integer, db.ForeignKey('training_plan.id')) 
    ex = db.relationship('Exercise')
    tr = db.relationship('Training_plan')

    def __init__(self, exercise, sets, reps, rest, training_plan_id):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.rest = rest
        self.training_plan_id = training_plan_id

class Plan_ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plan_exercise
        load_istance = True




def fn():
    return jsonify('bau')

print(app)

if __name__ == '__main__':
    app.run()
