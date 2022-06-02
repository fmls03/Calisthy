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
        height = payload.get('height')
        weight = payload.get('weight')
        user = app.User.query.filter_by(email = email).first()
        if not user:
            newUser = app.User(username, email, password, height, weight)
            app.db.session.add(newUser)
            app.db.session.commit()
            app.db.session.refresh(newUser)

            return jsonify('User Added')
        else:
            return jsonify('User already registered')

    return jsonify('bau bau')

    