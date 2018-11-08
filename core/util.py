#!/usr/bin/env python3
import hashlib
from urllib.parse import urlparse
from random import randint

"""
Utility methods for hashing, searching, and parsing URLs
"""
def hash_domain(raw_url):
    if (raw_url == None):
        return ""
    domain = parse_domain(raw_url)
    return bytes(hashlib.md5(domain.encode('utf-8')).hexdigest(), 'utf-8')

def hash_url(raw_url):
    if (raw_url == None):
        return ""
    path = parse_url(raw_url)
    return bytes(hashlib.md5(path.encode('utf-8')).hexdigest(), 'utf-8')

def parse_domain(raw_url):
    if (raw_url == None):
        return ""
    return urlparse(raw_url).hostname

def parse_url(raw_url):
    if (raw_url == None):
        return ""
    # Strip off extraneous fields & remove any last trailing "/"
    path = urlparse(raw_url).path
    if path.endswith('/'):
        path = path[:-1]
    return path

def in_domain(rs, hash_url):
    if (len(rs) == 0):
        return False
    for domain in rs:
        if(domain.hash_url == hash_url):
            return True
    return False

"""
    # 2-choice randomized load balancing algorithm maximum load bound is O(log log n/log 2) + theta(1)
    # (See Mitzenmacher d-choice randomized selection, where d=2)
    @article{richa2001power,
      title={The power of two random choices: A survey of techniques and results},
      author={Richa, Andrea W and Mitzenmacher, M and Sitaraman, R},
      journal={Combinatorial Optimization},
      volume={9},
      pages={255--304},
      year={2001}
    }
"""
def two_choice_load_balance(db_strings, usages):

    # 1) Select two DB instances randomly
    instance1 = randint(0, len(usages)-1)
    instance2 = randint(0, len(usages)-1)

    # 2) Choose the lighter loaded proxy and increment usage
    if (usages[instance1] <= usages[instance2]):
        db_string = db_strings[instance1]
        usages[instance1] = usages[instance1] + 1
    else:
        db_string = db_strings[instance2]
        usages[instance2] = usages[instance2] + 1
    #print(usages)

    return db_string
