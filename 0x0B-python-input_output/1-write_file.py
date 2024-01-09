#!/usr/bin/python3
""" A module to write a content to a file."""


def write_file(filename="", text=""):
    """ Writing to a file
    Args:
       filename: name of the file
       text: The content to be written
    """
    char_write = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        char_write = f.write(text)
    return char_write
