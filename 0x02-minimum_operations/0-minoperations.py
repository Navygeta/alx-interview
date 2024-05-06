#!/usr/bin/python3
"""Minimum Operations"""


def primeFactorization(x):
    """Returns prime factorization elements of x"""
    div = 2
    array = list()
    while (div <= x):
        if x % div == 0:
            array.append(div)
            x /= div
        else:
            div += 1

    return array


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    min_ops = 0
    factors = [x for x in primeFactorization(n)]
    occurrences = {item: factors.count(item) for item in factors}
    for k, v in occurrences.items():
        min_ops += k * v
    return min_ops
