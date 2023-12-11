#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = list(a_dictionary.keys())
    ls.sort()
    for key in ls:
        print("{}: {}".format(key, a_dictionary.get(key)))
