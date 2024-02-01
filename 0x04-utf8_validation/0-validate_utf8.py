#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """utf-8 functions"""
    try:
        decode_data = bytes(data).decode('utf-8')
        return True
    except (ValueError, UnicodeDecodeError):
        return False
