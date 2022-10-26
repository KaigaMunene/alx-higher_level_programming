#!/usr/bin/python3
"""
Divides all elements of a matrix.
matrix must be a list of lists of int or float,
otherwise raise a TypeError exception.
Returns: A new matrix
"""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """
    answer = []
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_error)

        answer.append([round(element / div, 2) for element in row])

    return answer
