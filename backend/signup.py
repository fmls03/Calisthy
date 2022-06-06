from passlib.hash import sha256_crypt
from flask import jsonify, Blueprint, request
from sqlalchemy import *

signup_bp = Blueprint('signup_bp', __name__)

import app

@signup_bp.route('/api/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        payload = request.get_json()
        username = payload.get('username')
        email = payload.get('email')
        password = sha256_crypt.hash(payload.get('password'))
        theme = payload.get('theme')
        height = payload.get('height')
        weight = payload.get('weight')
        user_by_email = app.User.query.filter_by(email = email).first()
        user_by_username = app.User.query.filter_by(username = username).first()
        if not user_by_email and not user_by_username :
            newUser = app.User(username, email, password, theme, height, weight)
            app.db.session.add(newUser)
            app.db.session.commit()
            app.db.session.refresh(newUser)

            return 'User Added'
        else:
            return 'User already registered'

    return jsonify('bau bau')

    