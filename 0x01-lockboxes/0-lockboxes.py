#!/usr/bin/python3
"""
This module contains a function to determine
if all the lockboxes can be unlocked.

The function `canUnlockAll` takes a list of lists `boxes` as input,
where each inner list represents a lockbox.
Each lockbox contains a list of keys that can unlock other lockboxes.
The function returns True if all the lockboxes can be unlocked,
and False otherwise.
"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all the lockboxes can be unlocked.

    Args:
      boxes (list): A list of lists representing the lockboxes.

    Returns:
      bool: True if all the lockboxes can be unlocked, False otherwise.
    """

    queue = deque()

    if not boxes:
        return True

    visited = {0}
    queue += boxes[0]

    while queue:
        box = queue.popleft()
        if box not in visited and box < len(boxes):
            visited.add(box)
            queue += boxes[box]

    if len(visited) == len(boxes):
        return True

    return False
