#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api
from api import URLInfo
from db import db_session, init_db

"""
Boilerplate code from Flask-RESTful
"""

app = Flask(__name__)
api = Api(app)
api.add_resource(URLInfo,'/urlinfo/1/<path:url>')

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
