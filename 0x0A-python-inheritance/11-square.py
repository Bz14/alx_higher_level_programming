#!/usr/bin/python3
""" A module to define a square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A square class """
    def __init__(self, size):
        """ Initialize the size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ An area function"""
        return self.__size ** 2

    def __str__(self):
        """ To string method """
        return f"[Square] {self.__size}/{self.__size}"
