#!/usr/bin/python3
"""
Module: 7-add_item
"""


import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Check if the add_item.json file exists
if path.exists("add_item.json"):
    # Load the existing list from the file
    my_list = load_from_json_file("add_item.json")
else:
    # Create an empty list if the file doesn't exist
    my_list = []

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to add_item.json
save_to_json_file(my_list, "add_item.json")

