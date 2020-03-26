from flask import Flask, jsonify, request
from flask_sqlalchemy
app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello, World!')


@app.route('/greetings')
def greetings():
    # return 'Hello from the Planetary API.'
    return jsonify(message='Hello from the Planetary API.')

@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


# Adding parameters to api end points
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f"Sorry, {name}. At {age} years of age you're not old enough to access this API.")
    else:
        return jsonify(message=f"Welcome to the API, {name}!")


# URL variables
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message=f"Sorry, {name}. At {age} years of age you're not old enough to access this API.")
    else:
        return jsonify(message=f"Welcome to the API, {name}!")























if __name__ == '__main__':
    app.run()


# app.run(port=5000)            If we want to run server on port 5000
# $env:FLASK_APP = "app.py"     Export the FLASK_APP environment variable
# $env:FLASK_ENV=development    Turn on # DEBUG mode
# python -m flask run           Run the application
