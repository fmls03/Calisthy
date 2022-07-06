import json
from flask import Blueprint, jsonify, request
from sqlalchemy import *
import app

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin/users', methods=['GET'])
def get_users():
    if request.method == 'GET':
        users = app.User.query.all()
        app.db.session.remove()
        return jsonify(users)


@admin_bp.route('/admin/exercises', methods=['GET'])
def get_exercises():
    exercises = app.Exercise.query.all()
    app.db.session.remove()
    return jsonify(exercises)

@admin_bp.route('/admin/users/delete/<userID>', methods=['DELETE'])
def deleteUser(userID):
    if request.method == 'DELETE':
        print(userID)
        app.User.query.filter_by(id=userID).delete()
        app.db.session.commit()
        app.db.session.remove()
        return jsonify('User deleted')


@admin_bp.route('/admin/exercises/edit', methods=['PUT'])
def editExercise():
    if request.method == 'PUT':
        payload = request.get_json()
        app.Exercise.query.filter_by(id = payload.get('id')).update(dict(name=payload.get('name'), path=payload.get('path')))
        app.db.session.commit()
        app.db.session.remove()

        return jsonify('Exercise edited successfully')

@admin_bp.route('/admin/add/exercise', methods=['GET', 'POST'])
def addExercise():
    if request.method == 'POST':
        payload = request.get_json()
        new_exercise = app.Exercise(payload.get('name'), payload.get('path'))
        app.db.session.add(new_exercise)
        app.db.session.commit()
        app.db.session.remove()
        return jsonify('Exercise added')

@admin_bp.route('/admin/exercises/delete/<ExID>', methods=['DELETE'])
def deleteExercise(ExID):
    if request.method == 'DELETE':
        app.Exercise.query.filter_by(id=ExID).delete()
        app.db.session.commit()
        app.db.session.remove()
        return jsonify('Exercise deleted')