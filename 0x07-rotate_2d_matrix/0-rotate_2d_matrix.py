#!/usr/bin/python3
"""
This module defines a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    :param matrix: List of lists where each inner list represents a row
    :type matrix: list of list of int
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
