#!/usr/bin/python3
""" Send POST request to URL with email address as URL paramter """

from requests import post
from sys import argv


if __name__ == "__main__":
    """ Display response body of POST request to URL with email param """

    response = post(argv[1], data={'email': argv[2]})
    print(response.text)
