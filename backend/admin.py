from crypt import methods
from flask import Flask, Blueprint, jsonify
from sqlalchemy import *
import app

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('admin/users', methods=['GET'])
def get_users():
    users = app.User.query.all()
    app.db.session.remove()
    return jsonify(users)


@admin_bp.route('admin/exercises', methods=['GET'])
def get_exercises():
    exercises = app.Exercise.query.all()
    app.db.session.remove()
    return jsonify(exercises)