#!/usr/bin/python3
""" index file
"""


from api.v1.views.__init__ import app_views
from flask import Flask, jsonify, Blueprint


@app_views.route('/status')
def status():
    status = {
            "status": "OK"
        }
    return jsonify(status)
