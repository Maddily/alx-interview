#!/usr/bin/python3
from collections import deque

"""
This module contains a function to determine
if all the lockboxes can be unlocked.

The function `canUnlockAll` takes a list of lists `boxes` as input,
where each inner list represents a lockbox.
Each lockbox contains a list of keys that can unlock other lockboxes.
The function returns True if all the lockboxes can be unlocked,
and False otherwise.
"""


def canUnlockAll(boxes):
    """
    Determine if all the lockboxes can be unlocked.

    Args:
      boxes (list): A list of lists representing the lockboxes.

    Returns:
      bool: True if all the lockboxes can be unlocked, False otherwise.
    """

    queue = deque()
    visited = set()

    if len(boxes) >= 1:
        visited.add(0)

    queue += boxes[0]

    while queue:
        box = queue.popleft()
        if box not in visited:
            visited.add(box)
            queue += boxes[box]

    if len(visited) == len(boxes):
        return True

    return False
