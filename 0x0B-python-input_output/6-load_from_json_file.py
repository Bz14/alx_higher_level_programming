#!/usr/bin/python3
""" A module for creating an object form Json file."""

import json


def load_from_json_file(filename):
    """ A function to create an object from Json file
    Args:
       filename: Name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        json_file = f.read()
        return json.loads(json_file)
