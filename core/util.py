#!/usr/bin/env python3
import hashlib
from urllib.parse import urlparse

"""
Utility methods for hashing, searching, and parsing URLs
"""
def parse_domain(raw_url):
    if (raw_url == None):
        return ""
    return urlparse(raw_url).hostname

def hash_filter(raw_url):
    if (raw_url == None):
        return ""
    # Strip off extraneous fields
    path = urlparse(raw_url).path
    return bytes(hashlib.md5(path.encode('utf-8')).hexdigest(), 'utf-8')

def in_domain(rs, hash_url):
    if (len(rs) == 0):
        return False

    for domain in rs:
        if(domain.hash_url == hash_url):
            return True
    return False
