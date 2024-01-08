#!/usr/bin/python3
""" A module contain a class and method
to print sorted list"""


class MyList(list):
    """A class extending a list object """
    def print_sorted(self):
        """ A function to print a sorted list """
        sorted_list = sorted(self)
        print(sorted_list)
