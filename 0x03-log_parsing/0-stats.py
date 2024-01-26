#!/usr/bin/python3
""""""
import sys
from collections import defaultdict


def print_statistics(total_size, status_code_counts):
    """"""
    print(f"Total file size: {total_size}")
    for code in sorted([200, 301, 400, 401, 403, 404, 405, 500]):
        count = status_code_counts[code]
        print(f"{code}: {count}")


def process_line(line):
    """"""
    parts = line.split()
    start = parts[6].startswith('/projects/')
    if len(parts) != 10 or parts[5] != '"GET' or not start:
        return None

    ip_address = parts[0]
    status_code = parts[8]

    try:
        file_size = int(parts[9])
    except (ValueError, IndexError):
        return None

    return ip_address, status_code, file_size


def main():
    """"""
    total_size = 0
    status_code_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            data = process_line(line)

            if data:
                ip_address, status_code, file_size = data
                total_size += file_size
                status_code_counts[status_code] += 1
                lines_processed += 1

                if lines_processed % 10 == 0:
