#!/usr/bin/python3
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
from api.v1.views import app_views


API_HOST = getenv('HBNB_API_HOST')
API_PORT = getenv('HBNB_API_PORT')
app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_request(self):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT, threaded=True)
