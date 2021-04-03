from flask import Flask, Blueprint
from routes.main_blueprint import *
from routes.engine_blueprint import *

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(engine_blueprint, url_prefix='/engine')



if __name__ == '__main__':
	# dont change the port number- its compatible with the vps.
    app.run(host='0.0.0.0', port=1999)
