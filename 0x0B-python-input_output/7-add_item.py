#!/usr/bin/python3
"""
Module content
Add all arguments to a Python list, and then save to a file
"""
import os.path
from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

obj = load_from_json_file("add_item.json") if os.path.exists(
    "add_item.json") else []

obj.extend(argv[1:])
save_to_json_file(obj, "add_item.json")
