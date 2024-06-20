#!/usr/bin/env python3

def min_coins(coins, amt):
    if amt <= 0:
        return 0

    # Initialize dp array with amt + 1 (which acts as "infinity")
    dp = [amt + 1] * (amt + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amt + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amt] if dp[amt] != amt + 1 else -1
