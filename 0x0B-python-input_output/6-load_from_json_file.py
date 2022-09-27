#!/usr/bin/python3
"""
Module content

creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file” """
    with open(filename, encoding="utf-8") as f:
        json.loads(f)
