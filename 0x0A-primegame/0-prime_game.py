#!/usr/bin/python3
"""find winner for Prime Game"""

def isWinner(x, nums):
    """Prime Game
      Return: winner
    """
    def is_prime(num):
       """check if element in nums is prime"""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    # Count the wins for each player
    maria_wins = 0
    ben_wins = 0

    # Iterate over each round
    for n in nums:
        # Find all prime numbers up to n
        primes = [i for i in range(2, n + 1) if is_prime(i)]

        # Count the number of primes in the set
        prime_count = len(primes)

        # Determine the winner based on the parity of prime count
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
