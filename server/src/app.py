from flask import Flask, Blueprint
from routes.main_blueprint import *
from routes.engine_blueprint import *
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
# app.register_blueprint(main_blueprint)
# app.register_blueprint(engine_blueprint, url_prefix='/engine')

socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message: '+ msg)
    senf(msg, broadcast=True)


if __name__ == '__main__':
	# dont change the port number- its compatible with the vps.
    # app.run(debug=True, host='0.0.0.0', port=1999)
    socketio.run(app)