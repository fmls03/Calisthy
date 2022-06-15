from crypt import methods
from flask import Blueprint, Flask, render_template, request, jsonify, blueprints
from sqlalchemy import *
import app

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
    video= ''
    if request.method == 'POST':
        payload = request.get_json()
        video = app.Exercise.query.filter_by(name = payload.get('exercise_name')).first()
        print(video.name)
    return render_template('video.html', video=video)
