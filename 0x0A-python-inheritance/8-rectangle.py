#!/usr/bin/python3
""" A module to define a rectangel """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangel class """
    def __init__(self, width, height):
        """ Initialize width an d height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
