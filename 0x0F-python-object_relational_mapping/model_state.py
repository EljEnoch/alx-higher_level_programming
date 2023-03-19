#!/usr/bin/python3

"""
class State
inherit from Base
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ State class """
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
