import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from model import URL
from core import util
from db import db_session
from sqlalchemy import exc
import pprint

"""
Insert small or large volumes of data from urlhaus
Choose urlhaus_malware_large or urlhaus_malware_small
"""
pp = pprint.PrettyPrinter(indent=4)

"""
Perform a bulk insert using the rows in the file
"""
def populate(file):

    pp.pprint("parsing file %s" % file)
    file_reader = open(file,"r")
    url_objects = []
    for line in file_reader:
        if not line.startswith("#"):
            pp.pprint(line)
            line = line.strip()
            line = line.strip("'")
            line = line.strip("\n")
            pp.pprint(line)
            url = URL(util.hash_domain(line), util.hash_url(line))
            if (not url.hash_domain == "" and not url.hash_url == ""):
                url_objects.append(url)
                db_session.add(url)
            db_session.commit()

    pp.pprint(url_objects)

    """
    TODO: this doesn't work with the large data set, perhaps there is a max without any errors?
    Will create a SQL script to insert manually into DB

    try:
        db_session.bulk_save_objects(url_objects)
        db_session.commit()
    except exc.IntegrityError:
        db_session.rollback()
    """
    results = URL.query.all()

    pp.pprint("Inserted %d rows" % len(results))

if __name__ == '__main__':
    # Parse file argument
    print ("Number of arguments: %d" % len(sys.argv))
    if (len(sys.argv) < 2):
        print ('Usage: populate_urlhaus.py <inputfile>')
        sys.exit(2)

    populate(sys.argv[1])
