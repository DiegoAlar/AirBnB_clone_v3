#!/usr/bin/python3
"""Users"""
from flask import jsonify, make_response, request, abort
from models import storage
from api.v1.views import app_views
from models.state import State
from models.user import User


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def all_users():
    """get users"""
    a_users = storage.all("User").values()
    aux = [user.to_dict() for user in a_users]
    return jsonify(aux)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def user_by_ID(user_id):
    """retrieves user by id"""
    a_user = storage.get("User", user_id)
    if a_user is None:
        return abort(404)
    return jsonify(a_user.to_dict())


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['DELETE'])
def delete_user(user_id):
    """deletes by user_id"""
    try:
        a_user = storage.get('User', user_id)
        if a_user is None:
            abort(404)
        a_user.delete()
        storage.save()
        return jsonify({}), 200
    except Exception:
        abort(404)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['POST'])
def new_user():
    """creates a new user"""
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    u_dict = request.get_json()
    if "email" not in u_dict:
        return jsonify({"error": "Missing email"}), 400
    if "password" not in u_dict:
        return jsonify({"error": "Missing password"}), 400
    else:
        user_email = u_dict["email"]
        user_password = u_dict["password"]
        user = User(email=user_email, password=user_password)
        for key, value in u_dict.items():
            setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict()), 201


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
    return jsonify(u_user.to_dict()), 200
