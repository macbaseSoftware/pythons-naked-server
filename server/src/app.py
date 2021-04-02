from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index!'

@app.route('/users')
def users():
    return 'Users!'

    
if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
