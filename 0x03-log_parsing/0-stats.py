#!/usr/bin/python3
"""Log Parsing"""


import sys
import re
from collections import defaultdict


total = 0
s_counts = defaultdict(int)
l_count = 0

pattern = re.compile(
    r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    print(f"File size: {total}")
    for status in sorted(s_counts):
        if s_counts[status] > 0:
            print(f"{status}: {s_counts[status]}")


try:
    for line in sys.stdin:
        l_count += 1
        match = pattern.match(line.strip())
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            total += file_size
            s_counts[status_code] += 1

        if l_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
