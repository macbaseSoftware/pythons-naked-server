from flask import Blueprint,request
from engine.index import getBestMove
engine_blueprint = Blueprint('engine_blueprint', __name__)


@engine_blueprint.route('/evaluate', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return getBestMove()
    else:
        return "else nothing"

