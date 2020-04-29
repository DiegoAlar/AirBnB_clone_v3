#!/usr/bin/python3
""" init file
"""


from flask import Flask, jsonify, Blueprint


app_views = Blueprint('app_views', __name__)
from api.v1.views.index import *
from api.v1.views.states import *
