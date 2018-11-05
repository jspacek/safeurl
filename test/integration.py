#!/usr/bin/env python3

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from model import URL
from core import util
from db import db_session
import pprint

"""
Integration tests to connect to the live DB to test all the connecting parts.
Any insertions are deleted at cleanup. No modification of real data.
"""
pp = pprint.PrettyPrinter(indent=4)

def cleanup():
    db_session.delete(url1)
    db_session.delete(url2)
    db_session.delete(url3)
    db_session.delete(url4)
    db_session.delete(url5)
    # Delete entire table
    URL.query.delete()

    db_session.commit()
    results = URL.query.all()
    pp.pprint(results)

def test_insert():
    db_session.add(url1)
    db_session.add(url2)
    db_session.add(url3)
    db_session.commit()
    results = URL.query.filter(URL.hash_domain == url2.hash_domain).all()
    size = len(results)
    if (size !=2):
        print("test_insert Failed. Wanted 2 results, got %d" % size)
        return
    print("test_insert passed")
    pp.pprint(results)

def test_compare():
    db_session.add(url4)
    db_session.add(url5)
    db_session.commit()
    results = URL.query.filter(URL.hash_domain == url4.hash_domain)
    if (results.count() != 2):
        print("test_compare Failed. Wanted 2 results, got %d" % results.count())
        return
    print("test_compare passed")
    pp.pprint(results[0])
    pp.pprint(results[1])

if __name__ == '__main__':

    url1 = URL(util.hash_filter('google.com'), util.hash_filter('https://googo.com/gmail'))
    url2 = URL(util.hash_filter('docs.googo.com'), util.hash_filter('https://docs.googo.com/spreadsheets/u/01/'))
    url3 = URL(util.hash_filter('docs.googo.com'), util.hash_filter('https://docs.googo.com/document/u/0/1'))
    url4 = URL(util.hash_filter('apple.com'), util.hash_filter('https://www.appa.com/mac/index.html'))
    url5 = URL(util.hash_filter('apple.com'), util.hash_filter('https://www.appa.com/ipad/stuff.htm'))

    test_insert()
    test_compare()
    cleanup()
