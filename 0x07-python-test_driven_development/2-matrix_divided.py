#!/usr/bin/python3

"""
Function that divides
Return quotient in matrix

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"

    if not matrix:
        raise TypeError(err1)

    if matrix == [[]] or matrix == []:
        raise TypeError(err1)

    count = len(matrix[0])

    for lists in matrix:
        comp = len(lists)
        for ele in lists:

            if not isinstance(ele, (int, float)):
                raise TypeError(err1)
        if comp != count:
            raise TypeError(err2)

    if not isinstance(div, (int, float)):
        raise TypeError(err3)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(i/div, 2) for i in row] for row in matrix]

    return new
