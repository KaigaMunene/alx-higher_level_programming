#!/usr/bin/python3
""" Send request to URL & dispaly value of X-Request-Id from response """

from requests import get
from sys import argv


if __name__ == "__main__":
    """ Send request to URL argument and display parsed results """

    response = get(argv[1])
    print(response.headers.get('X-Request-Id'))
