#!/usr/bin/python3
""" A module for printing a name """


def say_my_name(first_name, last_name=""):
    """
    Prints a full name
    Args:
       first_name: first name
       last_name: last name
    Raises:
         TypeError: I first and last name are not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
