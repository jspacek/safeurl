import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from model import URL
from core import util
from db import db_session
import pprint

"""
Initial setup of database table, populate with test data
"""
pp = pprint.PrettyPrinter(indent=4)

def populate():
    db_session.add(url1)
    db_session.add(url2)
    db_session.add(url3)
    db_session.commit()
    results = URL.query.all()
    pp.pprint(results)

url1 = URL(util.hash_filter('google.com'), util.hash_filter('https://google.com/gmail/'))
url2 = URL(util.hash_filter('google.com'), util.hash_filter('https://docs.google.com/spreadsheets/u/0/'))
url3 = URL(util.hash_filter('google.com'), util.hash_filter('https://docs.google.com/document/u/0/'))
url4 = URL(util.hash_filter('apple.com'), util.hash_filter('https://www.apple.com/mac/'))
url5 = URL(util.hash_filter('apple.com'), util.hash_filter('https://www.apple.com/ipad/'))

populate()
