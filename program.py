from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base action'

@app.route('/v2')
def v2():
    return 'Second action'

@app.route('/v7')
def v7():
    return 'Brichev T.U.'