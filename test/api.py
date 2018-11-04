#!/usr/bin/env python3

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
import pprint
from requests import put, get
from model import URL

"""
Tests live API calls to the service
"""
def test_get_true():
    response = get('http://localhost:5000/urlinfo/https://google.com/gmail/')
    print(response)

if __name__ == '__main__':
    test_get_true()
