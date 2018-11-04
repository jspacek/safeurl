#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import model

"""
Boilerplate code from SQLAlchemy
"""

engine = create_engine('sqlite:///safeurl1.db', convert_unicode=True, echo=False)
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
