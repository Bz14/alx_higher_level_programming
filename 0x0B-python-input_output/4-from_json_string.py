#!/usr/bin/python
""" Converting to object from json """


def from_json_string(my_str):
    """ Converting json to string """
    import json
    return json.loads(my_str)
