#!/usr/bin/python3
import sys

if len(sys.argv) == 2 and sys.argv[1] != "-":
    filename = sys.argv[1]
else:
    filename = "/dev/stdin"

print(f"Opening {filename}",file=sys.stderr)
try:
    with open(filename, 'rb') as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            code_point = 0x2800 + byte[0]
            char = chr(code_point)
            print(f'{char}', end="")
    print()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.",file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}",file=sys.stderr)
    sys.exit(1)
