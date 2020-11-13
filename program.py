from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Action number 1'

@app.route('/v2')
def v2():
    return 'Action number 2'
