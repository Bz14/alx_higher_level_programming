#!/usr/bin/python3
""" The mosule contain function that read the content of a file."""


def read_file(filename=""):
    """ A function to read from a file
    Args:
       filename: name of the file """
    file_content = 'Hi'
    with open(filename, mode='r', encoding="utf-8") as f:
        file_content = f.read()
    print(file_content)
