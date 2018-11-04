#!/usr/bin/env python3
import hashlib

"""
Utility methods for hashing and parsing URLs
"""
def parse_domain(raw_url):
    # TODO remove extraneous characters and formats to parse domain
    pass

def hash_filter(raw_url):
    return bytes(hashlib.md5(raw_url.encode('utf-8')).hexdigest(), 'utf-8')
