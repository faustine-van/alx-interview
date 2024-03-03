#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    possibles = []
    n = len(coins)
    count = 0
    i = n - 1
    while (i >= 0):
        while total >= coins[i]:
            total -= coins[i]
            possibles.append(coins[i])
            count += 1
            if total == 0:
                break
        i -= 1
    if total != 0:
        return -1
    # return count or
    return len(possibles)
