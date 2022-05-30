from flask import jsonify, request, Blueprint
from sqlalchemy import *
from passlib.hash import sha256_crypt

login_bp = Blueprint('login_bp', __name__)

from app import *


@login_bp.route('/api/login', methods=['GET', 'POST'])
def login_api():
    if request.method == 'POST':
        payload = request.get_json()
        print(payload.get('username'), payload.get('password'))
        user = User.query.filter_by(username = payload.get('username')).first()
        users = User.query.all()
        print(users)
        if user:
            print(user, 1)
            if sha256_crypt.verify(payload.get('password'), user.passw):
                print(user, 2)
                user =  User.to_json(user)
    return jsonify('miao')

