#!/usr/bin/python3
""" Integer validator class """


class BaseGeometry:
    """ A base geometry class """
    def area(self):
        """ An area function """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ An integer validator fuction """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + "  must be greater than 0")
