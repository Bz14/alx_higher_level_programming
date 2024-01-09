#!/usr/bin/python3
""" A module to decode Json object to python object """

import json


def from_json_string(my_str):
    """ A function to deconde Json to python object
    Args:
       my_str: Json object
    """
    return json.loads(my_str)
