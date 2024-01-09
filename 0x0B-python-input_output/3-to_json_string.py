#!/usr/bin/python3
""" A module to return json representation """

import json


def to_json_string(my_obj):
    """ A funtion to return json representation
    Args:
       my_obj: object to be serialized
    """
    return json.dumps(my_obj)
