#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """function"""
    if n <= 0:
        return []
    lists = [[1]]
    for row in range(1, n):
        tmp = [1]
        for i in range(len(lists[row - 1]) - 1):
            tmp.append(lists[row - 1][i] + lists[row - 1][i + 1])
        tmp.append(1)
        lists.append(tmp)
    return lists
