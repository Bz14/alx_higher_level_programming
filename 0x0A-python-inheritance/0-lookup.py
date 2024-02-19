#!/usr/bin/python3
""" List available attributes """


def lookup(obj):
    """ Return list of available attributes """
    return dir(obj)
