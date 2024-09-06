#!/usr/bin/python3
"""utf8 validation
"""


def validUTF8(data):
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
