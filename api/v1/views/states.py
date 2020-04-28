#!/usr/bin/python3
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
from api.v1.views.__init__ import app_views
from api.v1.app import app


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_route4(text='is cool'):