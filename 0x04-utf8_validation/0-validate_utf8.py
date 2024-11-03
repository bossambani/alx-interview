#!/usr/bin/python3
"""0-validate_utf8.py"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers where each integer represents a byte
                             (0-255) of data to be checked for UTF-8 validity.

    Returns:
        bool: True if the data set represents valid UTF-8 encoding, False otherwise.

    The function processes each byte in the input data as follows:

    1. It initializes `num_bytes` to 0, which tracks how many additional bytes
       are expected to complete a multi-byte UTF-8 character.
       
    2. It iterates over each integer `num` in the `data` list:
       - If any byte is greater than 255, it returns False since valid byte values
         must be in the range 0-255.
       - If `num_bytes` is 0 (indicating a new character):
         - It checks the first byte to determine the number of bytes in the character
           based on its leading bits:
           - If the first two bits are `110`, it expects 1 more byte (2-byte character).
           - If the first three bits are `1110`, it expects 2 more bytes (3-byte character).
           - If the first four bits are `11110`, it expects 3 more bytes (4-byte character).
           - If the first bit is `1` and not in the above formats, it returns False as
             it indicates an invalid start byte.
       - If `num_bytes` is greater than 0 (indicating a continuation byte):
         - It checks that the current byte starts with `10` (continuation byte pattern).
         - If not, it returns False.
         - It decrements `num_bytes` by 1 to account for the processed continuation byte.

    3. After processing all bytes, the function returns True if `num_bytes` is 0,
       indicating all multi-byte characters were completed correctly, or False otherwise.
    """
    num_bytes = 0

    for num in data:
        if num > 255:
            return False
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
