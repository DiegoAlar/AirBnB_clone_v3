#!/usr/bin/python3
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
from api.v1.views import app_views
from api.v1 import app

@app.route('/states', methods=['GET', 'POST'])
@app.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def states_routes(state_id=None):
    objs = storage.all('State')
    if state_id:
        key = "State." + id
        obj = objs.get(key)
        if request.method == 'GET':
            if obj:
                return jsonify(obj)
            else:
                abort(404)
        elif request.method == 'DELETE':
            if obj:
                storage.delete(obj)
                return make_response(jsonify({}), 200)
            else:
                abort(404)
        elif request.method == 'POST':
            pass
        elif request.method == 'PUT':
            pass
    else:
        states_list = []
        for obj in objs.values():
            states_list.append(obj.to_dict())
        return jsonify(states_list)
