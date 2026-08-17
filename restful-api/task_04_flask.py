#!/usr/bin/python3
"""Flask API application."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Return welcome message for root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return API status."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user dictionary for given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the users dictionary."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
