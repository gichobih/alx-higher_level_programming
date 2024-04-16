#!/usr/bin/python3
import sys

def print_metrics(total_size, status_counts):
    """
    Print the computed metrics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts of each status code.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts.get(status_code, 0)
        if count > 0:
            print("{}: {}".format(status_code, count))

def parse_line(line):
    """
    Parse a line to extract file size and status code.

    Args:
        line (str): Input line.

    Returns:
        tuple: A tuple containing file size (int) and status code (str).
    """
    parts = line.split()
    size = int(parts[-1])
    status = parts[-2]
    return size, status

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            size, status = parse_line(line)
            total_size += size
            status_counts[status] = status_counts.get(status, 0) + 1

            if i % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()

