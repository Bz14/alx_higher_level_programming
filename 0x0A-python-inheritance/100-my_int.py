#!/usr/bin/python3
"""A mosule contains MyInt class"""


class MyInt(int):
    """ MyInt class extending int"""

    def __eq__(self, value):
        """Equality"""
        return self.real != value

    def __ne__(self, value):
        """Inequality"""
        return self.real == value
