#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = sorted(a_dictionary.keys())
    for key in ls:
        print(f"{key}: {a_dictionary[key]}")
