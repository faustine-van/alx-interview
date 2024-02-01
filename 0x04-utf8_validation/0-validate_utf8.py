#!/usr/bin/python3
"""utf-8 validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """utf-8 functions"""
    try:
        decode_data = bytes(data).decode('utf-8')
        return True
    except (ValueError, UnicodeDecodeError):
        return False
