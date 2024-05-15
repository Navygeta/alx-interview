#!/usr/bin/python3
"""
Log parsing

This script parses log data from standard input, calculates statistics such as
file size and occurrence of HTTP status codes, and prints the results.

Usage:
    The script reads log data from standard input. It expects each line of the
    log data to contain at least the status code and the file size separated
    by whitespace.

Example:
    cat logfile.txt | python3 log_parsing.py

The script continues to read input until interrupted (Ctrl+C).
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """Prints statistics about the log data.

        Args:
            stats (dict): A dictionary containing the count of each HTTP status
            code.
            file_size (int): The total size of log files in bytes.

        Returns:
            None
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
