"""
lpthw-github
"""

import sys

def do_nothing():
    # this does nothing
    pass

def goodbye():
    # print goodbye world
    print("Goodbye, World ¯\_(ツ)_/¯")

if __name__ == '__main__':
    do_nothing()

    script,arg = sys.argv

    if arg == "goodbye":
        goodbye()
