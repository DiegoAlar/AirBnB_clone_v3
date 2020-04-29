#!/usr/bin/python3
"""State"""
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response, request, abort
from models import storage
from api.v1.views import app_views
from api.v1 import app
from models.state import State
from models.city import City


mets = ['GET', 'POST']
mets_id = ['GET', 'DELETE', 'PUT']


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=mets_id)
def cities_routes(city_id=None):
    """ Cities_routes """
    objs = storage.all('City')
    if city_id:
        key = "City." + city_id
        obj = objs.get(key)
        if obj is None:
            abort(404)
        if request.method == 'GET':
            return jsonify(obj.to_dict())
        elif request.method == 'DELETE':
            storage.delete(obj)
            storage.save()
            return make_response(jsonify({}), 200)
        elif request.method == 'PUT':
            if not request.get_json():
                return ('Not a JSON'), 400
            data = request.get_json()
            for k, v in data.items():
                setattr(obj, k, v)
            storage.save()
            return make_response(jsonify(obj.to_dict()), 200)
    else:
        if request.method == 'POST':
            if not request.get_json():
                return ('Not a JSON'), 400
            data = request.get_json()
            if not data['name']:
                return ('Missing name'), 400
            new_city = State(**data)
            storage.new(new_city)
            storage.save()
            return make_response(jsonify(new_city.to_dict()), 201)
        cities_list = []
        for obj in objs.values():
            cities_list.append(obj.to_dict())
        return jsonify(cities_list)

@app_views.route('/states/<state_id>/cities', strict_slashes=False, methods=mets)
def cities_routes2(state_id=None):
    """ return city objects """
    objs = storage.all('State')
    if state_id:
        key = "State." + state_id
        obj = objs.get(key)
        if obj is None:
            abort(404)
        if request.method == 'GET':
            cities_list = []
            for obj in objs.values():
                if obj.state_id == state_id:
                    cities_list.append(obj.to_dict())
            return jsonify(cities_list)
        elif request.method == 'POST':
            if not request.get_json():
                return ('Not a JSON'), 400
            data = request.get_json()
            if not data['name']:
                return ('Missing name'), 400
            data['state_id'] = state_id
            new_city = City(**data)
            storage.new(new_city)
            storage.save()
            return make_response(jsonify(new_city.to_dict()), 201)