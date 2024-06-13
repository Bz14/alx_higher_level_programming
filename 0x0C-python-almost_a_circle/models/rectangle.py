#!/usr/bin/python3
""" Rectangel module"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Getter for width """
    @property
    def width(self):
        """ Getter for width """
        return self.__width

    """Setter for width """
    @width.setter
    def width(self, value):
        """ Setter for width """
        self.__width = value

    """ Getter for height  """
    @property
    def height(self):
        """ Getter for height """
        return self.__height

    """Setter for height """
    @height.setter
    def height(self, value):
        """ Setter for height """
        self.__height = value

    """ Getter for x """
    @property
    def x(self):
        """ Getter for x """
        return self.__x

    """Setter for x """
    @x.setter
    def x(self, value):
        """ Setter for x """
        self.__x = value

    """ Getter for y """
    @property
    def y(self):
        """ Getter for y """
        return self.__y

    """Setter for y """
    @y.setter
    def y(self, value):
        """ Setter for y """
        self.__y = value
