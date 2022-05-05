from flask import Flask, Blueprint

homepage_bp = Blueprint('homepage_bp', __name__)

import app


@homepage_bp.route('/homepage')
def homepage():
    return 'HOMEPAGE'