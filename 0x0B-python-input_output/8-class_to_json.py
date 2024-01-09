#!/usr/bin/python3
""" A module to return the dictionary discription of some data structures. """


def class_to_json(obj):
    """ Function to return dictionary representation of an object """
    return obj.__dict__
