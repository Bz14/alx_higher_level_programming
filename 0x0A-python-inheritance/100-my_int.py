#!/usr/bin/python3
""" Definfing MyInt """

class MyInt(int):
    """A rebel of integer class """
    def __eq__(self, other):
        """ Override function equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Override not equal """
        return super().__eq__(other)
