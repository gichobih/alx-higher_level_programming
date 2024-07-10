#!/usr/bin/python3
#Function that executes a function safely.
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as e:
        res = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return res
