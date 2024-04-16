#!/usr/bin/python3
"""
Module: 5-save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file using a JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

