from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os


app = Flask(__name__)
basedir = os.path.dirname(os.path.dirname(__file__))
app.config['MONGODB_SETTINGS'] = {
    'db': 'planetary',
    'host': 'localhost',
    'port': 27017
}


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Planetary API.')


@app.route('/profile/<string:name>/<int:age>')
def profile(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough!")
    
    
if __name__ == '__main__':
    app.run()
