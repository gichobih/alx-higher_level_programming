#!/usr/bin/python3
"""
Module: 1-write_file
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)

