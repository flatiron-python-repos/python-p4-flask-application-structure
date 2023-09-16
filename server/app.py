#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to me</h1>'

@app.route('/<int:id>')
def user_id(id):
    return f'user id passed in parameter is: {id}'


if __name__ == '__main__':
    app.run(port=8001)