#!/usr/bin/python3
""" A module to append to a file."""


def append_write(filename="", text=""):
    """ Appending to a file
    Args:
       filename: Name of the file
       text: Content to be written to the file
   """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
