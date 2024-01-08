#!/usr/bin/python3
""" This module contain a function to list
available attributes and methods of a function """


def lookup(obj):
    """ Returns list of attributes and methods
    Args:
       obj: an objecct
    Returns:
       A list of attributes and methods
    """
    return [dir(obj)]
