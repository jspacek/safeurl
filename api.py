#!/usr/bin/env python3

from flask_restful import Resource, Api
from model import URL
from core import util

class URLInfo(Resource):
    def get(self, url):
        # TODO connect this piece to the DB
        return {'exists': "true"}
