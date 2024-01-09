#!/usr/bin/python3
""" A module to define a class """


class Student:
    """ A student class """
    def __init__(self, first_name, last_name, age):
        """ Initializing the instances """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary representation"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace the attribute of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
