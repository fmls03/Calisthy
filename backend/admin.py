
import json
from flask import Flask, Blueprint, jsonify, request
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


@admin_bp.route('/admin/exercises/edit/<exerciseID>', methods=['PUT'])
def editExercise(exerciseID):
    if request.method == 'PUT':
        payload = request.get_json()
        ex = app.Exercise.query.filter_by(id = exerciseID).first()
        ex.name = payload.get('name')
        ex.path = payload.get('path')

        app.db.session.merge(ex)
        app.db.session.commit()
        app.db.session.remove()

        return jsonify('Exercise edited successfully')