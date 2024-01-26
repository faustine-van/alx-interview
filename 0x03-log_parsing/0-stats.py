#!/usr/bin/python3
"""script that reads stdin line by line
   and computes metrics
"""
import sys


def print_statistics(total_size, status_code_counts):
    """print"""
    if total_size > 0:
        print(f"File size: {total_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


if __name__ == "__main__":
    line_number = 0
    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    sumAll = 0
    times = []
    n_of_counts = {}
    try:
        for line in sys.stdin:
            args = line.split()
            try:
                sumAll += int(args[-1])
                times.append(int(args[-2]))
            except BaseException:
                pass
            # print(times)
            line_number += 1
            if line_number % 10 == 0:
                try:
                    for i in sorted(times):
                        if i is None or not isinstance(i, int):
                            continue
                        if i in n_of_counts and i in codes:
                            n_of_counts[i] += 1
                        else:
                            n_of_counts[i] = 1
                except BaseException:
                    pass
                print_statistics(sumAll, n_of_counts)
                times = []
    except KeyboardInterrupt:
        print_statistics(sumAll, n_of_counts)
        sys.exit(0)
    print_statistics(sumAll, n_of_counts)
