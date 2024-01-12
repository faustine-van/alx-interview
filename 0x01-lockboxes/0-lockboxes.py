#!/usr/bin/python3
"""check Unlock box"""


def canUnlockAll(boxes):
    """Return True if all boxes
       can be opened,
       else return False
    """

    unlockedOnes = [0]
    for id, box in enumerate(boxes):
        if not box:
            continue
        for val in box:
            if val not in unlockedOnes and val < len(boxes) and val != id:
                unlockedOnes.append(val)
    if len(boxes) != len(unlockedOnes):
        return False
    return True
