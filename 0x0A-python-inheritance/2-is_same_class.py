#!/usr/bin/python3
""" Checking an object is an instance of a class or not """


def is_same_class(obj, a_class):
    """ Return true if instance else return False """
    if type(obj) == a_class:
        return True
    return False
