#!/usr/bin/python3
""" A module to check subclass or not """


def inherits_from(obj, a_class):
    """ Check whether an instance or not
    Args:
      obj: an object
      a_class: a class
    Returns: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
