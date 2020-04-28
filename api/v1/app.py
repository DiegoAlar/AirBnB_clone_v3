#!/usr/bin/python3
from os import getenv
from flask import Flask, jsonify, Blueprint
from models import storage
from api.v1.views.__init__ import app_views


API_HOST = getenv('HBNB_API_HOST')
API_PORT = getenv('HBNB_API_PORT')
app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_request(self):
    storage.close()


if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT, threaded=True)
