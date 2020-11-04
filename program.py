from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base action'

@app.route('/v2')
def v2():
    return 'Second action'

@app.route('/v3')
def v3():
    return 'Third action'

@app.route('/v4')
def v4():
    return 'Fourth action'