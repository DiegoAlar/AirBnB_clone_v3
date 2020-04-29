#!/usr/bin/python3
"""Status of your API"""
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
from api.v1.views import app_views


API_HOST = getenv('HBNB_API_HOST')
API_PORT = getenv('HBNB_API_PORT')
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_request(self):
    """teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """not found"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT, threaded=True)
