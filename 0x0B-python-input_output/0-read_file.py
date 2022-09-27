#!/usr/bin/pyhton3
"""
Module content

contains function to read UTF8 text filles and print to stdout
"""


def read_file(filename=""):
    """ Function that reads a text file and prints it to stdout """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
