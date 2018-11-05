#!/usr/bin/env python3

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
import pprint
import pytest
from requests import get
from model import URL

"""
Tests live API calls to the service
Note: call test/populate.py if the database is fresh
"""
pp = pprint.PrettyPrinter(indent=4)

def test_get_true():
    response = get('http://localhost:5000/urlinfo/https://google.com/gmail/')
    assert(response.status_code == 200)
    assert(response.text=='{\n    "exists": true\n}\n')

def test_get_false_url():
    response = get('http://localhost:5000/urlinfo/https://google.com/nope/')
    assert(response.status_code == 200)
    assert(response.text=='{\n    "exists": false\n}\n')

def test_get_false_domain():
    response = get('http://localhost:5000/urlinfo/https://not.com/nope/')
    assert(response.status_code == 200)
    assert(response.text=='{\n    "exists": false\n}\n')

def test_get_false_domain_true_page():
    response = get('http://localhost:5000/urlinfo/https://not.com/gmail/')
    assert(response.status_code == 200)
    assert(response.text=='{\n    "exists": false\n}\n')

def test_get_invalid_url():
    response = get('http://localhost:5000/urlinfo/sdhkflshf&hdkjshf=ffdf')
    assert(response.status_code == 400)

print("API Tests Passed")

if __name__ == '__main__':
    test_get_true()
    test_get_false_url()
    test_get_false_domain()
    test_get_false_domain_true_page()
    test_get_invalid_url()
