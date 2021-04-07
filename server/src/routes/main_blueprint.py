from flask import Blueprint,request
main_blueprint = Blueprint('main_blueprint', __name__)
from flask_socketio import SocketIO, send

@main_blueprint.route('/blueprint')
def index():
    return 'Index!'

@main_blueprint.route('/users')
def users():
    return 'Users!'

    