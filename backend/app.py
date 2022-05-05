from flask import Flask, redirect
import os

from homepage import homepage_bp

secret_key = str(os.urandom(128))

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key

app.register_blueprint(homepage_bp)

@app.route('/')
def index():
    return redirect('/homepage')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)

