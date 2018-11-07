#!/usr/bin/env python3
import hashlib
from urllib.parse import urlparse
from random import randint

"""
Utility methods for hashing, searching, and parsing URLs
Load balancing algorithm
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

def two_choice_load_balance(db_strings, usages):
    # 2-choice randomized load balancing algorithm maximum load bound is O(log log n/log 2) + theta(1)
    # (See Mitzenmacher d-choice randomized selection, where d=2)

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
