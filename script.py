"""
lpthw-github
"""

import sys
import requests


def do_nothing():
    # this does nothing
    pass


def goodbye():
    # print goodbye world
    print("Goodbye, World ¯\_(ツ)_/¯")


# Printing "Hello World!"
def print_hello():
    print("Hello World!")


# Get a Random Quote.
def get_quote():
    url = "https://programming-quotes-api.herokuapp.com/quotes/random"
    r = requests.get(url)
    dict = r.json()
    quote = dict['en']

    print(quote)


if __name__ == '__main__':
    do_nothing()

    script, arg = sys.argv

    if arg == "hello":
        print_hello()
    elif arg == "goodbye":
        goodbye()
    elif arg == "quote":
        get_quote()
    else:
        print("nothing")
