import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from model import URL
from core import util
from db import db_session
import pprint

"""
Insert large volumes of data from urlhaus
"""
pp = pprint.PrettyPrinter(indent=4)

def populate():
    # 3 massive file read
    db_session.add(url1)
    db_session.add(url2)
    db_session.add(url3)
    db_session.commit()
    results = URL.query.all()
    pp.pprint(results)

if __name__ == '__main__':
    # 1 parse large or small argument

    #2 massive hash
    url1 = URL(util.hash_filter('google.com'), util.hash_filter('https://google.com/gmail/'))


    populate()
