#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """utf-8 functions"""
    try:
        decode_data = bytes(data)
        return True
    except (ValueError):
        return False
