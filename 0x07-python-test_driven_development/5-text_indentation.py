#!/usr/bin/python3
"""
prints a text with 2 new lines after certain characters
"""


def text_indentation(text):
    """
    Outputs text argument verbatim with the exception of adding
    a newline if it encounters a '.', '?', ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
