from flask import Flask, Blueprint, render_template

homepage_bp = Blueprint('homepage_bp', __name__)

import app


@homepage_bp.route('/homepage')
def homepage():
    return render_template('homepage.html')