#!/usr/bin/python3
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    if (r == "" or r is None):
        return 0
    return -1


def roman_to_int(roman_string):
    res = 0
    i = 0
    while (i < len(roman_string)):
        string_1 = value(roman_string[i])
        if (i + 1 < len(roman_string)):
            string_2 = value(roman_string[i+1])
            if (string_1 >= string_2):
                res = res + string_1
                i = i + 1
            else:
                res = res + string_2 - string_1
                i = i + 2
        else:
            res = res + string_1
            i = i + 1
    return res
