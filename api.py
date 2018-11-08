#!/usr/bin/env python3

from flask_restful import Resource, Api, abort
from model import URL
from core import util

"""
Business logic for the API calls
"""
class URLInfo(Resource):
    def get(self, url):
        # First, query for the hashed domain
        hash_raw_domain = util.hash_domain(url)
        if (hash_raw_domain == None or hash_raw_domain == ""):
            abort(400, description="BadRequest: The URL supplied is either missing or incorrectly formatted")
        domain_resulset = URL.query.filter(URL.hash_domain == hash_raw_domain).all()
        hash_raw_url = util.hash_url(url)
        # Second, search for the hashed url in the resultset
        exists = util.in_domain(domain_resulset, hash_raw_url)
        return {'exists': exists}
