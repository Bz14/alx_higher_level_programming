#!/usr/bin/python3
""" A function to add two numbrs """


def add_integer(a, b=98):
    """ Add integer function """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
