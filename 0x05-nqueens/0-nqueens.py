#!/usr/bin/python3
"""
This solves the N queens problem.
"""
import sys


def is_safe_placement(row, column, row_col_repr):
    """ Checks if it's safe to place the queen at a position """

    for prev_row in range(row):
        prev_column = row_col_repr[prev_row]
        if (
                prev_column == column
                or abs(prev_column - column) == abs(prev_row - row)
        ):
            return False
    return True


def get_possible_solution(row_col_repr):
    """Returns a list representing a possible solution"""

    return [[row, row_col_repr[row]] for row in range(dimension)]


def backtrack(row, row_col_repr):
    """Recursively looks for positions to place queens"""

    if row == dimension:
        print(get_possible_solution(row_col_repr))
        return

    for column in range(dimension):
        if is_safe_placement(row, column, row_col_repr):
            row_col_repr[row] = column
            backtrack(row + 1, row_col_repr)
            row_col_repr[row] = -1


def place_queens(dimension):
    """
    Solves the N queens problem by placing N non-attacking queens
    on an N×N chessboard.
    """

    row_col_repr = [-1] * dimension

    backtrack(0, row_col_repr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        dimension = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if dimension < 4:
        print("N must be at least 4")
        sys.exit(1)

    place_queens(dimension)
