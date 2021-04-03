from flask import Flask, Blueprint
from main_blueprint import main_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)

# we can register routes with specific prefix
# app.register_blueprint(urls2_blueprint, url_prefix='/urls2')


if __name__ == '__main__':
	# dont change the port number- its compatible with the vps.
    app.run(host='0.0.0.0', port=1999)
