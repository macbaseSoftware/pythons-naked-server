from flask import Blueprint,request

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def index():
    return 'Index!'

@main_blueprint.route('/users')
def users():
    return 'Users!'

    
@main_blueprint.route('/evaluate', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return getBestMove()
    else:
        return "else nothing"

def getBestMove():
	return "Bxa4";
