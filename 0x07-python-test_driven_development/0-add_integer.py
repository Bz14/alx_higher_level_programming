#!/usr/bin/python3
""" A module for adding two integers or floats """


def add_integer(a, b=98):
    """ Return the integer addition of a and b
    Float arguments will be casted to integer
    Raises:
        TypeError: If either a or b is  not integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
