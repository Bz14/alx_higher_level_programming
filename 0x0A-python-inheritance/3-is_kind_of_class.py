#!/usr/bin/python3
""" A module to check whether an object is instance or not """


def is_kind_of_class(obj, a_class):
    """ Check whether an instance or not
    Args:
      obj: an object
      a_class: a class
   Returns: True or False
   """
    return isinstance(obj, a_class)
