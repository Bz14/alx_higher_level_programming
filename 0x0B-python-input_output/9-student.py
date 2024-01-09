#!/usr/bin/python3
""" A module to define a class """


class Student:
    """ A student class """
    def __init__(self, first_name, last_name, age):
        """ Initializing the instances """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns the dictionary representation"""
        return self.__dict__
