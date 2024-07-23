#!/usr/bin/python3
"""
This module contains a function to validate whether a given
list of integers represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing a UTF-8 encoding.

    Returns:
        bool: True if the encoding is valid, False otherwise.
    """

    n = len(data)
    i = 0

    while i < n:
        leader_byte = data[i] & 0xFF

        if leader_byte not in range(0, 256):
            return False

        # Determine the number of bytes in a sequence
        if leader_byte in range(0, 128):
            number_of_bytes = 1
        elif leader_byte in range(192, 224):
            number_of_bytes = 2
        elif leader_byte in range(224, 240):
            number_of_bytes = 3
        elif leader_byte in range(240, 248):
            number_of_bytes = 4
        else:
            return False

        # Check if the remaining bytes are enough to complete a sequence
        if i + number_of_bytes > n:
            return False

        # Check trailing bytes
        for j in range(1, number_of_bytes):
            if data[i + j] & 0xFF not in range(128, 192):
                return False

        i += number_of_bytes

    return True
