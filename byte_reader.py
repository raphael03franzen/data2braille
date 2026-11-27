#!/usr/bin/env python3
import sys

while True:
	byte = sys.stdin.buffer.read(1)
	if not byte:
		break
	code_point = 0x2800+byte[0]
	char = chr(code_point)
	print(f'{char}', end="")
print()
