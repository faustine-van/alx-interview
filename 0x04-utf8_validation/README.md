# 0x04. UTF-8 Validation

The problem is to determine whether a given data set represents a valid UTF-8 encoding.
UTF-8 is a variable-width character encoding that can represent characters
using 1 to 4 bytes. Each byte in the encoding has specific bit patterns
that indicate its role in the representation of a character.

### Here are the key points in the problem:

1. Data Set Representation: The input data set is represented by a list of integers,
   where each integer represents 1 byte of data. Since UTF-8 characters can have up
   to 4 bytes, the data set can contain multiple integers.

2. Character Lengths: A character in UTF-8 can be 1 to 4 bytes long.
   The number of leading high-order bits in the first byte determines the length of the character.

3. Validation Rules:
  - For a 1-byte character, the leading bit must be 0.
  - For a 2-byte character, the leading bits must be 110.
  - For a 3-byte character, the leading bits must be 1110.
  - For a 4-byte character, the leading bits must be 11110.
  - All continuation bytes (bytes following the first byte of a
    multi-byte character) must have the leading bits 10.
4. Handling 8 Least Significant Bits: Since the input consists of
   integers representing bytes, the validation process should focus
   on the 8 least significant bits of each integer.

The provided method validUTF8(data) checks these rules by iterating through the
data set and validating each byte according to UTF-8 encoding standards.
It uses a helper function isContinuation to check if a given byte is a valid
continuation byte. The method returns True if the data set represents a
valid UTF-8 encoding, and False otherwise
