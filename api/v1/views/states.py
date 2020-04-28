#!/usr/bin/python3
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response, request, abort
from models import storage
from api.v1.views import app_views
from api.v1 import app
from models.state import State

@app_views.route('/states', strict_slashes=False, methods=['GET', 'POST'])
@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET', 'DELETE', 'PUT'])
def states_routes(state_id=None):
    objs = storage.all('State')
    if state_id:
        key = "State." + state_id
        obj = objs.get(key)
        if obj is None:
            abort(404)
        if request.method == 'GET':
            return jsonify(obj.to_dict())
        elif request.method == 'DELETE':
            storage.delete(obj)
            return make_response(jsonify({}), 200)
        elif request.method == 'PUT':
            if not request.get_json():
                return ('Not a JSON'), 400
    else:
        if request.method == 'POST':
            if not request.get_json():
                return ('Not a JSON'), 400
            data = request.get_json()
            if not data['name']:
                return ('Missing name'), 400
            new_state = State(data)
            return (new_state.to_dict()), 201
        states_list = []
        for obj in objs.values():
            states_list.append(obj.to_dict())
        return jsonify(states_list)
