from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"

@app.route('/json')
def json():
    name = session['name']
    return jsonify({'key': 'value', 'key2': [1,2,3], 'key3': True, 'name': name})

@app.route('/json',methods=['POST'])
def json_post():
    return jsonify({'key': 'value', 'key2': [1,2,3], 'key3': True})

@app.route('/home/<name>')
def home(name):
    session['name'] = name
    return f'Hello, {name}'

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'Name: {name}, Location: {location}'

@app.route('/theform')
def theform():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    location = request.form.get('location')

    return f'Name: {name}, Location: {location}'

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['name']
    location = data['location']

    return jsonify({'name': name, 'location': location})

@app.route('/redirect')
def redirect_handler():
    return redirect(url_for('home'))