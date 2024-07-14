from flask import Flask, jsonify, request

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

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'Name: {name}, Location: {location}'

@app.route('/theform')
def theform():
    return '''
        <form method="post" action="/process">
            <input type="text" name="name">
            <input type="text" name="location">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    location = request.form.get('location')

    return f'Name: {name}, Location: {location}'