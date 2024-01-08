#!/usr/bin/python3
"""A mosule contains MyInt class"""


class MyInt(int):
    """ MyInt class extending int"""

    def __eq__(self, val):
        """Equality"""
        return self.real != val

    def __nq__(self, val):
        """Inequality"""
        return self.value == val
