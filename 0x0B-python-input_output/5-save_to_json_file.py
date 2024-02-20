#!/usr/bin/python3
""" Save object to a file """
import json


def save_to_json_file(my_obj, filename):
    """ Save an object to a file """
    with open(filename, "w") as file:
        content = json.dumps(my_obj)
        file.write(content)
