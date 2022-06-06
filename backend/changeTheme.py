import app
from flask import Flask, Blueprint, request, jsonify

from sqlalchemy import *

changeTheme_bp = Blueprint('changeTheme_bp', __name__)

@changeTheme_bp.route('/api/user/changeTheme', methods=['GET', 'POST'])
def changeTheme():
    if request.method == 'POST':
        payload = request.get_json()
        user = app.User.query.filter_by(username = payload.get('username')).first()
        user.theme = not user.theme

        app.db.session.commit()
        return jsonify('Theme changed')     
