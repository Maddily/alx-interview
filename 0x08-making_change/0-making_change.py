#!/usr/bin/python3
"""
This module contains a function to determine the minimum
number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins
    needed to meet a given total.

    Args:
        coins (list): A list of the values
        of the coins available.
        total (int): The total amount of money
        to make change for.

    Returns:
        int: The minimum number of coins needed to make
        the change, or -1 if it is not possible.
    """

    if total <= 0:
        return 0

    if len(coins) == 0:
        return -1

    coins.sort(reverse=True)
    number_of_coins_needed = 0

    for coin in coins:
        while total:
            if coin <= total:
                total -= coin
                number_of_coins_needed += 1
            else:
                break

    return number_of_coins_needed if total == 0 else -1
