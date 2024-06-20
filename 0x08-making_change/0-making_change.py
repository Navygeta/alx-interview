#!/usr/bin/env python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with total + 1 (which acts as "infinity")
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
