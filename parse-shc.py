#!/usr/bin/env python3

import re
import sys


def invert_ord(s: str) -> str:
    fixed_offset = 45
    value = int(s)
    return chr(value + fixed_offset)


raw_data = input()
if raw_data is None:
    print("Missing input data")
    exit(1)
if not raw_data.startswith("shc:/"):
    print("Content is not a smart health card, unable to process", file=sys.stderr)
    exit(1)

data = raw_data.lstrip("shc:/")
encoded_characters = re.findall(r"..", data)
decoded_characters = ''.join(list(map(invert_ord, encoded_characters)))

print(decoded_characters)

