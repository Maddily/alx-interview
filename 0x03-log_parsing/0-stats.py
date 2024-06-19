#!/usr/bin/python3
"""
This script parses log files and calculates statistics
such as file size and status code occurrences.
"""

import re
import sys
import signal


count = 0
size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def match_line(line):
    """
    Match a line against a specific pattern.

    Args:
        line (str): The line to match.

    Returns:
        re.Match: A match object if the line matches the pattern,
            None otherwise.
    """

    pattern = re.compile(r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
                         + r'\[(?P<date>[^\]]+)\] '
                         + r'"GET /projects/260 HTTP/1\.1" '
                         + r'(?P<status>\d{3}) (?P<size>\d{1,4})')
    match = pattern.match(line)
    return match


def print_statistics():
    """
    Print the calculated statistics.

    Args:
        size (int): The total file size.
        status_codes (dict): A dictionary containing status codes
            and their occurrences.
    """

    global size, status_codes

    print(f'File size: {size}')
    for code, occurrences in sorted(status_codes.items()):
        if occurrences > 0:
            print(f'{code}: {occurrences}')


def interrupt_handler(signum, frame):
    """
    Handle the interrupt signal (SIGINT).

    Args:
        signum (int): The signal number.
        frame (frame): The current stack frame.
    """

    print_statistics()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, interrupt_handler)

    for line in sys.stdin:
        match = match_line(line)
        if match is None:
            continue

        size += int(match.group('size'))
        status_code = match.group('status')

        if status_code in status_codes:
            status_codes[status_code] += 1

        count += 1
        if count % 10 == 0:
            print_statistics()

    print_statistics()
