from flask import jsonify, request, Blueprint
from sqlalchemy import *
from passlib.hash import sha256_crypt

login_bp = Blueprint('login_bp', __name__)

import app

@login_bp.route('/api/login', methods=['GET', 'POST'])
def login_api():
    if request.method == 'POST':
        payload = request.get_json()
        print(payload.get('username'), payload.get('password'))
        user = app.User.query.filter_by(username = payload.get('username')).first()
        users = app.User.query.all()
        print(users)
        if user:
            if sha256_crypt.verify(payload.get('password'), user.passw):
                app.db.session.remove()
                return jsonify(user)
            else:
                app.db.session.remove()
                return jsonify('wrong password')
        else:
            app.db.session.remove()
            return jsonify('wrong username')
    return jsonify('miao')

