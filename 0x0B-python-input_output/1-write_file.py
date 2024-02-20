#!/usr/bin/python3
""" Writing to a file """


def write_file(filename="", text=""):
    """ Writing a text to a file """
    with open(filename, "w", encoding="utf-8") as f:
        length = f.write(text)
        return length
