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

def test_parse_domain(raw_url, raw_domain):
    assert util.parse_domain(raw_url) == raw_domain

def test_hash_filter(raw_url):
    assert util.hash_filter(raw_url) == test_hash_url1

def in_domain_true(test_list, hash_url):
    #pp.pprint(test_list)
    assert util.in_domain(test_list, hash_url) == True

def in_domain_false(test_list, hash_url):
    assert util.in_domain(test_list, hash_url) == False

if __name__ == '__main__':
    test_raw_url1 = "https://google.com/gmail/"
    test_raw_url2 = "https://go.google.com/somethingelse"

    test_hash_url1 = b'77b73e2cbe6704dfbf1cd4836a2f4ae3'
    test_hash_url2 = b'de24b5571deaea7cf4b2a5c00ef66fb7'

    test_domain1 = "google.com"
    test_domain2 = "go.google.com"
    test_list = []

    test_list.append(URL(b'1d5920f4b44b27a802bd77c4f0536f5a', b'cc52e9e63b5b628ad0af7c1fe3f83304'))
    test_list.append(URL(b'1d5920f4b44b27a802bd77c4f0536f5a', b'77b73e2cbe6704dfbf1cd4836a2f4ae3'))
    test_list.append(URL(b'1d5920f4b44b27a802bd77c4f0536f5a', b'b893128fdf787f98606dc442b7d0530c'))

    test_parse_domain(test_raw_url1, test_domain1)
    test_parse_domain(test_raw_url2, test_domain2)
    test_hash_filter(test_raw_url1)
    in_domain_true(test_list, test_hash_url1)
    in_domain_false(test_list, test_hash_url2)

    print("Unit tests passed")
