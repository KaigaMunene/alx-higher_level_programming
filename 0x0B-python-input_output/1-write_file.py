#!/usr/bin/python3
"""
Module content

writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """
    function that writes a string to text file and
    prints its characters
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
