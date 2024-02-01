#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
# ------------------------------------------------

# Valid UTF-8 Sequence
data1 = [65, 66, 67]  # ASCII characters 'A', 'B', 'C'
print(validUTF8(data1))  # Output: True

# Example 2: Invalid Leading Byte
data2 = [128, 65, 66]  # Invalid UTF-8 sequence
print(validUTF8(data2))  # Output: False

# Example 3: Valid Two-Byte Sequence
data3 = [195, 162]  # UTF-8 encoding of 'â'
print(validUTF8(data3))  # Output: True

# Example 4: Invalid Continuation Byte
data4 = [195, 65, 162]  # Invalid UTF-8 sequence
print(validUTF8(data4))  # Output: False

# Example 5: Incomplete Multi-Byte Character
data5 = [195]  # Incomplete UTF-8 sequence
print(validUTF8(data5))  # Output: False

print('--------------')
data6 = [65, 128]
print(validUTF8(data6))  # Output: False
print('--------------')
