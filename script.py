"""
lpthw-github
"""

import sys


def do_nothing():
    # this does nothing
    pass


# Printing "Hello World!"
def print_hello():
    print("Hello World!")


if __name__ == '__main__':
    do_nothing()

    script, arg = sys.argv

    if arg == "hello":
        print_hello()
