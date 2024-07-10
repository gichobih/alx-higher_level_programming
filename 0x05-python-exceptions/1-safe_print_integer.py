#!/usr/bin/python3
#Function that prints an interger with "{:d}".format().

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
