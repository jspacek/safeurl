#!/usr/bin/env python3

from flask_restful import Resource, Api
from model import URL
from core import util

"""
Business logic for the API calls
"""
class URLInfo(Resource):
    def get(self, url):
        # First, query for the hashed domain
        domain = util.parse_domain(url)
        hash_raw_domain = util.hash_filter(domain)
        domain_resulset = URL.query.filter(URL.hash_domain == hash_raw_domain).all()
        #print(domain_resulset)
        if (len(domain_resulset) > 0):
            # Search within the local domain resulset for the hashed URL
            hash_raw_url = util.hash_filter(url)
            #print(hash_raw_url)
            for domain in domain_resulset:
                if(domain.hash_url == hash_raw_url):
                    return {'exists': "true"}
            return {'exists': "false"}
        else:
            return {'exists': "false"}
