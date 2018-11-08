#!/usr/bin/env python3

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from model import URL
from core import util
from db import db_session
import pprint

"""
Delete all of the data in the database
"""
pp = pprint.PrettyPrinter(indent=4)

def delete():
    results = URL.query.all()
    pp.pprint(len(results))

    URL.query.delete()
    db_session.commit()
    results = URL.query.all()
    pp.pprint(len(results))

if __name__ == '__main__':

    delete()
