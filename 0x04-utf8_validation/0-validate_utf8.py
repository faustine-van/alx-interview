#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """utf-8 functions"""
    for item in data:
        if item < 0x80:
            return True
        else:
            return False
