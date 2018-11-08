#!/usr/bin/env python3

from sqlalchemy import create_engine
import sqlalchemy.pool as pool
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
import model
from core import util

"""
Connect to either local dev or AWS postgres DB
"""

if config.PROD['is_prod']:
    db_strings = [config.DB['db_prod_master'], config.DB['db_prod_slave1'],config.DB['db_prod_slave2']]
    usages = [0,0,0]
    # No need to prefer master over slave at this point, because DB is read only
    db_string = util.two_choice_load_balance(db_strings, usages)
    engine = create_engine(db_string, convert_unicode=True, echo=True, pool_size=20, max_overflow=0, timeout=30)
else:
    db_string = config.DB['db_dev']
    engine = create_engine(db_string, convert_unicode=True, echo=False)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import model
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
