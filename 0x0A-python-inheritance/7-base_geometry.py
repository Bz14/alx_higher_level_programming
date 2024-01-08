#!/usr/bin/python3
""" A module to define a geometry class """


class BaseGeometry:
    """ An empty class """
    def area(self):
        """ An area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
