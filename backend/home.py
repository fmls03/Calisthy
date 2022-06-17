from flask import Blueprint, Flask, render_template, request, jsonify, blueprints
from sqlalchemy import *
import app
from datetime import datetime

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/user/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        payload = request.get_json()
        training_plans = app.Training_plan.query.filter_by(creator = payload.get('username')).all()
        app.db.session.remove()
        return jsonify(training_plans)

@home_bp.route('/user/home/exercises', methods=['GET', 'POST'])
def sendPlanExercises():
    if request.method == 'POST':
        payload = request.get_json()
        planID = payload.get('plan_id')
        exercises = app.Plan_exercise.query.filter_by(training_plan_id = planID).all()
        app.db.session.remove()
        return jsonify(exercises)      


@home_bp.route('/exercise/video', methods=['GET', 'POST'])
def watchVideo():
    if request.method == 'POST':
        payload = request.get_json()
        video = app.Exercise.query.filter_by(name = payload.get('exercise_name')).first()
        app.db.session.remove()
        return jsonify(video)
    


@home_bp.route('/exercises/list', methods=['GET'])
def sendExercisesList():
    if request.method == 'GET':
        exercises_list = app.Exercise.query.all()
        app.db.session.remove()
        return jsonify(exercises_list)


@home_bp.route('/user/new_plan', methods=['GET', 'POST'])
def newPlan():
    if request.method == 'POST':
        payload = request.get_json()
        print(payload.get('creator'))
        print(payload.get('plan_name'))
        new_plan = app.Training_plan(payload.get('plan_name'), 'example desc', payload.get('creator'), True)
        app.db.session.add(new_plan)
        app.db.session.commit()
        app.db.session.refresh(new_plan)
        app.db.session.remove()
        


        for ex in payload.get('exercises'):
            new_ex = app.Plan_exercise(ex['exercise'], ex['reps'], ex['sets'], ex['rest'], new_plan.id)
            app.db.session.add(new_ex)
            app.db.session.commit()
            app.db.session.remove()

        return jsonify('aoaoa')


@home_bp.route('/user/delete/plan', methods=['GET', 'POST'])
def deletePlan():
    if request.method == 'POST':
        payload = request.get_json()
        app.Plan_exercise.query.filter_by(training_plan_id = payload.get('plan_id')).delete()
        app.db.session.commit()
        app.Training_plan.query.filter_by(id = payload.get('plan_id')).delete()
        app.db.session.commit()

        app.db.session.remove()

        return jsonify('Eliminato correttamente')