#!/usr/bin/python3
""" Creating an object from a file """
import json


def load_from_json_file(filename):
    """ Creating an object from a JSOn file """
    with open(filename) as f:
        content = f.read()
        return json.loads(content)
