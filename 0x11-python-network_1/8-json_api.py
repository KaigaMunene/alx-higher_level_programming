#!/usr/bin/python3
"""
Send POST request to URL with letter param, display different output
depending on if response contains valid JSON object
"""

from requests import post
from sys import argv


if __name__ == "__main__":
    """ Make POST request with param and display customized output """

    q = argv[1] if len(argv) > 1 else ""

    response = post("http://0.0.0.0:5000/search_user", data={'q': q})
    json = response.json()

    if json:
        if json["id"] and json["name"]:
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("Not a valid JSON")
    else:
        print("No result")
