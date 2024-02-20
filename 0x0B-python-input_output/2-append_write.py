#!/usr/bin/python3
""" Appending a content to a file """


def append_write(filename="", text=""):
    """ Append to a file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
