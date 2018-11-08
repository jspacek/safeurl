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
    db_session.add(url4)
    db_session.add(url5)

    db_session.commit()
    results = URL.query.all()
    pp.pprint(results)

if __name__ == '__main__':

    url1 = URL(util.hash_domain('https://googo.com/gmail'), util.hash_url('https://googo.com/gmail'))
    url2 = URL(util.hash_domain('https://docs.googo.com/spreadsheets/u/01/'), util.hash_url('https://docs.googo.com/spreadsheets/u/01/'))
    url3 = URL(util.hash_domain('https://docs.googo.com/document/u/0/1'), util.hash_url('https://docs.googo.com/document/u/0/1'))
    url4 = URL(util.hash_domain('https://www.appa.com/mac/index.html'), util.hash_url('https://www.appa.com/mac/index.html'))
    url5 = URL(util.hash_domain('https://www.appa.com/ipad/stuff.htm'), util.hash_url('https://www.appa.com/ipad/stuff.htm'))


    populate()
