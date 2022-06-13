from crypt import methods
from flask import Blueprint, Flask, request, jsonify, blueprints
from sqlalchemy import *
import app

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/user/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        payload = request.get_json()
        training_plans = getTrainingPlans(payload)    
        return jsonify(training_plans)


def getTrainingPlans(payload):
    training_plans = app.Training_plan.query.filter_by(creator = payload.get('username')).all()
    training_planSchema = app.Training_planSchema(many = True)
    training_plans_json = training_planSchema.dump(training_plans)
    return training_plans_json


@home_bp.route('/user/home/exercises', methods=['GET', 'POST'])
def sendPlanExercises():
    if request.method == 'POST':
        payload = request.get_json()
        planID = payload.get('plan_id')
        exercises = app.Plan_exercise.query.filter_by(training_plan_id = planID).all()
        exercises_json = exercises.to_dict()
        
        print(exercises_json)
        return jsonify(exercises_json)        
