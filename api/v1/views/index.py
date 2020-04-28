#!/usr/bin/python3
""" index file
"""


from api.v1.views.__init__ import app_views
from flask import Flask, jsonify, Blueprint
from models import storage


@app_views.route('/status')
def status():
    """ show status """
    status = {
            "status": "OK"
        }
    return jsonify(status)


@app_views.route('/stats')
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
