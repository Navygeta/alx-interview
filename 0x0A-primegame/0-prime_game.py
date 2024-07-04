#!/usr/bin/python3

def isWinner(x, nums):
    def sieve_of_eratosthenes(max_num):
        """
        Return a list of primes up to max_num using Sieve of Eratosthenes
        """
        if max_num < 2:
            return []
        is_prime = [True] * (max_num + 1)
        p = 2
        while p * p <= max_num:
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, max_num + 1) if is_prime[p]]

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        if n == 1:
            # Ben wins directly if n is 1 because there are no primes to pick
            wins['Ben'] += 1
            continue

        available = set(range(1, n + 1))
        current_player = 'Maria'

        while True:
            found_move = False
            for prime in primes:
                if prime > n:
                    break
                if prime in available:
                    found_move = True
                    # Remove prime and its multiples from available numbers
                    for multiple in range(prime, n + 1, prime):
                        if multiple in available:
                            available.remove(multiple)
                    break

            if not found_move:
                break

            # Switch turn
            current_player = 'Ben' if current_player == 'Maria' else 'Maria'

        # After the loop, current_player cannot make a move
        if current_player == 'Maria':
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
