#!/usr/bin/python3
""" A module to define a rectangel """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangel class """
    def __init__(self, width, height):
        """ Initialize width an d height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ An area function"""
        return self.__width * self.__height

    def __str__(self):
        """ To string method """
        return f"[Rectangle] {self.__width}/{self.__height}"
