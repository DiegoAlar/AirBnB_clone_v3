#!/usr/bin/python3
""" index file
"""


from api.v1.views import app_views
from flask import Flask, jsonify, Blueprint
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ show status """
    status = {
            'status': 'OK'
        }
    return jsonify(status)


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Show stats """
    stats = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
        }
    return jsonify(stats)
