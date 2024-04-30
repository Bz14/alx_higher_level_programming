#!/usr/bin/python3
""" Defining a model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


""" A state class """


class State(Base):
    """ Defining the columns """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all, delete')
