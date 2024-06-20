#!/usr/bin/python3
"""Making Change function"""


def make_change(coins, total):
    """Determines the fewest number of coins needed to meet a given total."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count, value, index = 0, total, 0

    while value > 0 and index < len(coins):
        if value >= coins[index]:
            value -= coins[index]
            count += 1
        else:
            index += 1

    return count if value == 0 else -
