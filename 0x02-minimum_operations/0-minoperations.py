#!/usr/bin/python3
"""find minimum operation
   for given number
"""


def minOperations(n):
    """minOperations()
       n: give number
       return min operations
    """
    if n <= 0:
        return 0
    prime_factors = []
    # init 2 as smallest prime number
    ops = 2
    while ops * ops <= n:
        if n % ops == 0:
            prime_factors.append(ops)
            # update n ex: 6 (12 // 2).
            n //= ops
        else:
            ops = ops + 1
    # in case n is 1, so no action is needed.
    if n > 1:
        prime_factors.append(n)
    return sum(prime_factors)
