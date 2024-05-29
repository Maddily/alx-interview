#!/usr/bin/python3
"""
A module to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates the first n rows of Pascal's Triangle.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists of integers
        representing the first n rows of Pascal's Triangle.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [
          1 if j == 0 or j == i
          else triangle[i - 1][j - 1] + triangle[i - 1][j]
          for j in range(i + 1)
          ]

        triangle.append(row)

    return triangle
