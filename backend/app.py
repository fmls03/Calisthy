from flask import Flask, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_cors import CORS

from homepage import homepage_bp

secret_key = str(os.urandom(128))

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fmls03:Schipilliti03@localhsot/Calisthy'
app.congig['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins':'*'}})

db = SQLAlchemy(app)

app.register_blueprint(homepage_bp)


@app.route('/')
def index():
    return redirect('/homepage')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)

