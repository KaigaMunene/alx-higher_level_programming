#!/usr/bin/python3
""" Send request to URL & dispaly value of X-Request-Id from response """

import urllib.request
from sys import argv


if __name__ == "__main__":
    """ Send request to URL argument and display parsed results """
    with urllib.request.urlopen(argv[1]) as response:
        for header in response.getheaders():
            if header[0] == 'X-Request-Id':
                print(header[1])
