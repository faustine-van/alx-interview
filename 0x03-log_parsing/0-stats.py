#!/usr/bin/python3
"""script that reads stdin line by line
   and computes metrics
"""
import sys


def print_statistics(total_size, status_code_counts):
    """print"""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")


if __name__ == "__main__":

    line_number = 0
    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    sumAll = 0
    stats = {k: 0 for k in codes}

    try:
        for line in sys.stdin:
            line_number += 1
            args = line.split()
            try:
                sumAll += int(args[-1])
            except BaseException:
                pass
            try:
                status_code = int(args[-2])
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            if line_number % 10 == 0:
                print_statistics(sumAll, stats)
        print_statistics(sumAll, stats)
    except KeyboardInterrupt:
        print_statistics(sumAll, stats)
        sys.exit(0)
