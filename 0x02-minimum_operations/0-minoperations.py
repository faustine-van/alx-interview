#!/usr/bin/python3
"""find minimum operation
   for given number
"""


def minOperations(n):
    """minOperations()
       n: give number
       return min operations
    """
    text = "H"
    result = [text]
    for _ in range(2):
        # count = 1
        #  if len(result[-1]) <= n:
        text += text
        result.append(text)
        if len(result[-1]) <= n:
            text = result[-1]
            result.append(text)
        # count = count + 1
    return result
