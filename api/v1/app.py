#!/usr/bin/python3
"""Status of your API"""
from flask import Flask, make_response, jsonify, Blueprint
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app_context(self):
    """teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """not found"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = '0.0.0.0'
    port = '5000'
    if getenv('HBNB_API_HOST'):
        host = getenv('HBNB_API_HOST')
    if getenv('HBNB_API_PORT'):
        port = getenv('HBNB_API_PORT')
    app.run(host=host, port=port, threaded=True)
