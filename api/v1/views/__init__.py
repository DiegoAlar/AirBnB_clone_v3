#!/usr/bin/python3
""" init file
"""


from flask import Flask, jsonify, Blueprint
from api.v1.views.index import *
import api.v1.views.states


app_views = Blueprint('app_views', __name__)
