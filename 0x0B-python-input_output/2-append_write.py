#!/usr/bin/python3
"""
Module content

appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
