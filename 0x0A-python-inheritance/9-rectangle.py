#!/usr/bin/python3
""" A Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle class """
    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ An area function """
        return self.__width * self.__height
    def __str__(self):
        """ Return the string representation of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
