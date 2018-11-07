#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
import pytest
import pprint
from core import util
from math import log

"""
Unit tests for db load balancing
"""
pp = pprint.PrettyPrinter(indent=4)


def test_100_connections(db_strings, usages):

    for number in range (100):
        db_string = util.two_choice_load_balance(db_strings, usages)
    print(usages)
    maximum_load = max(usages)
    upper_bound = log(log(100))/log (2) + 1
    print("test_100_connections")
    print("Maximum Load %d" % maximum_load)
    print("Upper Bound %d" % upper_bound)
    assert maximum_load <= upper_bound

def test_1000_connections(db_strings, usages):

    for number in range (1000):
        db_string = util.two_choice_load_balance(db_strings, usages)
    #print(usages)
    maximum_load = max(usages)
    upper_bound = log(log(1000))/log (2) + 1
    print("test_1000_connections")
    print("Maximum Load %d" % maximum_load)
    print("Upper Bound %d" % upper_bound)
    assert maximum_load <= upper_bound

def test_10000_connections(db_strings, usages):

    for number in range (10000):
        db_string = util.two_choice_load_balance(db_strings, usages)
    #print(usages)
    maximum_load = max(usages)
    upper_bound = log(log(10000))/log (2) + 1
    print("test_10000_connections")
    print("Maximum Load %d" % maximum_load)
    print("Upper Bound %d" % upper_bound)
    assert maximum_load <= upper_bound

if __name__ == '__main__':

    db_strings_100 = ["" for x in range(100)]
    usages100 = [0 for x in range(100)]
    test_100_connections(db_strings_100, usages100)

    db_strings_1000 = ["" for x in range(1000)]
    usages1000 = [0 for x in range(1000)]
    test_1000_connections(db_strings_1000, usages1000)

    db_strings_10000 = ["" for x in range(10000)]
    usages10000 = [0 for x in range(10000)]
    test_10000_connections(db_strings_10000, usages10000)

    # TODO test when # of clients >> # of servers
    print("DB unit tests passed")
