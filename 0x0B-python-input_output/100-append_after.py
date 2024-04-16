#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing the search string.
    """
    # Open the file for reading and writing
    with open(filename, 'r+') as file:
        # Read the lines of the file
        lines = file.readlines()

        # Iterate through the lines
        for i, line in enumerate(lines):
            # Check if the search string is in the line
            if search_string in line:
                # Insert the new string after the line
                lines.insert(i + 1, new_string)

        # Move the cursor to the beginning of the file
        file.seek(0)

        # Write the modified lines back to the file
        file.writelines(lines)

if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

