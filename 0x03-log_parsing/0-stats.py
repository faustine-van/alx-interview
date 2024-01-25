#!/usr/bin/python3
"""script that reads stdin line by line
   and computes metrics
"""
import fileinput
import re


if __name__ == "__main__":

    line_number = 0
    ip = r'(\d+\.\d+\.\d+\.\d+)'
    date = r'\[(\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]'
    status = r'"GET \/projects\/260 HTTP\/1\.1"'
    match = f'{ip} - {date} {status} (\\d+) (\\d+)'

    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    sumAll = []
    times = []
    n_of_counts = {}
    for line in fileinput.input():
        if not re.search(match, line):
            continue
        line_number += 1
        args = line.split()
        sumAll.append(int(args[-1]))
        times.append(int(args[-2]))

        if line_number % 10 == 0:
            # after 10 line do this
            # print(times)
            for i in sorted(times):
                if i in n_of_counts and i in codes:
                    n_of_counts[i] += 1
                else:
                    n_of_counts[i] = 1
                times = []
            print(f'File size: {sum(sumAll)}')
            for key, val in n_of_counts.items():
                for num in sorted(codes):
                    if num == key:
                        print(f'{num}: {val}')
