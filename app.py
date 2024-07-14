import sqlite3

from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"

def connect_db():
    sqlite_db = sqlite3.connect("data.db")
    sqlite_db.row_factory = sqlite3.Row
    return sqlite_db

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/json')
def json():
    name = session['name']
    return jsonify({'key': 'value', 'key2': [1,2,3], 'key3': True, 'name': name})

@app.route('/json',methods=['POST'])
def json_post():
    return jsonify({'key': 'value', 'key2': [1,2,3], 'key3': True})

@app.route('/home', defaults={'name': 'Default'})
@app.route('/home/<name>')
def home(name):
    session['name'] = name

    db = get_db()
    cur = db.execute('SELECT * FROM users')
    results = cur.fetchall()

    return render_template('home.html', name=name, display=False, list_of_dicts=[{'name': 'tester'}, {'name': 'tester2'}, {'name': 'tester3'}], results=results)

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

    db = get_db()
    db.execute('INSERT INTO users (name, location) VALUES (?, ?)', (name, location))
    db.commit()

    return f'Name: {name}, Location: {location}'

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['name']
    location = data['location']

    db = get_db()
    db.execute('INSERT INTO users (name, location) VALUES (?, ?)', (name, location))
    db.commit()

    return jsonify({'name': name, 'location': location})

@app.route('/redirect')
def redirect_handler():
    return redirect(url_for('home'))

@app.route('/viewresults')
def viewresults():
    db = get_db()
    cur = db.execute('SELECT id, name, location from users')
    results = cur.fetchall()
    return [{"name": result["name"], "location": result["location"]} for result in results]