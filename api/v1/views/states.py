#!/usr/bin/python3
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
from api.v1.views.__init__ import app_views
from api.v1.app import app

@app.route('/states', methods=['GET', 'POST'])
@app.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT')
def state_objs(state_id=None):
    """Retrieves all states or and specific state"""
    if state_id:
        key = "state" + id
        obj = objs.get(key)
        if request.method == 'GET'
           if obj:
           return json(obj)
           else:
