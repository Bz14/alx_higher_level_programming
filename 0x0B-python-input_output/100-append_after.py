#!/usr/bin/python3
""" A module appending to a file"""


def append_after(filename="", search_string="", new_string=""):
    """ A function to insert a line of text to a file """
    text = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            text += line
            if search_string in line:
                text += newString
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
