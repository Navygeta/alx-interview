#!/usr/bin/python3
'''
This script determines the winner of a prime number game between Maria and Ben.
'''


def isWinner(x, nums):
    '''
    Determines the winner of the prime game based on the number of rounds won.

    Args:
        x (int): Number of rounds to play.
        nums (list): List of integers representing the # of items in each round

    Returns:
        str: Name of the winner ('Maria' or 'Ben'), or None if it's a tie.
    '''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    '''
    Determines the winner of a single round of the prime game.

    Args:
        n (int): Number of items in the round.
        x (int): Total number of rounds.

    Returns:
        str: Name of the round winner ('Maria' or 'Ben'), or None if no winner.
    '''
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num

        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del list[val - idx]
    return None


def isPrime(n):
    '''
    Checks if a number is prime.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    '''
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return False
        return True
