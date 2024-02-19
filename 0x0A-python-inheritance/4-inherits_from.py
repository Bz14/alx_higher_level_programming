#!/usr/bin/python3
""" Check if object is an instance or not """


def inherits_from(obj, a_class):
    """ Return true if instance elase return false """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
