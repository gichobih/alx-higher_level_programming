#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        # Initialize the new row with 1 at the beginning
        row = [1]

        # Generate the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Append 1 at the end of the row
        row.append(1)

        # Add the new row to the triangle
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """
    Print the triangle

    Args:
        triangle (list of lists): The Pascal's triangle to print
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)

