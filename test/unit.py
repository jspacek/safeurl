#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
import pytest
from model import URL
from core import util
from db import db_session
import pprint

"""
Unit tests for utility functions
"""
pp = pprint.PrettyPrinter(indent=4)

def test_parse_domain(raw_url):
    assert util.parse_domain(raw_url) == test_domain

def test_hash_filter(raw_url):
    assert util.hash_filter(raw_url) == test_hash_url1

def in_domain_true(test_list, hash_url):
    #pp.pprint(test_list)
    assert util.in_domain(test_list, hash_url) == True

def in_domain_false(test_list, hash_url):
    assert util.in_domain(test_list, hash_url) == False

if __name__ == '__main__':
    test_raw_url1 = "https://google.com/gmail/"
    test_hash_url1 = b'd8f6542f4fc22b7cfa3771dc0ba8525d'
    test_hash_url2 = b'd8f6542f4fc22b7cfa3771dc0ba8525e'
    test_domain = "google.com"
    test_list = []
    test_list.append(URL(b'1d5920f4b44b27a802bd77c4f0536f5a', b'd8f6542f4fc22b7cfa3771dc0ba8525d'))
    test_list.append(URL(b'1d5920f4b44b27a802bd77c4f0536f5a', b'bf3f6fb34e3ff4f8a3d9b3cb3f3321fa'))
    test_list.append(URL(b'1d5920f4b44b27a802bd77c4f0536f5a', b'0e6b371b318bbe913e07cca553fbc9bc'))

    test_parse_domain(test_raw_url1)
    test_hash_filter(test_raw_url1)
    in_domain_true(test_list, test_hash_url1)
    in_domain_false(test_list, test_hash_url2)

    print("Unit tests passed")
