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

    db_session.commit()
    # results = URL.query.all()
    # pp.pprint(results)

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

    url1 = URL(util.hash_domain('https://googo.com/gmail/1/2/3/4'), util.hash_url('https://googo.com/gmail/1/2/3/4'))
    url2 = URL(util.hash_domain('https://docs.googollll.com/spreadsheets/u/04/'), util.hash_url('https://docs.googollll.com/spreadsheets/u/04/'))
    url3 = URL(util.hash_domain('https://docs.googollll.com/document/u/1/1'), util.hash_url('https://docs.googollll.com/document/u/1/1'))
    url4 = URL(util.hash_domain('https://www.appa3.com/mac/index.html'), util.hash_url('https://www.appa3.com/mac/index.html'))
    url5 = URL(util.hash_domain('https://www.appa3.com/ipad/stuff.htm'), util.hash_url('https://www.appa3.com/ipad/stuff.htm'))

    test_insert()
    test_compare()
    cleanup()
