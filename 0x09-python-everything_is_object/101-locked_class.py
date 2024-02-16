#!/usr/bin/python3
""" Define a locked class """



class LockedClass:
    """ Prevent the user from instantiating untill the attributes called first_name """

    __slots__ = ['first_name']
