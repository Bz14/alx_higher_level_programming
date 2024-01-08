#!/usr/bin/python3
"""A module to check an object is an instance of a given class."""


def is_same_class(obj, a_class):
    """ Checks an object is an instance of a clss or not
    Arguments:
        obj: an object
        a_class: a class
    Returns: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
