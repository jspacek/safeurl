#!/usr/bin/env python3
import hashlib
from urllib.parse import urlparse

"""
Utility methods for hashing and parsing URLs
"""
def parse_domain(raw_url):
    # TODO handle None and nulls, and strange formats, https, etc.
    print(raw_url)
    return urlparse(raw_url).hostname

def hash_filter(raw_url):
    return bytes(hashlib.md5(raw_url.encode('utf-8')).hexdigest(), 'utf-8')
