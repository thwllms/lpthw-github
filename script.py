"""
lpthw-github
"""

import sys
from exchangeratesapi import Api

def do_nothing():
    # this does nothing
    pass

def goodbye():
    # print goodbye world
    print("Goodbye, World ¯\_(ツ)_/¯")

# Printing "Hello World!"
def print_hello():
    print("Hello World!")

# Print exchange rates
def get_exchange_rates():
    api = Api()

    # Get the latest foreign exchange rates:
    print(api.get_rates('USD'))


if __name__ == '__main__':
    do_nothing()

    script, arg = sys.argv

    if arg == "hello":
        print_hello()
    elif arg == "rates":
        get_exchange_rates()
    elif arg == "goodbye":
        goodbye()
    else:
        print("nothing")
