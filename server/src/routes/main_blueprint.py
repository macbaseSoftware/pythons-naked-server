from flask import Blueprint,request
main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def index():
    return 'Index!'

@main_blueprint.route('/users')
def users():
    return 'Users!'

    