#!/usr/bin/python3
""" Defines locked class."""


class LockedClass:
    """
    Prevent object instantiation except for first_name attribute.
    """
    __slots__ = ['first_name']
