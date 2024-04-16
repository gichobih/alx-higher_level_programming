#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after each line containing the search string.
    """
    # Open the file for reading and writing
    with open(filename, 'r+') as file:
        # Read all lines of the file
        lines = file.readlines()
        
        # Go back to the beginning of the file
        file.seek(0)

        # Iterate through the lines
        for line in lines:
            # Write the current line to the file
            file.write(line)
            # If the search string is found in the current line, append the new string
            if search_string in line:
                file.write(new_string)
        
        # Ensure that any remaining content in the file is preserved
        file.truncate()

if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

