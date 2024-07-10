#!/usr/bin/python3
#Function that divides 2 integers and prints the result.

def safe_print_division(a, b):
    """
    divides two integers and prints the result
    catches divide by zero exception
    """
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
