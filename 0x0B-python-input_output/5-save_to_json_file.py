#!/usr/bin/python3
""" A module to write an object to a text file """

import json


def save_to_json_file(my_obj, filename):
    """ A function to save object to a file
    Args:
       my_obj: the object
       filename: The name of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
