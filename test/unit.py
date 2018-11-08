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
    pp.pprint(".....Starting test_parse_domain test. No news is good news.")
    assert util.parse_domain(raw_url) == raw_domain

def test_parse_url(raw_url, parsed_url):
    pp.pprint(".....Starting test_parse_url test. No news is good news.")
    assert util.parse_url(raw_url) == parsed_url

def test_hash_filter(raw_url, hash_url):
    pp.pprint(".....Starting test_hash_filter test. No news is good news.")
    assert util.hash_filter(raw_url) == hash_url

def test_in_domain_true(test_list, hash_url):
    pp.pprint(".....Starting test_in_domain_true test. No news is good news.")
    pp.pprint(test_list)
    pp.pprint(hash_url)
    assert util.in_domain(test_list, hash_url) == True

def test_in_domain_false(test_list, hash_url):
    pp.pprint(".....Starting test_in_domain_false test. No news is good news.")
    assert util.in_domain(test_list, hash_url) == False

if __name__ == '__main__':
    test_raw_url1 = "https://google.com/gmail/"
    test_raw_url2 = "https://go.google.com/somethingelse"
    test_raw_url3 = "http://stuffandthings.co.au/somethingelse/anotherthing&andparams=true"
    test_raw_url4 = "http://www.stuffandthings.co.au/somethingelse/anotherthing&andparams=true"
    test_raw_url5 = "http://www2.stuffandthings.co.au:8080/somethingelse/anotherthing&andparams=true"
    test_raw_notincl = "http://bananasare.bananas"

    test_domain1 = "google.com"
    test_domain2 = "go.google.com"
    test_domain3 = "stuffandthings.co.au"
    test_domain4 = "www.stuffandthings.co.au"
    test_domain5 = "www2.stuffandthings.co.au"

    test_parse_url1 = "https://google.com/gmail/"
    test_parse_url2 = "https://go.google.com/somethingelse"
    test_parse_url3 = "http://stuffandthings.co.au/somethingelse/anotherthing"
    test_parse_url4 = "http://www.stuffandthings.co.au/somethingelse/anotherthing"
    test_parse_url5 = "http://www.stuffandthings.co.au:8080/somethingelse/anotherthing/yaya.html"

    test_parse_path1 = "httpsgoogle.com/gmail"
    test_parse_path2 = "httpsgo.google.com/somethingelse"
    test_parse_path3 = "httpstuffandthings.co.au/somethingelse/anotherthing"
    test_parse_path4 = "httpwww.stuffandthings.co.au/somethingelse/anotherthing"
    test_parse_path5 = "http8080www.stuffandthings.co.au/somethingelse/anotherthing/yaya.html"

    test_list = []
    url1 = URL(util.hash_domain(test_raw_url1), util.hash_url(test_raw_url1))
    url2 = URL(util.hash_domain(test_raw_url2), util.hash_url(test_raw_url2))
    url3 = URL(util.hash_domain(test_raw_url3), util.hash_url(test_raw_url3))
    url4 = URL(util.hash_domain(test_raw_url4), util.hash_url(test_raw_url4))
    url5 = URL(util.hash_domain(test_raw_url5), util.hash_url(test_raw_url5))

    test_list.append(url1)
    test_list.append(url2)
    test_list.append(url3)
    test_list.append(url4)
    test_list.append(url5)

    # Domain parsing tests
    test_parse_domain(test_raw_url1, test_domain1)
    test_parse_domain(test_raw_url2, test_domain2)
    test_parse_domain(test_raw_url3, test_domain3)
    test_parse_domain(test_raw_url4, test_domain4)
    test_parse_domain(test_raw_url5, test_domain5)

    # URL parsing tests
    test_parse_url(test_parse_url1, test_parse_path1)
    test_parse_url(test_parse_url2, test_parse_path2)
    test_parse_url(test_parse_url3, test_parse_path3)
    test_parse_url(test_parse_url4, test_parse_path4)
    test_parse_url(test_parse_url5, test_parse_path5)

    # Domain match test
    test_in_domain_true(test_list, util.hash_url(test_raw_url1))
    test_in_domain_true(test_list, util.hash_url(test_raw_url2))
    test_in_domain_true(test_list, util.hash_url(test_raw_url3))
    test_in_domain_true(test_list, util.hash_url(test_raw_url4))
    test_in_domain_true(test_list, util.hash_url(test_raw_url5))
    test_in_domain_false(test_list, util.hash_url(test_raw_notincl))

    pp.pprint("Unit tests passed")
