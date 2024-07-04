#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of a game played between Maria and Ben over
    multiple rounds.

    In each round, they start with a set of consecutive integers from 1 to n.
    Maria and Ben take turns choosing a prime number from the set and removing
    that number and all its multiples from the set. The player who cannot make
    a move loses the game. Maria always goes first, and both players play
    optimally.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): An array of integers where each integer represents
                            the upper bound of the set of numbers for each
                            round.

    Returns:
        str: The name of the player ("Maria" or "Ben") who won the most rounds.
             If the winner cannot be determined, return None.

    """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Step 1: Use Sieve of Eratosthenes to find all prime numbers up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    # Precompute the number of primes up to each number i (0 to max_n)
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Step 2: Simulate the game for each n in nums
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 3: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
