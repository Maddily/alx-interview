#!/usr/bin/python3
"""
This module contains a function called `isWinner`
that determines the winner of a prime number game.
"""


def isWinner(x, nums):
    """
    Determine the winner of a prime game.

    Args:
      x (int): The number of rounds to play.
      nums (list): A list of integers representing
      the range of numbers to be played each round.

    Returns:
      str or None: The name of the winner ('Maria' or 'Ben')
      or None if there is a tie.
    """

    if not nums or x <= 0 or x != len(nums):
        return None

    cache = {}

    points = {'maria': 0, 'ben': 0}

    largest_n = max(nums)

    if largest_n != 1:
        numbers_in_largest_n = list(range(2, largest_n + 1))
        # The index of the first prime number (2)
        p = 0
        # While the current prime number is less than the square root of n,
        # remove the numbers that are multiples
        # of the current prime number (composite numbers)
        while numbers_in_largest_n[p] * numbers_in_largest_n[p] <= largest_n:
            for j in range(p + 1, len(numbers_in_largest_n)):
                if numbers_in_largest_n[j] % numbers_in_largest_n[p] == 0:
                    numbers_in_largest_n[j] = 0

            p += 1
            while numbers_in_largest_n[p] == 0:
                p += 1

    while x > 0:
        n = nums.pop()

        # The name of the player who played last
        last_played = 'ben'

        if n == 1:
            points['ben'] += 1
            x -= 1
            continue

        # Extract the range of numbers for this `n` from the already-generated
        # `numbers_in_largest_n` list
        numbers = numbers_in_largest_n[0:n - 1]

        # Check if the winner for this range is cached
        if len(numbers) in cache:
            points[cache[len(numbers)]] += 1
            x -= 1
            continue

        # Remove the 0s and keep only the prime numbers
        prime_numbers = [number for number in numbers if number != 0]

        # Let Maria and Ben take turns playing
        while prime_numbers:
            prime_numbers.pop()
            last_played = 'maria' if last_played == 'ben' else 'ben'

        points[last_played] += 1
        cache[len(numbers)] = last_played
        x -= 1

    if points['maria'] == points['ben']:
        return None
    return 'Maria' if points['maria'] > points['ben'] else 'Ben'
