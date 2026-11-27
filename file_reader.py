#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
    print("Usage: python script.py <filename>",file=sys.stderr)
    sys.exit(1)

with open(filename, 'rb') as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        code_point = 0x2800 + byte[0]
        char = chr(code_point)
        print(f'{char}', end="")
print()
