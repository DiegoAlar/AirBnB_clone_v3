#!/usr/bin/python3
"""Users"""
from flask import jsonify, make_response, request, abort
from models import storage
from api.v1.views import app_views
from models.state import State
from models.user import Users
from models.base_model import BaseModel


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def all_users():
    """get users"""
    a_users = storage.all("User").values()
    aux = [user.to_json() for user in a_users]
    return jsonify(aux)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def user_by_ID(user_id):
    """retrieves user by id"""
    a_user = storage.get("User", user_id)
    if a_user is None:
        return abort(404)
    return jsonify(a_user.to_json())


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['DELETE'])
def delete_user(user_id):
    """deletes by user_id"""
    a_user = storage.get("User", user_id)
    if a_user is None:
        return abort(404)
    storage.delete(a_user)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['POST'])
def new_user():
    """creates a new user"""
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    email = request_data.get('email')
    if email is None:
        abort(400, 'Missing email')
    password = request_data.get("password")
    if password is None:
        abort(400, 'Missing password')
    New_user = User(**request_data)
    New_user.save()

    return make_response(jsonify(New_user.to_json()), 201)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def Update_user(user_id):
    """Updates user"""
    keys_to_ignore = ["id", "email", "created_at", "updated_at"]
    u_user = storage.get("User", user_id)
    if not u_user:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    request_data = request.get_json()
    for k, v in json.items():
        if k not in keys_to_ignore:
            setattr(u_user, k, v)
    u_user.save()
    return make_reponse(jsonify(user.to_json()), 200)
