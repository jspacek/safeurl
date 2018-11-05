#!/usr/bin/env python3

from sqlalchemy import Column, Binary, Integer
from db import Base, init_db
from core import util

"""
ORM wrapper for a URL row, connects the API and DB
"""

class URL(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    hash_domain = Column(Binary(32), nullable=False, index=True)
    hash_url = Column(Binary(32), nullable=False, unique=True)

    def __init__(self, hash_domain=None, hash_url=None):
        self.hash_domain = hash_domain
        self.hash_url = hash_url

    def __repr__(self):
        return '<URL %s %s>' % (self.hash_domain, self.hash_url)
