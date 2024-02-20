#!/usr/bin/python3
""" Reading from a file. """


def read_file(filename=""):
    """ Read the content of a file """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
