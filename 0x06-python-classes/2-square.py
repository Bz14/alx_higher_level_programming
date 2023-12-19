#!/usr/bin/python3
"""Module for square class"""


class Square:
    """This is a square class"""
    def __init__(self, size=0):
        """This is the init function."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
