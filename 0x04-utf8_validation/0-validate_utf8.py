#!/usr/bin/python3
"""utf-8 validation"""
from typing import List


def validUTF8(data):
    """utf-8 functions"""
    # keep number of continuation
    countBytes = 0
    for byte in data:
        if countBytes == 0:
            if byte >> 7 == 0b0:
                # Single-byte character
                continue
            elif byte >> 5 == 0b110:
                # Two-byte character
                countBytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character
                countBytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character
                countBytes = 3
            else:
                # Invalid leading byte
                return False
        else:
            if byte >> 6 == 0b10:
                # valid continuation byte
                countBytes -= 1
            else:
                # Invalid continuation byte
                return False
    return countBytes == 0
