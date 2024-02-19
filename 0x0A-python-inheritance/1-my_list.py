#!/usr/bin/python3
""" A class inherits a list """

class MyList(list):
    """ A list class """
    def print_sorted(self):
        """ Print sorted list """
        newList = sorted(self)
        print(newList)
