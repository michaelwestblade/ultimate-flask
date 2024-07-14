from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1,2,3], 'key3': True})

@app.route('/json',methods=['POST'])
def json_post():
    return jsonify({'key': 'value', 'key2': [1,2,3], 'key3': True})

@app.route('/home/<name>', defaults={'name':'Computer'})
def home(name):
    return f'Hello, {name}'

@app.route('/<name>')
def index(name):
    return f'<p>Hello, {name}!</p>'