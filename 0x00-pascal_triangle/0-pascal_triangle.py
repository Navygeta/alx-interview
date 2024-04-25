#!/usr/bin/python3

"""
Generates Pascal's Triangle up to the nth row.

Args:
    n (int): The number of rows in Pascal's Triangle.

Returns:
    list of lists: Pascal's Triangle up to the nth row.
        Each row is represented as a list of integers.

Note:
    Returns an empty list if n <= 0.
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
