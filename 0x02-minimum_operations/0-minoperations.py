#!/usr/bin/python3
"""
This module contains a function to calculate the minimum
number of operations required to reach a given number of 'H' characters.

The operations allowed are:
- Copy All: Copy all the characters present on the screen.
- Paste: Paste the characters that were last copied.

Example usage:
>>> minOperations(4)
4
>>> minOperations(12)
7
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    required to reach a given number of 'H' characters.

    Args:
        n (int): The target number of 'H' characters to reach.

    Returns:
        int: The minimum number of operations required
            to reach `n` 'H' characters.
    """

    # Start with one 'H' character and no operations
    no_of_operations = 0
    factor = 2

    while n > 1:
        # Factorize `n`
        while n % factor == 0:
            no_of_operations += factor
            n //= factor
        factor += 1

    return no_of_operations
