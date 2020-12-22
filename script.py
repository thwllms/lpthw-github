"""
lpthw-github
"""

import sys
import requests
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


def qwerty():
    print('qwerty')


def get_quote():
    """
    Get a random quote from an online api.
    """
    url = "https://programming-quotes-api.herokuapp.com/quotes/random"
    r = requests.get(url)
    dict = r.json()
    quote = dict['en']

    print(quote)


def blah():
    print('blah')


def city():
	city_name = input("Which city do you live in? ")
	print('Greetings to {}!'.format(city_name))


if __name__ == '__main__':
    do_nothing()

    script, arg = sys.argv

    if arg == "hello":
        print_hello()
    elif arg == "rates":
        get_exchange_rates()
    elif arg == "goodbye":
        goodbye()
    elif arg == 'qwerty':
        qwerty()
    elif arg == "quote":
        get_quote()
    elif arg == 'blah':
        blah()
    elif arg == 'city':
    	city()
    else:
        print("nothing")
