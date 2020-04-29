#!/usr/bin/python3
""" Amenity """
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response, request, abort
from models import storage
from api.v1.views import app_views
from api.v1 import app
from models.place import Place
from models.city import City
from models.user import User


mets = ['GET', 'POST']
mets_id = ['GET', 'DELETE', 'PUT']


@app_views.route('/places/<place_id>', strict_slashes=False, methods=mets_id)
def places_routes(place_id=None):
    """ Places_routes """
    objs = storage.all('Place')
    if place_id:
        key = "Place." + place_id
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
            new_place = Place(**data)
            storage.new(new_place)
            storage.save()
            return make_response(jsonify(new_place.to_dict()), 201)
        places_list = []
        for obj in objs.values():
            places_list.append(obj.to_dict())
        return jsonify(places_list)

@app_views.route('/cities/<city_id>/places', strict_slashes=False, methods=mets)
def places_routes2(city_id=None):
    """ Places_routes """
    objs_city = storage.all('City')
    objs_places = storage.all('Places')
    objs_users = storage.all('User')
    all_places = []
    if city_id:
        key = "City." + city_id
        obj = objs_city.get(key)
        if obj is None:
            abort(404)
        if request.method == 'GET':
            for place in objs_places.values():
                if place.city_id == city_id:
                    all_places.append(place.to_dict())
            return jsonify(all_places)
        elif request.method == 'POST':
            if not request.get_json():
                return ('Not a JSON'), 400
            data = request.get_json()
            if not data['user_id']:
                return ('Missing user_id'), 400
            key_usr = "User." + data['user_id']
            obj_user = objs_users.get(key_usr)
            if obj_user is None:
                abort(404)
            if not data['name']:
                return ('Missing name'), 400
            data['city_id'] = city_id
            new_place = Place(**data)
            storage.new(new_place)
            storage.save()
            return make_response(jsonify(new_place.to_dict()), 201)